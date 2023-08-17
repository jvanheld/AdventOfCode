"""
--- Day 10: Elves Look, Elves Say ---

Today, the Elves are playing a game called look-and-say. They take turns making sequences by reading aloud the
previous sequence and using that reading as the next sequence. For example, 211 is read as "one two, two ones",
which becomes 1221 (1 2, 2 1s).

Look-and-say sequences are generated iteratively, using the previous value as input for the next step. For each step,
take the previous value, and replace each run of digits (like 111) with the number of digits (3) followed by the
digit itself (1).

For example:

- 1 becomes 11 (1 copy of digit 1).
- 11 becomes 21 (2 copies of digit 1).
- 21 becomes 1211 (one 2 followed by one 1).
- 1211 becomes 111221 (one 1, one 2, and two 1s).
- 111221 becomes 312211 (three 1s, two 2s, and one 1).

Starting with the digits in your puzzle input, apply this process 40 times. What is the length of the result?

Your puzzle answer is 252594.



--- Part Two ---

Neat, right? You might also enjoy hearing John Conway talking about this sequence (that's Conway of Conway's Game of
Life fame).

Now, starting again with the digits in your puzzle input, apply this process 50 times. What is the length of the new
result?

Your puzzle input is still 1113222113.



"""

from tqdm import tqdm


def encode_number(n_string: str):
    # print("n_string = " + n_string)
    result = ""
    char = 0
    count = 0
    for i in range(len(n_string)):
        if i == 0:
            # Initialise the current letter
            char = n_string[i]
            # print('\t\tinit')

        if n_string[i] == char:
            # Update counter of current letter
            count += 1
            # print('\t\tincrease')

        else:
            # Update result string
            result += str(count) + char
            # print('\t\tupdate')

            ## Initialize letter and counter
            char = n_string[i]
            count = 1
        # print(f'\t\ti = {i}\tnumber = {number}\tcount = {count}')
    result += str(count) + char
    # print(f'\tresult\t{result}')
    return result


def iterate_encode_number(input_string: str, times: int):
    result = input_string
    for i in tqdm(range(times)):
        result = encode_number(result)
        # print(f'\t{i}\t{len(result)}')
    return result


def day10():
    puzzle_input = "1113222113"

    print("\n\nDay 10 - Part One")
    result1 = iterate_encode_number(input_string=puzzle_input, times=40)
    print(f"\tResult length: {len(result1)}")

    print("\nDay 10 - Part Two")
    result2 = iterate_encode_number(input_string=result1, times=10)
    print(f"\tResult length: {len(result2)}")

    print("\nDay 10 - Part Two")
    result2 = iterate_encode_number(input_string=puzzle_input, times=50)
    print(f"\tResult length: {len(result2)}")
