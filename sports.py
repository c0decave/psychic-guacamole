#!/usr/bin/env python3


import os
import sys
import socket
import argparse
import struct


__tool_author__ = 'dash'
__tool_name__ = 'sports.py'
__tool_version__ = 'v0.1'
__tool_desc__ = 'quick and dirty tcp portscanner'


def build_tcp_socket(host, port, args):
    '''
    setup a tcp client socket
    host - target host connect to
    port - target port connect to
    args - namespace arguments
    '''
    timeout_connect = args.timeout_connect

    try:
        # build up
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # we want blocking socket
        s.setblocking(1)

        # we want to have a timeout
        s.settimeout(timeout_connect)

        # connect to host
        s.connect((host, port))

    except socket.timeout as e:
        s.close()
        return False, e

    except socket.error as e:
        # s.close()
        # print(repr(e))
        return False, e

    except Exception as e:
        # print(repr(e))
        return False, e

    return True, s


def run(args):
    host = args.host
    start_port = args.start_port
    end_port = args.end_port

    port = start_port
    while port != end_port+1:
        ret, s = build_tcp_socket(host, port, args)
        if ret == False:
            e = s
            print(host + ':' + str(port) + ',CLOSED,' + repr(e))
            # return False
        else:
            print(host + ':' + str(port) + ',OPEN')
            s.close()
        port += 1


def main():

    parser_desc = '{0} by {1} version {2}'.format(
        __tool_name__, __tool_author__, __tool_version__)

    prog_desc = '%s' % (sys.argv[0])
    parser = argparse.ArgumentParser(prog=prog_desc, description=__tool_desc__)

    parser.add_argument("-l", "--host", action="store", default='127.0.0.1',
                        required=False, help='host to check ports', dest='host')
    parser.add_argument("-L", "--hostlist", action="store", required=False,
                        help='hostlist run checks against', dest='hostlist', default=False)
    parser.add_argument("-Ps", "--start-port", action="store", required=False, default=1, type=int,
                        help='start port (default:{0})'.format(1), dest='start_port')
    parser.add_argument("-Pe", "--end-port", action="store", required=False, default=65535, type=int,
                        help='end port (default:{0})'.format(1), dest='end_port')
    parser.add_argument("-tc", "--timeout-connect", action="store", required=False, default=5, type=int,
                        help='timeout_connect', dest='timeout_connect')
    parser.add_argument("-tr", "--timeout-read", action="store", required=False, default=5, type=int,
                        help='timeout_connect', dest='timeout_read')
    args = parser.parse_args()
    run(args)


if __name__ == "__main__":
    main()
