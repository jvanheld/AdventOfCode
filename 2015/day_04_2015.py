"""
--- Day 4: The Ideal Stocking Stuffer ---

--- Part One ---

Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the economically
forward-thinking little girls and boys.

To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes. The input to the MD5
hash is some secret key (your puzzle input, given below) followed by a number in decimal. To mine AdventCoins,
you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.

For example:

If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes (
000001dbbfa...), and it is the lowest such number to do so. If your secret key is pqrstuv, the lowest number it
combines with to make an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks
like 000006136ef....

Your puzzle input is iwrupvqb.


--- Part Two ---
Now find one that starts with six zeroes.


"""
import hashlib


def find_suffix_number(puzzle_input: str, leading_zeros: int):
    """
    Given an input string (e.g. abcdef), find the smallest integer (in this case 609043) for which the concatenation
    (e.g. abcdef609043) produces a hexadecimal MD5 hash starting with a given number of leading zeros (ex:
    000001dbbfa3a5c83a2d506429c7b00e).

    :param puzzle_input: string with the prefix text
    :param leading_zeros: number of zeros required in the hexadecomal MD5 hash
    return: a tuple with 4 elements: puzzle input, solution suffix number, concatenated
    string, and hexadecimal hash code

    """
    number = 1  # Initialise the suffix number
    hex_hash = '1' * leading_zeros  # initialise the hex_hash
    hash_prefix = '0' * leading_zeros
    while hex_hash[0:leading_zeros] != hash_prefix:
        # while not hex_hash.startswith(hash_prefix):
        number += 1
        hex_hash = hashlib.md5(f'{puzzle_input}{number}'.encode()).hexdigest()
    return puzzle_input, number, hex_hash


def day04():
    puzzle_input = 'iwrupvqb'
    print("\nDay 04 - Part One")
    print('\t', find_suffix_number(puzzle_input, 5))
    print("Day 04 - Part Two")
    print('\t', find_suffix_number(puzzle_input, 6))
