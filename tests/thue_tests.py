from unittest import TestCase

from thue import Thue


class ThueTests(TestCase):

    def test_find_repetition_at_beginning(self):
        repetition = Thue._find_repetition('ababcdefg')
        self.assertEqual(repetition, (0, 4))

    def test_find_repetition_at_middle(self):
        repetition = Thue._find_repetition('abcdcdb')
        self.assertEqual(repetition, (2, 6))

    def test_find_repetition_at_end(self):
        repetition = Thue._find_repetition('cdefgabab')
        self.assertEqual(repetition, (5, 9))

    def test_find_trivial_repetition(self):
        repetition = Thue._find_repetition('aa')
        self.assertEqual(repetition, (0, 2))

    def test_find_no_repetition(self):
        repetition = Thue._find_repetition('abcdefgh')
        self.assertIsNone(repetition)
