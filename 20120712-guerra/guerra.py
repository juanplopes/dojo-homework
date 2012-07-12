class Relations:
    def __init__(self):
        self.data = {}
 
    def find(self, v):
        if not v in self.data: 
            return v
        return self.find(self.data[v])
        
    def union(self, x, y):
        self.data[self.find(x)] = self.find(y)
        
    def set_friends(self, x, y):
        self.union((0, x), (0, y))
        self.union((1, x), (1, y))

    def set_enemies(self, x, y):
        self.union((0, x), (1, y))
        self.union((1, x), (0, y))
      
    def are_friends(self, x, y):
        return self.find((0, x)) == self.find((0, y))

    def are_enemies(self, x, y):
        return self.find((0, x)) == self.find((1, y))

