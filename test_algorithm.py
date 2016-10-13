import unittest
from algorithm import func

class TestFunc(unittest.TestCase):
  def setUp(self):
    self.array = [100, 25, 20, 30, 1, 8]

  def test_successful(self):
    self.assertTrue(func(self.array, 20, 10))

  def test_failed(self):
    self.assertFalse(func(self.array, 100, 1))

  def test_emptyArray(self):
    self.assertFalse(func([], 10, 15))

  def test_whenArrayIsNone(self):
    self.assertFalse(func([None], 10 , 90))

  def test_whentwoElementIsNegative(self):
    self.assertFalse(func(self.array, -1, -6))
  
  def test_whentwoElementIsNone(self):
    self.assertFalse(func(self.array, None, None))

  def test_whenElementIsNone(self):
    self.assertFalse(func(self.array, None, 1))



if __name__ == '__main__':
    unittest.main()
