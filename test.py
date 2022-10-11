import unittest
import algo

class TestAlgo(unittest.TestCase):

  def test_sort(self):
    arr = [0, -1, 6, 3, 4, -3, 1, 5, -540000]
    algo.quick_sort(arr)
    self.assertEqual(arr, [-540000, -3, -1, 0, 1, 3, 4, 5, 6])

if __name__ == '__main__':
  unittest.main()