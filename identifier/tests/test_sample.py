import unittest

from src import sample

class TestSampleMethod(unittest.TestCase):

    def test_inc(self):
        self.assertEqual(sample.inc(10), 11)

if __name__ == '__main__':
    unittest.main()