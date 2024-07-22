import unittest

from src import identifier

class TestIdentifier(unittest.TestCase):

    def test_ct01(self):
        app = identifier.Identifier()
        self.assertTrue(app.validate_identifier('toja'))
    def test_ct02(self):
        app = identifier.Identifier()
        self.assertFalse(app.validate_identifier('cont123'))
    def test_ct03(self):
        app = identifier.Identifier()
        self.assertTrue(app.validate_identifier('cont1'))
    def test_ct04(self):
        app = identifier.Identifier()
        self.assertFalse(app.validate_identifier('1cont'))

if __name__ == '__main__':
    unittest.main()