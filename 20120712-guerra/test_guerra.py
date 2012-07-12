import unittest
from guerra import Relations

class TestRelations(unittest.TestCase):
    def test_two_explicit_friends(self):
        relations = Relations()
        relations.set_friends('A', 'B')
        self.assertTrue(relations.are_friends('A', 'B'))

    def test_two_explicit_friends_commutative(self):
        relations = Relations()
        relations.set_friends('A', 'B')
        self.assertTrue(relations.are_friends('B', 'A'))

    def test_non_declared_relation(self):
        relations = Relations()
        self.assertFalse(relations.are_friends('B', 'A'))
        self.assertFalse(relations.are_enemies('B', 'A'))
        
    def test_one_level_transitiveness(self):
        relations = Relations()
        relations.set_friends('A', 'B')
        relations.set_friends('B', 'C')
        self.assertTrue(relations.are_friends('A', 'C'))

    def test_two_level_transitiveness(self):
        relations = Relations()
        relations.set_friends('A', 'B')
        relations.set_friends('B', 'C')
        relations.set_friends('C', 'D')
        self.assertTrue(relations.are_friends('A', 'D'))

    def test_explicit_enemy(self):
        relations = Relations()
        relations.set_enemies('A', 'B')
        self.assertTrue(relations.are_enemies('A', 'B'))

    def test_implicit_enemy(self):
        relations = Relations()
        relations.set_friends('A', 'B')
        relations.set_enemies('B', 'C')
        self.assertTrue(relations.are_enemies('A', 'C'))

    def test_enemys_enemy(self):
        relations = Relations()
        relations.set_enemies('A', 'B')
        relations.set_enemies('B', 'C')
        self.assertTrue(relations.are_friends('A', 'C'))
        
    def test_enemys_implicit_enemy(self):
        relations = Relations()
        relations.set_friends('A', 'B')
        relations.set_enemies('B', 'C')
        relations.set_enemies('C', 'D')
        self.assertTrue(relations.are_friends('A', 'D'))


unittest.main()
