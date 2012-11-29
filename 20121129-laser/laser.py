from collections import defaultdict

def augment(G, V, source, sink):
    if source == sink:
        return True

    V.add(source)

    for next in G[source]:
        if next not in V and augment(G, V, next, sink):
            del G[source][next]
            G[next][source] = True
            return True
            
    return False

def laser(soldiers):
    G = defaultdict(dict)

    for row, column in soldiers:
        r, c = 'R%s' % [row], 'C%s' % [column]

        G[0][r] = True
        G[r][c] = True
        G[c][42] = True

    total = 0
    while augment(G, set(), 0, 42):
        total += 1
        
    return total
