from collections import defaultdict, deque

class Erdometer:
    def __init__(self):
        self.authors = defaultdict(set)
 
    def add(self, *book):
        for author in book:
            self.authors[author].update(book)
        
    def rank(self, author):
        Q, V = deque(), set()

        Q.append((0, author))
        while len(Q):
            i, item  = Q.popleft()

            if item == 'Erdos': return i
            if item in V: continue
            V.add(item)
            
            for other in self.authors[item]:
                Q.append((i+1, other))

