'''
Original problem: 
http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=2414
'''
from collections import defaultdict

def augment(G, V, source, sink):
    if source == sink:
        return True

    V.add(source)

    for next in G[source]:
        if next not in V and augment(G, V, next, sink):
            G[source].remove(next)
            G[next].add(source)
            return True
            
    return False

def laser(soldiers):
    G = defaultdict(set)

    for row, column in soldiers:
        r, c = 'row%d' % row, 'col%d' % column

        G[0].add(r)
        G[r].add(c)
        G[c].add(42)

    total = 0
    while augment(G, set(), 0, 42):
        total += 1
        
    return total
