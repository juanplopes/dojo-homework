import unittest
from erdos import Erdometer

class TestErdometer(unittest.TestCase):
    def test_distance_from_erdos(self):
        erdometer = Erdometer()
        self.assertEqual(0, erdometer.distance('Erdos'))

    def test_distance_from_lopes(self):
        erdometer = Erdometer()
        erdometer.add('Erdos', 'Lopes')
        self.assertEqual(1, erdometer.distance('Lopes'))

    def test_distance_from_lopes_with_carvalho(self):
        erdometer = Erdometer()
        erdometer.add('Erdos', 'Lopes')
        erdometer.add('Lopes', 'Carvalho')
        self.assertEqual(1, erdometer.distance('Lopes'))

    def test_distance_from_carvalho(self):
        erdometer = Erdometer()
        erdometer.add('Erdos', 'Lopes')
        erdometer.add('Lopes', 'Carvalho')
        self.assertEqual(2, erdometer.distance('Carvalho'))

    def test_distance_from_abreu(self):
        erdometer = Erdometer()
        erdometer.add('Erdos', 'Lopes')
        erdometer.add('Lopes', 'Carvalho')
        erdometer.add('Carvalho', 'Abreu')
        self.assertEqual(3, erdometer.distance('Abreu'))

    def test_distance_from_thimoteo(self):
        erdometer = Erdometer()
        erdometer.add('Erdos', 'Lopes')
        erdometer.add('Lopes', 'Carvalho')
        erdometer.add('Carvalho', 'Abreu')
        erdometer.add('Abreu', 'Thimoteo')
        erdometer.add('Thimoteo', 'Erdos')
        self.assertEqual(1, erdometer.distance('Thimoteo'))

    def test_distance_from_thimoteo_to_lopes(self):
        erdometer = Erdometer()
        erdometer.add('Erdos', 'Lopes')
        erdometer.add('Lopes', 'Carvalho')
        erdometer.add('Carvalho', 'Abreu')
        erdometer.add('Abreu', 'Thimoteo')
        erdometer.add('Thimoteo', 'Erdos')
        self.assertEqual(2, erdometer.distance('Thimoteo', 'Lopes'))

    def test_distance_from_bernardes(self):
        erdometer = Erdometer()
        erdometer.add('Erdos', 'Lopes')
        erdometer.add('Bernardes', 'Carvalho')
        self.assertEqual(None, erdometer.distance('Bernardes'))


unittest.main()
