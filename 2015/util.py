def read_string(infile: str):
    """
    Read the content of a text file and returns it as a string.

    :param infile: path of the input text file
    :return: string read from the input file
    """
    with open(infile) as f:
        res = f.read()
    return res


def read_list(infile: str):
    """
    Read the content of a text file and returns it as a list of strings (one string per line).

    :param infile: path of the input text file
    :return: list of strings
    """
    with open(infile) as f:
        res = f.readlines()
    return res
