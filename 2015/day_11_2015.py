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



Your puzzle input was vzbxkghb.

Your puzzle answer was vzbxxyzz.

--- Part Two ---
Santa's password expired again. What's the next one?

Your puzzle answer was vzcaabcc.



"""

import os
import sys

from tqdm import tqdm

from util import read_string


def increment_password(ord_password: list):
    """
    Increment a given password.

    Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so on. Increase the rightmost letter one
    step; if it was z, it wraps around to a, and repeat with the next letter to the left until one doesn't wrap around.

    :param ord_password: initial password (as a list of unicode points)
    :return: incremented password (as a list of unicode points)
    """

    done = False
    i = - 1
    while not done:
        if ord_password[i] == 122:  # ord("z") = 122
            ord_password[i] = 97  # ord("a") = 97
            i -= 1
        else:
            ord_password[i] += 1
            done = True

    return ord_password


def check_password(ord_password: list):
    """
    Check if a given password complies to all the security requirements.

    - Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on,
      up to xyz. They cannot skip letters; abd doesn't count.

    - Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are
      therefore confusing.

    - Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.


    :param ord_password: input password
    :return: a Boolean value indicating if the input password is valid or not
    """
    checked = [True, False, False]
    #    checked = list

    if len(ord_password) != 8:
        print(f"\tInvalid password: length = {len(ord_password)}", file=sys.stderr)
        exit()

    # Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are
    # therefore confusing
    if any(x in ord_password for x in [105, 108, 111]):
        # print(f"\t{password} contains at least one forbidden letter (i, o or l)")
        checked[0] = False

    # Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on,
    # up to xyz. They cannot skip letters; abd doesn't count.
    for code1, code2, code3 in zip(ord_password, ord_password[1:], ord_password[2:]):
        if (code1 + 2 == code2 + 1) & (code2 + 1 == code3):
            checked[1] = True
            break

    # Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz
    pairs = 0
    skip_next = False
    for code1, code2 in zip(ord_password, ord_password[1:]):
        if code1 == code2:
            if not skip_next:
                pairs += 1
            if pairs >= 2:
                checked[2] = True
                break
            skip_next = True
        else:
            skip_next = False

    return checked[0] & checked[1] & checked[2]


def replace_forbidden(ord_password: list):
    """
    Check if a password contains a forbidden letter, and if so replace it by the next letter + replace all the
    following letters by "a".

    :param ord_password: input password
    :return: a string with the fixed password
    """
    # First replace the forbidden letters (i, l, o) by the next one
    # This gains a huge time compared to a raw loop of increment/check until they are replaced, especially if the
    # forbidden letter are at the begining of the password
    replacement = {105: 106, 108: 109, 111: 112}
    # ord_password = [replacement[ord_password[i]] if ord_password[i] in replacement
    #                else ord_password[i]
    #                for i in range(len(ord_password))]

    for char in replacement:
        if char in ord_password:
            pos = ord_password.index(char)
            ord_password[pos] = replacement[char]
            for i in range(pos + 1, len(ord_password)):
                ord_password[i] = 97

    # w = len(ord_password)
    # for a in replacement:
    #    if a in ord_password:
    #        i = ord_password.index(a)
    #        ord_password = ord_password[0:i] + replacement[a]
    #        if w - i > 1:
    #            ord_password = ord_password + "a" * (w - i - 1)
    #        # print(f"{password}\t{a}\ti={i}\tlen = {w}\t{password}")

    return ord_password


def next_password(password: str):
    """
    Return the next valid password, taking into account the requirements.

    :param password: a string with the input password
    :return: a string with the next password
    """

    # Convert string to list of unicode points
    ord_password = [ord(char) for char in password]

    # Replace forbidden characters (i, l, o) in the password
    ord_password = replace_forbidden(ord_password)

    # Convert list of unicode points to string
    password = [chr(number) for number in ord_password]

    # Increment the letters until a valid password is returned
    valid = False
    with tqdm() as pbar:
        while not valid:
            ord_password = increment_password(ord_password)

            # Replace forbidden characters (i, l, o) in the password
            ord_password = replace_forbidden(ord_password)

            valid = check_password(ord_password)
            pbar.update()

    # Convert list of unicode points to string
    password = "".join([chr(number) for number in ord_password])
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
