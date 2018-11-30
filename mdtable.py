#!/usr/bin/env python3.6

import sys
import argparse
import codecs

def unescaped_str(arg_str):
    return codecs.decode(str(arg_str), 'unicode_escape')

def mdtable(fname, n, delim):

    bar = '|---'
    end = '|\n'

    with open(fname) as f:
        for i in range(n):
            txt = f.readline().rstrip()

            if i is 1:
                sys.stdout.write(bar * (txt.count(delim) + 1) + end)
            sys.stdout.write('|' + txt.replace(delim, '|') + end)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Print text file in Markdown table format')
    parser.add_argument('filename')
    parser.add_argument('-n', '--nrows', type=int,
                        help='number of rows to print', default=10)
    parser.add_argument('-d', '--delimiter', type=unescaped_str,
                        help='column delimiter', default=',')
    args = vars(parser.parse_args())

    mdtable(args['filename'], args['nrows'], args['delimiter'])
