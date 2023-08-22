from unittest import TestCase

from day_11_2015 import increment_password, check_password, next_password, replace_forbidden


class Test(TestCase):
    def test_increment_password(self):
        self.assertEqual([ord(char) for char in "xy"], increment_password([ord(char) for char in "xx"]))
        self.assertEqual([ord(char) for char in "ya"], increment_password([ord(char) for char in "xz"]))
        self.assertEqual([ord(char) for char in "baaaa"], increment_password([ord(char) for char in "azzzz"]))

    def test_check_password(self):
        self.assertFalse(check_password([ord(char) for char in "hijklmmn"]))
        self.assertFalse(check_password([ord(char) for char in "abbceffg"]))
        self.assertFalse(check_password([ord(char) for char in "abbcegjk"]))
        self.assertTrue(check_password([ord(char) for char in "ghjaabcc"]))
        self.assertTrue(check_password([ord(char) for char in "abcdffaa"]))

    def test_next_password(self):
        self.assertEqual("abcdffaa", next_password("abcdefgh"))
        self.assertEqual("ghjaabcc", next_password("ghijklmn"))

    def test_replace_forbidden(self):
        self.assertEqual("ghjaaaaa", replace_forbidden("ghijklmn"))
