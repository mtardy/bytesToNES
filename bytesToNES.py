#!/usr/local/bin/python3

import sys
import argparse

parser = argparse.ArgumentParser(description="Converts bytes to NES controller strings, see '-d' for information on the format.")
parser.add_argument("-d", "--doc", help="display documentation on the NES controller string format and exit", action='store_true')
parser.add_argument('-f', "--format", help="change the format of output", choices=['bk2', 'fm2'])
parser.add_argument("-v", "--verbose", help="verbose human readable output, line is red if the controller combinaison is impossible a priori", action='store_true')
parser.add_argument("-b", "--byte", help="input one byte to convert")
args = parser.parse_args()

if (args.doc):
    print("Mapping of the NES controller:")
    print("7 - A\n6 - B\n5 - Select (s)\n4 - Start (S)\n3 - Up\n2 - Down\n1 - Left\n0 - Right\n")
    indicators = "ABsSUDLR"
    index = "76543210"
    separator = "|"
    print("---------------")
    print(separator.join(index))
    print(separator.join(indicators))
    print("---------------")
    exit(0)

def formatter(internal: dict[str, bool], fmt: str) -> str:
    out = ""
    if (fmt == "fm2"):
        template = "|0|$|........||"
        order = "RLDUTsBA"
        sep = '.'
    elif (fmt == "bk2"):
        template = "|..|$|........|"
        order = "UDLRSsBA"
        sep = '.'
    else:
        template = "$"
        order = "ABsSUDLR"
        sep = '-'
    for o in order:
        out += o if internal[o if o != 'T' else 'S'] else sep
    return template.replace('$', out)

def toIntern(byte: int) -> dict[str, bool]:
    inputs_str = format(byte, '08b')
    indicators = "ABsSUDLR"
    dic = {}
    for i, c in enumerate(inputs_str):
        dic[indicators[i]] = True if c == "1" else False
    return dic

def impossible(s: dict[str, bool]) -> bool:
    return (s['U'] and s['D']) or (s['L'] and s['R'])

def display(data: bytes, fmt: str):
    for b in data:
        s = toIntern(b)
        if (args.verbose):
            print(('\033[31m' if impossible(s) else '\033[0m') + "0x{:02x}: ".format(b) + formatter(s, fmt))
        else:
            print(formatter(s, fmt))

if (args.byte != None):
    byte = int(args.byte, 0)
    if (byte < 0 or byte > 255):
        print("Error: must be an uint8, between 0 and 255")
        exit(2)
    display(bytes([byte]), args.format)
else:
    data = sys.stdin.buffer.read()
    display(data, args.format)
