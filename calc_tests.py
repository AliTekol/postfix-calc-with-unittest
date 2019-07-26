import unittest
from calc import postfix

class PostfixTestcase(unittest.TestCase):

    def test_empty(self):
        result = postfix("")
        target = 0
        self.assertEqual(target, result)

    def test_integer(self):
    
        result = postfix("42")
        target = 42
        self.assertEqual(target,result)

    def test_third(self):
        
        result = postfix("42.5")
        target = 42.5
        self.assertEqual(target, result)

    def test_fourth(self):
        
        result = postfix("4 6 +")
        target = 10
        self.assertEqual(target, result)

    def test_fifth(self):
        
        result = postfix("4 -61.5 +")
        target = -57.5
        self.assertEqual(target, result)

    def test_sixth(self):
        
        result = postfix("4.5 5 + 15.4 +")
        target = 24.9
        self.assertEqual(target, result)

    def test_seventh(self):
        
        result = postfix("4 6 + 5 + 3 -")
        target = 12
        self.assertEqual(target, result)

    def test_eighth(self):
        
        result = postfix("4 6 + 5 + 3 - 4 /")
        target = 3
        self.assertEqual(target, result)

    def test_ninth(self):
        
        result = postfix("4 6 + 5 + 3 - 4 / 1000 *")
        target = 3000
        self.assertEqual(target, result)
    
if __name__ == '__main__':
    unittest.main()