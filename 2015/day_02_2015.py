"""--- Day 2: I Was Told There Would Be No Math ---

--- Part One --- 

The elves are running low on wrapping paper, and so they need to submit an order for more. They have a list of the
dimensions (length l, width w, and height h) of each present, and only want to order exactly as much a"s they need.

Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required
wrapping paper for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The
elves also need a little extra paper for each present: the area of the smallest side.

For example:

A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of
slack, for a total of 58 square feet. A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of
wrapping paper plus 1 square foot of slack, for a total of 43 square feet. All numbers in the elves' list are in
feet. 

How many total square feet of wrapping paper should they order?

--- Part Two --- 

The elves are also running low on ribbon. Ribbon is all the same width, so they only have to worry about the length 
they need to order, which they would again like to be exact.

The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of any one 
face. Each present also requires a bow made out of ribbon as well; the feet of ribbon required for the perfect bow is 
equal to the cubic feet of volume of the present. Don't ask how they tie the bow, though; they'll never tell.

For example:

A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to wrap the present plus 2*3*4 = 24 feet of 
ribbon for the bow, for a total of 34 feet. A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon to 
wrap the present plus 1*1*10 = 10 feet of ribbon for the bow, for a total of 14 feet. How many total feet of ribbon 
should they order? to order, which they would again like to be exact.

The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of any one 
face. Each present also requires a bow made out of ribbon as well; the feet of ribbon required for the perfect bow is 
equal to the cubic feet of volume of the present. Don't ask how they tie the bow, though; they'll never tell.

For example:

A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to wrap the present plus 2*3*4 = 24 feet of 
ribbon for the bow, for a total of 34 feet. A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon to 
wrap the present plus 1*1*10 = 10 feet of ribbon for the bow, for a total of 14 feet. How many total feet of ribbon 
should they order?


https://adventofcode.com/2015/day/2

"""

from util import read_list

def calc_wrapping_paper_surface(l: int, w: int, h: int):
    """
    Compute the surface of wrapping paper required for a given package.

    :param l: length of the package
    :param w: width
    :param h: height
    :return: required wrapping paper surface
    """
    surfaces = [l * w, w * h, h * l]
    extra = min(surfaces)
    total_surface = 2 * sum(surfaces) + extra
    return total_surface


def calc_one_ribbon_length(l: int, w: int, h: int):
    """
    Compute the ribbon length required for a given package.

    :param l: length of the package
    :param w: width
    :param h: height
    :return: required ribbon length
    """
    dimensions = [l, w, h]
    dimensions.sort()

    required_length = 2 * sum(dimensions[0:2]) + l * w * h

    return required_length


def calc_paper_and_ribbon(dimension_list: [str]):
    """
    Read the dimensions from an input file and compute the total required surface.

    :param dimension_list: list of strings describing package dimensions (LxWxH)
    :return: a tuple with total wrapping paper surface and ribbon length
    """
    total_surface = 0
    total_ribbon = 0
    for dimensions in dimension_list:
        l, w, h = map(int, dimensions.split("x"))
        total_surface += calc_wrapping_paper_surface(l, w, h)
        total_ribbon += calc_one_ribbon_length(l, w, h)
    return total_surface, total_ribbon


def day02():
    """
    Compute wrapping paper surface
    """
    dimensions = read_list('2015/data/data_2015_02.txt')
    total_surface, total_ribbon = calc_paper_and_ribbon(dimensions)
    print("\nDay 02 - Part One")
    print(f"\tTotal wrapping paper surface: {total_surface}")
    print("Day 02 - Part Two")
    print(f"\tTotal ribbon length: {total_ribbon}")
