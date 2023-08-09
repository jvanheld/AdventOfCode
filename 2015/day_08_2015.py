"""
--- Day 8: Matchsticks ---

--- Part One ---

Space on the sleigh is limited this year, and so Santa will be bringing his list as a digital copy. He needs to know
how much space it will take up when stored.

It is common in many programming languages to provide a way to escape special characters in strings. For example, C,
JavaScript, Perl, Python, and even PHP handle special characters in very similar ways.

However, it is important to realize the difference between the number of characters in the code representation of the
string literal and the number of characters in the in-memory string itself.

For example:

Santa's list is a file that contains many double-quoted string literals, one on each line. The only escape sequences
used are [double-backslash] (which represents a single backslash),  [backslash double-quote] (which represents a lone
double-quote character), and [backslash x] plus two hexadecimal characters (which represents a single character with
that ASCII code).


Disregarding the whitespace in the file, what is the number of characters of code for string literals minus the
number of characters in memory for the values of the strings in total for the entire file?

For example, given the four strings above, the total number of characters of string code (2 + 5 + 10 + 6 = 23) minus
the total number of characters in memory for string values (0 + 3 + 7 + 1 = 11) is 23 - 11 = 12.

--- Part Two ---

Now, let's go the other way. In addition to finding the number of characters of code, you should now encode each code
representation as a new string and find the number of characters of the new encoded representation, including the
surrounding double quotes.

For example:

"" encodes to "\"\"", an increase from 2 characters to 6.
"abc" encodes to "\"abc\"", an increase from 5 characters to 9.
"aaa\"aaa" encodes to "\"aaa\\\"aaa\"", an increase from 10 characters to 16.
"\x27" encodes to "\"\\x27\"", an increase from 6 characters to 11.

Your task is to find the total number of characters to represent the newly encoded strings minus the number of
characters of code in each original string literal. For example, for the strings above, the total encoded length (6 +
9 + 16 + 11 = 42) minus the characters in the original code representation (23, just like in the first part of this
puzzle) is 42 - 23 = 19.



"""
import re
from util import read_list


def decode(code_string: str):
    memory_string = re.sub(r'^"', "", code_string)
    memory_string = re.sub(r'"$', "", memory_string)
    memory_string = re.sub(r'\\x[0-9a-f][0-9a-f]', '.',
                           memory_string)  # Note: I would like to replace by the corresponding character but I did not find the way. chr('\\1') or chr(r'\1') or chr(int(r'\1')) do not work here
    memory_string = re.sub(r'\\(.)', r'\1', memory_string)
    print(f'\n\t{code_string}\t{len(code_string)}',
          f'\n\t{memory_string}\t{len(memory_string)}\t')
    return memory_string


def encode(code_string: str):
    encoded_string = re.sub(r'\\', r'\\\\', code_string)
    encoded_string = re.sub('"', '\\"', encoded_string)
    encoded_string = '"' + encoded_string + '"'
    print(f'\n\t{code_string}\t{len(code_string)}',
          f'\n\t{encoded_string}\t{len(encoded_string)}\t')
    return encoded_string


def count_chars_all_strings():
    decoded_result = 0
    encoded_result = 0
    code_strings = read_list('2015/data/data_2015_08.txt')
    for code_string in code_strings:
        # Code string
        code_string = code_string.strip()
        code_chars = len(code_string)

        # Decoded string
        memory_string = decode(code_string)
        memory_chars = len(memory_string)
        decoded_result += code_chars - memory_chars

        # Encoded string
        encoded_string = encode(code_string)
        encoded_chars = len(encoded_string)
        encoded_result += encoded_chars - code_chars

        print(f'\n\t{code_string}\t{code_chars}',
              f'\n\t{memory_string}\t{memory_chars}\t'
              f'\n\t{encoded_string}\t{encoded_chars}\t')
    return decoded_result, encoded_result


def day08():
    decoded_result, encoded_result = count_chars_all_strings()
    print("\nDay 07 - Part One")
    print(f"\tResult: {decoded_result}")

    print("\nDay 07 - Part Two")
    print(f"\tResult: {encoded_result}")
