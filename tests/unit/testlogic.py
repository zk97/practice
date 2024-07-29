from pyrsistent import pmap, pvector, plist, pset
import unittest
import logic


class TestStringEdge(unittest.TestCase):
    def test_string_edge(self):
        string = '1 2'
        result = plist([1,2])
        return self.assertEqual(logic.string_to_edge(string), result)
    
class TestFileContents(unittest.TestCase):
    def test_file_edges(self):
        string = '1 2\n'
        result = pvector([plist([1,2])])
        return self.assertEqual(logic.file_contents_to_edges(string), result)
    
class TestNetwork(unittest.TestCase):
    def test_true_network(self):
        return self.assertTrue(logic.is_same_network(1, 2, pmap({1: pset([2]), 2: pset([1, 3]),
                                                                 3: pset([2]), 4: pset([])})))
    def test_false_network(self):
        return self.assertFalse(logic.is_same_network(2, 4, pmap({1: pset([2]), 2: pset([1, 3]),
                                                                  3: pset([2]), 4: pset([])})))
if __name__ == '__main__':
    unittest.main()