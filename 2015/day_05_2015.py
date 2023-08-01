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
    :return: True/False
    """
    vowels = "aeiou"
    vowel_counts = list(map(my_string.lower().count, vowels))
    vowel_counts = list(filter(lambda x: (x > 0), vowel_counts))  ## Only keep count of present vowels
    if (len(vowel_counts) < 3):
        rule1_check = False
    else:
        rule1_check = True
    print(f'\t{my_string}\tRule 1\t{rule1_check}\t{len(vowel_counts)}')
    return rule1_check


def check_double_letter(my_string: str):
    """
    Check that input string contains at least one letter that appears twice in a row, like xx, abcdde (dd),
    or aabbccdd (aa, bb, cc, or dd).

    :param my_string: input strung
    :return: True/False
    """
    rule2_check = False
    previous_letter = ''
    for letter in my_string:
        if letter == previous_letter:
            rule2_check = True
            break
        previous_letter = letter
    if rule2_check:
        print(f'\t{my_string}\tRule 2\t{rule2_check}\t{previous_letter + letter}')
    else:
        print(f'\t{my_string}\tRule 2\t{rule2_check}')

    return rule2_check

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
    print(f'\n{my_string}')
    rule_checks = (check_vowels(my_string),
                   check_double_letter(my_string))
    count_checks = 0
    for rule in rule_checks:
        count_checks += int(rule)
    return count_checks == 2
