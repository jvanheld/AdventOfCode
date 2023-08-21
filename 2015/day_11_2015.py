"""
--- Day 11: Corporate Policy ---

Santa's previous password expired, and he needs help choosing a new one.

To help him remember his new password after the old one expires, Santa has devised a method of coming up with a
password based on the previous one. Corporate policy dictates that passwords must be exactly eight lowercase letters
(for security reasons), so he finds his new password by incrementing his old password string repeatedly until it is
valid.


Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so on. Increase the rightmost letter one
step; if it was z, it wraps around to a, and repeat with the next letter to the left until one doesn't wrap around.

Unfortunately for Santa, a new Security-Elf recently started, and he has imposed some additional password requirements:

- Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on,
  up to xyz. They cannot skip letters; abd doesn't count.

- Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are
  therefore confusing.

- Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.

For example:

- hijklmmn meets the first requirement (because it contains the straight hij) but fails the second requirement
  requirement (because it contains i and l).

- abbceffg meets the third requirement (because it repeats bb and ff) but fails the first requirement.

- abbcegjk fails the third requirement, because it only has one double letter (bb).

- The next password after abcdefgh is abcdffaa.

- The next password after ghijklmn is ghjaabcc, because you eventually skip all the passwords that start with ghi...,
  since i is not allowed.

Given Santa's current password (your puzzle input), what should his next password be?



Your puzzle input is vzbxkghb.

--- Part Two ---
Santa's password expired again. What's the next one?
Your puzzle answer was vzcaabcc.
Your puzzle input was vzbxkghb.

"""

import os
import sys

import numpy as np
from tqdm import tqdm

from util import read_string


def increment_password(password: str):
    """
    Increment a given password.

    Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so on. Increase the rightmost letter one
    step; if it was z, it wraps around to a, and repeat with the next letter to the left until one doesn't wrap around.

    :param password: initial password
    :return: a string with the incremented password
    """
    done = False
    # password = list(password)
    ord_password = [ord(char) for char in password]
    i = - 1

    while not done:
        if ord_password[i] == 122:  # ord("z") = 122
            ord_password[i] = 97  # ord("a") = 97
            i -= 1
        else:
            ord_password[i] += 1
            done = True

    return "".join([chr(number) for number in ord_password])


def check_password(password: str):
    """
    Check if a given password complies to all the security requirements.

    - Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on,
      up to xyz. They cannot skip letters; abd doesn't count.

    - Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are
      therefore confusing.

    - Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.


    :param password: input password
    :return: a Boolean value indicating if the input password is valid or not
    """
    is_valid = True

    if len(password) != 8:
        print(f"\tInvalid password: length = {len(password)}", file=sys.stderr)
        exit("Pas déconnner ")

    # Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are
    # therefore confusing
    if any(x in password for x in ["i", "o", "l"]):
        # print(f"\t{password} contains at least one forbidden letter (i, o or l)")
        is_valid = False

    # Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on,
    # up to xyz. They cannot skip letters; abd doesn't count.
    password_ord = list(map(ord, list(password)))
    ord_diff = list(np.subtract(password_ord[1:], password_ord[:-1]))
    if not any(ord_diff[i:i + 2] == [1, 1] for i in range(len(ord_diff) - 1)):
        # print(f"\t{password} does not include increasing any straight of at least three letters")
        is_valid = False

    # Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz
    pairs = 0
    first_pair = -1
    two_pairs = False
    for i in range(len(ord_diff)):
        if ord_diff[i] == 0:
            if first_pair == -1:
                first_pair = i
            elif i - first_pair > 1:
                two_pairs = True
                # print(f"\ttwo_pairs\t{password}\t{first_pair}\t{i}")
    if not two_pairs:
        # print(f"\t{password} does not include two non-overlapping pairs of equal letters")
        is_valid = False

    return is_valid


def replace_forbidden(password: str):
    """
    Check if a password contains a forbidden letter, and if so replace it by the next letter + replace all the
    following letters by "a".

    :param password: input password
    :return: a string with the fixed password
    """
    # First replace the forbidden letters (i, l, o) by the next one
    # This gains a huge time compared to a raw loop of increment/check until they are replaced, especially if the
    # forbidden letter are at the begining of the password
    replacement = {"i": "j", "l": "m", "o": "p"}
    w = len(password)
    for a in replacement:
        if a in password:
            i = password.index(a)
            password = password[0:i] + replacement[a]
            if w - i > 1:
                password = password + "a" * (w - i - 1)
            # print(f"{password}\t{a}\ti={i}\tlen = {w}\t{password}")

    return password


def next_password(password: str):
    """
    Return the next valid password, taking into account the requirements.

    :param password: input password
    :return: a string with the next password
    """

    password = replace_forbidden(password)

    # Increment the letters until a valid password is returned
    valid = False
    with tqdm() as pbar:
        while not valid:
            password = increment_password(password)
            password = replace_forbidden(password)
            valid = check_password(password)
            pbar.update()
    return password


def day11():
    # puzzle_input = "vzbxkghb"
    puzzle_input = read_string("2015/data/data_2015_11.txt").strip()
    print("\n\nDay 11 - Part One")
    password_day1 = next_password(puzzle_input)
    print(f"Puzzle input: {puzzle_input}\nNext password : {password_day1}")

    print("\nDay 11 - Part Two")
    password_day2 = next_password(password_day1)
    print(f"Next password : {password_day2}")


if __name__ == '__main__':
    os.chdir('..')
    day11()
