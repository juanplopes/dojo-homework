from collections import defaultdict, deque

class Erdometer:
    def __init__(self):
        self.authors = defaultdict(set)
 
    def add(self, *book):
        for author in book:
            self.authors[author].update(book)
        
    def rank(self, this_author):
        Q, V = deque(), set()

        Q.append((0, this_author))
        while len(Q):
            distance, author = Q.popleft()

            if author == 'Erdos': return distance
            if author in V: continue
            V.add(author)
            
            for coauthor in self.authors[author]:
                Q.append((distance+1, coauthor))

