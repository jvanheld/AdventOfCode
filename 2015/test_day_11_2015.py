from unittest import TestCase

from day_11_2015 import increment_password, check_password, next_password, replace_forbidden


class Test(TestCase):
    def test_increment_password(self):
        self.assertEqual("xy", increment_password("xx"))
        self.assertEqual("ya", increment_password("xz"))
        self.assertEqual("baaaa", increment_password("azzzz"))

    def test_check_password(self):
        self.assertFalse(check_password("hijklmmn"))
        self.assertFalse(check_password("abbceffg"))
        self.assertFalse(check_password("abbcegjk"))
        self.assertTrue(check_password("ghjaabcc"))
        self.assertTrue(check_password("abcdffaa"))

    def test_next_password(self):
        self.assertEqual("ghjaabcc", next_password("ghijklmn"))
        self.assertEqual("abcdffaa", next_password("abcdefgh"))

    def test_replace_forbidden(self):
        self.assertEqual("ghjaaaaa", replace_forbidden("ghijklmn"))
