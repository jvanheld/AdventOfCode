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

--- Part Two ---

Now, take the signal you got on wire a, override wire b to that signal, and reset the other wires (including wire a).
What new signal is ultimately provided to wire a?


"""

import math

import matplotlib.pyplot as plt
import networkx as nx
from bitstring import BitArray
from tqdm import tqdm

from util import read_list


def read_network(infile):
    G = nx.DiGraph()
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
        # print(f'\t{node_id}\t{G.nodes[node_id]["info"]}')

    # Parse node info, create edges and assign signal
    for node_id in G.nodes():
        node_info = G.nodes[node_id]['info']
        instr = node_info.split(sep=' ')
        if len(instr) == 1:
            if node_info.isnumeric():
                # Wire signal
                G.nodes[node_id]['signal'] = int(node_info)
                G.nodes[node_id]['signal_bits'] = BitArray(uint=G.nodes[node_id]['signal'], length=16)

            else:
                # Node signal equals signal from a single other node
                G.add_edge(instr[0], node_id)

        elif instr[1] in ("AND", "OR"):
            G.nodes[node_id]['operator'] = instr[1]
            if instr[0].isnumeric():
                G.nodes[node_id]['input_signal'] = int(instr[0])
            else:
                G.add_edge(instr[0], node_id)
            if instr[2].isnumeric():
                G.nodes[node_id]['input_signal'] = int(instr[2])
            else:
                G.add_edge(instr[2], node_id)
        elif instr[0] == "NOT":
            G.nodes[node_id]['operator'] = instr[0]
            G.add_edge(instr[1], node_id)
        elif instr[1] in ('RSHIFT', 'LSHIFT'):
            G.add_edge(instr[0], node_id)
            G.nodes[node_id]['operator'] = instr[1]
            G.nodes[node_id]['shift'] = int(instr[2])

    return G


def init_solved_nodes(G):
    solved_nodes = set()
    unsolved_nodes = set()
    for node_id in G.nodes:
        if math.isnan(G.nodes[node_id]['signal']):
            unsolved_nodes.add(node_id)
        else:
            solved_nodes.add(node_id)
    return solved_nodes, unsolved_nodes


def shift_bits(bits: BitArray, shift: int, length=16):
    if shift > 0:
        shifted_bin = '0' * shift + bits.bin[:-shift]
    elif shift == 0:
        shifted_bin = bits.bin
    else:
        shifted_bin = bits.bin[-shift:] + '0' * -shift
    shifted = BitArray(bin=shifted_bin, length=length)
    # print(f'\t{bits}\tshift: {shift}\t{bits.uint}\t{bits.bin}\t{shifted_bin}\t{shifted.uint}')
    return shifted


def calc_signal(G):
    solved_nodes, unsolved_nodes = init_solved_nodes(G)
    iteration = 0
    max_iteration = len(unsolved_nodes) + 1
    with tqdm() as pbar:
        while len(unsolved_nodes) > 0:
            if iteration > max_iteration:
                print(f"Could not solve the graph after {iteration} iterations")
                break
            iteration += 1

            # Detect solvable nodes
            solvable_nodes = set()
            for node_id in unsolved_nodes:
                predecessors = set(G.predecessors(node_id))  # predecessor nodes in the graph
                solved_predecessors = predecessors & solved_nodes
                if (predecessors == solved_predecessors):
                    solvable_nodes.add(node_id)
            # print(f'\t\tSolvable nodes: {len(solvable_nodes)}')

            # Solve solvable nodes
            for node_id in solvable_nodes:
                node = G.nodes[node_id]
                pred = list(G.predecessors(node_id))
                # print(f'\t\t\tsolving node\t{node_id}\t{node["info"]}')

                # Right shift
                if node['operator'] == "NOT":
                    node['signal_bits'] = BitArray(uint=G.nodes[pred[0]]['signal'], length=16)
                    node['signal_bits'].invert()
                    node['signal'] = node['signal_bits'].uint

                elif node['operator'] == "RSHIFT":
                    node['signal_bits'] = shift_bits(G.nodes[pred[0]]['signal_bits'], node['shift'])
                    node['signal'] = node['signal_bits'].uint

                # Left shift
                elif node['operator'] == "LSHIFT":
                    node['signal_bits'] = shift_bits(G.nodes[pred[0]]['signal_bits'], -node['shift'])
                    node['signal'] = node['signal_bits'].uint

                # OR
                elif node['operator'] == "OR":
                    node['signal_bits'] = G.nodes[pred[0]]['signal_bits'] | G.nodes[pred[1]]['signal_bits']
                    node['signal'] = node['signal_bits'].uint

                elif node['operator'] == "AND":
                    # print(node)
                    if len(pred) == 2:
                        node['signal_bits'] = G.nodes[pred[0]]['signal_bits'] & G.nodes[pred[1]]['signal_bits']
                        node['signal'] = node['signal_bits'].uint
                    else:
                        node['signal_bits'] = G.nodes[pred[0]]['signal_bits'] & BitArray(uint=node['input_signal'],
                                                                                         length=16)
                        node['signal'] = node['signal_bits'].uint

                elif node['operator'] == "":
                    node['signal'] = G.nodes[pred[0]]['signal']
                    node['signal_bits'] = G.nodes[pred[0]]['signal_bits']

                solved_nodes.add(node_id)
                unsolved_nodes.remove(node_id)
            pbar.update()
            # print(f'\tAfter iteration: {iteration}\tSolved nodes: {len(solved_nodes)}\tUnsolved nodes: {len(unsolved_nodes)}')

    return G


def print_signals(G):
    print("Graph signal")
    for node_id in sorted(dict(G.nodes)):
        print(f"\t{node_id}\t{G.nodes[node_id]['signal']}\t{G.nodes[node_id]['info']}")

def day07():
    # Read the network from puzzle input file

    print("\nDay 07 - Part One")
    G1 = read_network('2015/data/data_2015_07.txt')

    print("Viewing the network")
    nx.draw_networkx(G1)
    plt.savefig("2015/figures/day07_wires.png", )
    #  plt.show()

    G1 = calc_signal(G1)
    # print_signals(G)
    print(f"\tSignal in node a = ", G1.nodes['a']['signal'])

    print("\nDay 07 - Part One")
    G2 = read_network('2015/data/data_2015_07.txt')
    # Override b
    G2.nodes['b']['info'] = G1.nodes['a']['signal']
    G2.nodes['b']['signal'] = G1.nodes['a']['signal']
    G2.nodes['b']['signal_bits'] = G1.nodes['a']['signal_bits']
    # Solve the signals
    G2 = calc_signal(G2)
    # print_signals(G2)
    print(f"\tSignal in node a = ", G2.nodes['a']['signal'])


if __name__ == '__main__':
    main()

