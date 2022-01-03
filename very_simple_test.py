import unittest

from very_simple import sum

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum(2,2), 4)

 

if __name__ == '__main__':
    unittest.main()
