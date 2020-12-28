import unittest
from algoritm import *


class MyTestCase(unittest.TestCase):
    def test_rabin_karp_1(self):
        self.assertEqual(algoritm("bbbshobbb", "sho", 5, 12), [(3,5)])

    def test_rabin_karp_2(self):
        self.assertEqual(algoritm("romaromeroma", "roma", 6, 13), [(0, 3),(8,11)])

    def test_rabin_karp_3(self):
        self.assertEqual(algoritm("rrrrrrrrrr", "l", 7, 14), [])

    def test_rabin_karp_4(self):
        self.assertEqual(algoritm("loooooooolsasha", "ol",8,15), [(8,9)])


if __name__ == '__main__':
    unittest.main()