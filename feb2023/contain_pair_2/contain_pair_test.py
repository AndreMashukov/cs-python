import unittest
from contain_pair import contain_pair

class ContainPairTest(unittest.TestCase):
  def test_contain_pair_1(self):
    a = [2, 4, 7, 5, 3, 5, 8, 5, 1, 7]
    m = 4
    k = 10

    result = contain_pair(a, m, k)
    self.assertEqual(result, 5)

  # def test_contain_pair_2(self):
  #   a = [15, 8, 8, 2, 6, 4, 1, 7]
  #   m = 2
  #   k = 8

  #   result = contain_pair(a, m, k)
  #   self.assertEqual(result, 2)

if __name__ == "__main__":
  unittest.main()