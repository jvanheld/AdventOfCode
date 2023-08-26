"""
--- Day 12: JSAbacusFramework.io ---
Santa's Accounting-Elves need help balancing the books after a recent order. Unfortunately, their accounting software uses a peculiar storage format. That's where you come in.

They have a JSON document which contains a variety of things: arrays ([1,2,3]), objects ({"a":1, "b":2}), numbers, and strings. Your first job is to simply find all of the numbers throughout the document and add them together.

For example:

[1,2,3] and {"a":2,"b":4} both have a sum of 6.
[[[3]]] and {"a":{"b":4},"c":-1} both have a sum of 3.
{"a":[-1,1]} and [-1,{"a":1}] both have a sum of 0.
[] and {} both have a sum of 0.
You will not encounter any strings containing numbers.

What is the sum of all numbers in the document?


--- Part Two ---

Uh oh - the Accounting-Elves have realized that they double-counted everything red.

Ignore any object (and all of its children) which has any property with the value "red". Do this only for objects ({
...}), not arrays ([...]).

- [1,2,3] still has a sum of 6.
- [1,{"c":"red","b":2},3] now has a sum of 4, because the middle object is ignored.
-  {"d":"red","e":[1,2,3,4],"f":5} now has a sum of 0, because the entire structure is ignored.
[1,"red",5] has a sum of 6, because "red" in an array has no effect.

"""

import json
import os
import time
from re import findall

from util import read_list


# import sys

def collect_numbers(json_data, current_sum):
    """
    Traverse the tree parsed from the JSON file except for the branches having a "red" property, and collect the sumb
    of all the numbers.

    :param json_data: data extracted from the JSON file, describing a tree made of embedded of dictionaries and lists.
    :param current_sum: ab ubteger with the sum of all the numbers found in the tree traversal.
    :return:
    """
    if type(json_data) == dict:
        if "red" not in json_data.values():
            for item in json_data.values():
                current_sum = collect_numbers(item, current_sum)
    elif type(json_data) == list:
        for item in json_data:
            current_sum = collect_numbers(item, current_sum)
    elif type(json_data) == int:
        current_sum += json_data
    return current_sum


def day12():
    data = "".join(read_list("2015/data/data_2015_day12.json"))
    # print(data)

    print("\n\nDay 12 - Part One")
    start = time.time()
    numbers = list(map(int, findall(r'-?\d+', data)))
    print(f"\tSum of numbers\t{sum(numbers)}")
    print(f"Elapsed: {time.time() - start}")

    print("\nDay 12 - Part Two")
    start = time.time()
    json_data = json.loads(data)
    # print(json.dumps(json_data, indent=2), file=sys.stderr)
    print(f"\tSum of numbers with no red property: {collect_numbers(json_data, 0)}")
    print(f"Elapsed: {time.time() - start}")


if __name__ == '__main__':
    os.chdir('..')
    day12()
