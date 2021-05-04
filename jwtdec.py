#!/usr/bin/env python
# You have exactly *one* job: decode jwt token

import os
import sys
import base64
import argparse
import pprint

__tool_name__ = 'jwtdec'
__tool_author__ = 'dash'
__tool_version__ = 'v0.1'
__tool_desc__ = 'simple jwt decode'

def run(args):

    jwt = args.jwtoken

    if jwt == None:
        sys.exit(1)

    dict = {}
    splitter = jwt.split('.')
    print('Results')
    print('-'*7)

    decoded=[]
    for item in splitter:
        dec = (base64.b64decode(item+'=='))
        try:
            dec = dec.decode()
        except UnicodeDecodeError as e:
            dec = base64.b64encode(dec).decode()
        decoded.append(dec)
        print('-'*7)
        print(dec)


def main():

    parser_desc = '{0} by {1} version {2}'.format(
        __tool_name__, __tool_author__, __tool_version__)

    prog_desc = parser_desc
    parser = argparse.ArgumentParser(
        prog=prog_desc, description=__tool_desc__)

    parser.add_argument("-t", "--token", action="store", default=None,
                        required=True, help='specify jwt token to decode', dest='jwtoken')
#    parser.add_argument("-p", "--no-pretty", action="store_false", default=True,
#                        required=False, help='Do not print pretty', dest='nopretty')
    args = parser.parse_args()
    run(args)


if __name__ == "__main__":
    main()
