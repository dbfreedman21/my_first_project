import unittest
from checkio.goes_right_after import goes_after

class TestGoesRightAfter(unittest.TestCase):
    def test_goes_after(self):
        self.assertTrue(goes_after("world", "w", "o"))
        self.assertFalse(goes_after("world", "w", "r"))
        self.assertFalse(goes_after("world", "l", "o"))
        self.assertTrue(goes_after("panorama", "a", "n"))
        self.assertFalse(goes_after("list", "l", "o"))
        self.assertFalse(goes_after("", "l", "o"))
        self.assertFalse(goes_after("list", "l", "l"))
        self.assertFalse(goes_after("world", "d", "w"))
        self.assertFalse(goes_after("Almaz", "a", "l"))

if __name__ == "__main__":
    unittest.main()