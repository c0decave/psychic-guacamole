#!/usr/bin/env python
# You have exactly *one* job: Get me the fingerprint of the remote SSL layer.

import os
import sys
import ssl
import base64
import socket
import argparse
from M2Crypto import X509

__tool_name__ = 'fingerprint'
__tool_author__ = 'dash'
__tool_version__ = 'v0.3'
__tool_desc__ = 'get fingerprint from remote ssl layer'


def connect(host, port):

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))

    except Exception as e:
        print(repr(e))
        return False

    return s


def wrap_it(sock):

    try:
        ssock = ssl.wrap_socket(sock)
    except Exception as e:
        print(repr(e))
        return False

    return ssock


def get_pem_cert(ssock):

    try:

        cert = ssock.getpeercert(binary_form=True)
    except Exception as e:
        print(repr(e))
        return False

    return cert


def run(args):

    myfp = ['md5', 'sha1', 'sha256', 'sha512']
    host = args.host
    port = args.port

    sock = connect(host, port)
    if not sock:
        sys.exit(1)

    ssock = wrap_it(sock)

    if not ssock:
        sys.exit(1)

    pem_cert = get_pem_cert(ssock)

    if not pem_cert:
        sys.exit(1)

    x509 = X509.load_cert_string(pem_cert, X509.FORMAT_DER)

    print('Results')
    print('-'*7)
    for entry in myfp:
        fp = x509.get_fingerprint(entry)
        print(host+':' + str(port) + ',' + entry + ':' + fp)


def main():

    parser_desc = '{0} by {1} version {2}'.format(
        __tool_name__, __tool_author__, __tool_version__)

    prog_desc = parser_desc
    parser = argparse.ArgumentParser(
        prog=prog_desc, description=__tool_desc__)

    parser.add_argument("-l", "--host", action="store", default='127.0.0.1',
                        required=False, help='host to get ssl cert from, default: 127.0.0.1', dest='host')
    parser.add_argument("-p", "--port", action="store", required=False, default=443, type=int,
                        help='port (default:{0})'.format(443), dest='port')
    args = parser.parse_args()
    run(args)


if __name__ == "__main__":
    main()
