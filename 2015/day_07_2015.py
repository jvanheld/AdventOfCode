"""
--- Day 7: Some Assembly Required ---

This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately, little Bobby is a
little under the recommended age range, and he needs help assembling the circuit.

Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). A
signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal from
one source, but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs
have a signal.

The included instructions booklet describes how to connect the parts together: x AND y -> z means to connect wires x
and y to an AND gate, and then connect its output to wire z.

For example:

123 -> x means that the signal 123 is provided to wire x.
x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.

Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason, you'd like to emulate the
circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide operators for these
gates.



For example, here is a simple circuit:

123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i

After it is run, these are the signals on the wires:

d: 72
e: 507
f: 492
g: 114
h: 65412
i: 65079
x: 123
y: 456

In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to
wire a?


"""

import math

import matplotlib.pyplot as plt
import networkx as nx

from util import read_list


# import pandas
# import networkit as nk
# import matplotlib.pyplot as plt


def read_network(infile):
    G = nx.DiGraph()
    # network = dict()
    instructions = read_list(infile)

    # Create nodes
    for instruction in instructions:
        instruction = instruction.strip()
        node_info, node_id = instruction.split(' -> ')

        # Create a node in the network for the current node
        G.add_node(node_id,
                   info=node_info,
                   signal=math.nan,
                   operator='')
        print(f'\t{node_id}\t{G.nodes[node_id]["info"]}')
        # network[node_id] = dict()
        # network[node_id]['info'] = node_info

    # Parse node info, create edges and assign signal
    for node_id in G.nodes():
        node_info = G.nodes[node_id]['info']
        # print(f'\t{node}\t{info}\t{info.isnumeric()}')
        # network[node_id]['signal'] = math.nan
        instr = node_info.split(sep=' ')
        if len(instr) == 1:
            if node_info.isnumeric():
                # Wire signal
                G.nodes[node_id]['signal'] = int(node_info)
                # network[node_id]['signal'] = int(node_info)
            else:
                # Single node input
                G.add_edge(instr[0], node_id)
                # network[node_id]['input'] = instr[0]
        elif instr[1] in ("AND", "OR"):
            G.nodes[node_id]['operator'] = instr[1]
            # network[node_id]['operator'] = instr[1]
            # network[node_id]['input'] = []
            if instr[0].isnumeric():
                G.nodes[node_id]['input_signal'] = instr[0]
                # network[node_id]['input_signal'] = instr[0]
            else:
                G.add_edge(instr[0], node_id)
                # network[node_id]['input'].append(instr[0])
            if instr[2].isnumeric():
                G.nodes[node_id]['input_signal'] = instr[2]
                # network[node_id]['input_signal'] = instr[2]
            else:
                G.add_edge(instr[2], node_id)
                # network[node_id]['input'].append(instr[2])
        elif instr[0] == "NOT":
            G.nodes[node_id]['operator'] = instr[0]
            G.add_edge(instr[1], node_id)
            # network[node_id]['operator'] = instr[0]
            # network[node_id]['input'] = instr[1]
        elif instr[1] in ('RSHIFT', 'LSHIFT'):
            G.add_edge(instr[0], node_id)
            G.nodes[node_id]['operator'] = instr[1]
            G.nodes[node_id]['shift'] = instr[2]
            # network[node_id]['input'] = instr[0]
            # network[node_id]['operator'] = instr[1]
            # network[node_id]['shift'] = instr[2]

    # print(G.nodes)
    # print(G.nodes['a'])
    return G
    # return network


# def draw_network(network):
#     # Add nodes
#     G = nx.DiGraph()
#     for node in network.keys():
#         # print(f'\tadding node\t{node}')
#         G.add_node(node)
#
#     # Add edges
#     for node in network.keys():
#         # print(network[node])
#         if network[node].get('input'):
#             for innode in network[node]['input']:
#                 # print(f'Adding edge from {innode} to {node}')
#                 G.add_edge(innode, node)
#
#     # I don't knpw why this does not work
#     print("Viewing the network")
#     nx.draw_networkx(G)
#     plt.savefig("2015/figures/day07_wires.png", )
#     plt.show()
#     return(G)


def day07():
    # network = read_network('2015/data/data_2015_07.txt')
    # pprint.pprint(network)
    # G = draw_network(network)

    # Read the network from puzzle input file
    G = read_network('2015/data/data_2015_07.txt')
    print("Viewing the network")
    nx.draw_networkx(G)
    plt.savefig("2015/figures/day07_wires.png", )
    #  plt.show()


def main():
    day07()


if __name__ == '__main__':
    main()

## Play with bitstrings
from bitstring import BitArray

x = BitArray(uint=123, length=16)
y = BitArray(uint=456, length=16)
d = x & y
e = x | y
result = {'x': x.int, 'y': y.int, 'd': d.int, 'e': e.int}
print(result)
