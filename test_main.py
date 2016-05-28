import unittest

from main import PostCode, printPostCode


class TestPostCodes(unittest.TestCase):
    first = PostCode(79, 900)
    first_smaller = PostCode(79, 899)
    first_same = PostCode(79, 900)
    second = PostCode(80, 155)

    def test_lessThan(self):
        self.assertTrue(self.first < self.second)
        self.assertTrue(self.first_smaller < self.first)
        self.assertFalse(self.first > self.second)

    def test_equal(self):
        self.assertFalse(self.first == self.second)
        self.assertTrue(self.first == self.first_same)

    def test_add(self):
        self.assertEqual(PostCode(12, 650) + PostCode(3, 800), PostCode(16, 450))

    def test_exception(self):
        self.assertRaises(SyntaxError, printPostCode, 12, 555, 10, 444)


if __name__ == '__main__':
    unittest.main()