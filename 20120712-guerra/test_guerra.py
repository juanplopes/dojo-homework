import unittest
from guerra import Relations

class TestRelations(unittest.TestCase):
    
    def setUp(self):
        self.relations = Relations()        
    
    def test_two_explicit_friends(self):
        self.relations.set_friends('A', 'B')
        self.assertTrue(self.relations.are_friends('A', 'B'))

    def test_two_explicit_friends_commutative(self):        
        self.relations.set_friends('A', 'B')
        self.assertTrue(self.relations.are_friends('B', 'A'))

    def test_non_declared_relation(self):        
        self.assertFalse(self.relations.are_friends('B', 'A'))
        self.assertFalse(self.relations.are_enemies('B', 'A'))
        
    def test_one_level_transitiveness(self):        
        self.relations.set_friends('A', 'B')
        self.relations.set_friends('B', 'C')
        self.assertTrue(self.relations.are_friends('A', 'C'))

    def test_two_level_transitiveness(self):        
        self.relations.set_friends('A', 'B')
        self.relations.set_friends('B', 'C')
        self.relations.set_friends('C', 'D')
        self.assertTrue(self.relations.are_friends('A', 'D'))

    def test_explicit_enemy(self):        
        self.relations.set_enemies('A', 'B')
        self.assertTrue(self.relations.are_enemies('A', 'B'))

    def test_implicit_enemy(self):        
        self.relations.set_friends('A', 'B')
        self.relations.set_enemies('B', 'C')
        self.assertTrue(self.relations.are_enemies('A', 'C'))

    def test_enemys_enemy(self):        
        self.relations.set_enemies('A', 'B')
        self.relations.set_enemies('B', 'C')
        self.assertTrue(self.relations.are_friends('A', 'C'))
        
    def test_enemys_implicit_enemy(self):        
        self.relations.set_friends('A', 'B')
        self.relations.set_enemies('B', 'C')
        self.relations.set_enemies('C', 'D')
        self.assertTrue(self.relations.are_friends('A', 'D'))
        
    def tearDown(self):
        self.relations = None

unittest.main()