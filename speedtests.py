'''This is a module of unit tests for the speed module'''
import speedtest as s
import unittest

class TestSequenceFunctions(unittest.TestCase):

    def test_linestructure(self):
        tester = s.speed()

        testline = "ping: 42.001 ms"
        actual = tester.extractNumbers(testline)

        self.assertEqual(42.001, actual, 'line not extracted as predicted')
        self.assertTrue(len(tester.results)==3, "Results should be a list with 3 items" )




if __name__ == '__main__':
    unittest.main()
