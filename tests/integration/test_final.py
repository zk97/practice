from pyrsistent import pmap, pvector, plist, s, pset
import atomos.atom as atom
import unittest
from unittest import mock
import final

class TestAppState(unittest.TestCase):
    
    def SetUp(self):
        final.app_state = None
    
    def test_init_value(self):
        return self.assertIsNone(final.app_state.deref())
    
    def test_load_file(self):
        file_path = 'tests/integration/test_file.txt'
        return self.assertIsNone(final.initialize_state(file_path))
    
    def test_loaded_file(self):
        file_path = 'tests/integration/test_file.txt'
        final.initialize_state(file_path)
        result = pmap({1: pset([2]), 2: pset([1, 4]), 4: pset([2])})
        return self.assertEqual(final.app_state.deref(), result)
    
    @mock.patch("final.app_state", atom.Atom(pmap({1: pset([2]), 2: pset([1, 4]), 4: pset([2])})))
    def test_add_edge(self):
        new_edge = plist([3, 4])
        result = pmap({1: pset([2]), 2: pset([1, 4]), 3: pset([4]), 4: pset([2,3])})
        return self.assertEqual(final.add_edge(new_edge), result)
    
class TestNetwork(unittest.TestCase):
    
    def SetUp(self):
        final.app_state = None
        
    @mock.patch("final.app_state", atom.Atom(pmap({1: pset([2]), 2: pset([1, 4]), 3: pset([5]),
                                                   4: pset([2]), 5: pset([3])})))
    def test_false_network(self):
        return self.assertFalse(final.is_same_network(1, 3))
    
    
    @mock.patch("final.app_state", atom.Atom(pmap({1: pset([2]), 2: pset([1, 4]), 3: pset([5]),
                                                   4: pset([2]), 5: pset([3])})))
    def test_true_network(self):
        return self.assertTrue(final.is_same_network(1, 4))
    
    
    
if __name__ == '__main__':
    unittest.main()