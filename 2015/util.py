def read_string(infile):
    """
    Read the content of a text file and returns it as a string.

    :param infile: path of the input text file
    :return: string read from the input file
    """
    with open(infile) as f:
        res = f.read()
    return res
