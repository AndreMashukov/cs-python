import unittest
from rotated_rect_sum import rotated_rect_sum

class RotatedRectSumTest(unittest.TestCase):
  def test_rotated_rect_sum_1(self):
    matrix = [
      [1, 2, 3, 4, 0],
      [5, 6, 7, 8, 1],
      [3, 2, 4, 1, 4],
      [4, 3, 5, 1, 6]
    ]
    result = rotated_rect_sum(matrix, 2, 3)
    self.assertEqual(result, 36)

  def test_rotated_rect_sum_2(self):
    matrix = [
        [-2, 3],
        [4, 3]
      ]

    result = rotated_rect_sum(matrix, 1, 2)
    self.assertEqual(result, 7)

  def test_rotated_rect_sum_3(self):
    matrix = [
      [-2, 3, 5, -1],
      [4, 3, -10, 10]
    ]

    result = rotated_rect_sum(matrix, 1, 1)
    self.assertEqual(result, 10)

if __name__ == "__main__":
  unittest.main()