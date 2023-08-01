"""
--- Day 5: Doesn't He Have Intern-Elves For This? ---
Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.

For example:

ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of
the disallowed substrings. aaa is nice because it has at least three vowels and a double letter, even though the
letters used by different rules overlap.

jchzalrnumimnmhp is naughty because it has no double letter.

haegwjzuvuyypxyu is naughty because it contains the string xy.

dvszwmarrgswjxmb is naughty because it contains only one vowel.

How many strings are nice?


"""


def check_vowels(my_string: str):
    """
    Check that my_string contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.

    :param my_string: input string
    :return: TRUE/FALSE
    """
    vowels = "aeiou"
    vowel_counts = list(map(my_string.lower().count, vowels))
    vowel_counts = list(filter(lambda x: (x > 0), vowel_counts))  ## Only keep count of present vowels
    print(f'\t{my_string}\t{vowel_counts}\t{len(vowel_counts)}')
    if (len(vowel_counts) < 3):
        rule1_check = False
    else:
        rule1_check = True
    return rule1_check


def check_rules(my_string: str):
    """
    Check the rules of a given input string.

    Rule 1: It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
    Rule 2: It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb,
    cc, or dd).
    Rule 3: It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.


    :param my_string: input string on which the rules should be checked
    :return: a tuple with the list of non-matched rule numbers
    """

    # Check rule 1
    vowel_check = check_vowels(my_string)
