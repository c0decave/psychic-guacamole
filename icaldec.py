#!/usr/bin/env python

import os
import sys
import base64
import argparse
from icalendar import Calendar, Event

__tool_name__ = 'icaldec'
__tool_author__ = 'dash'
__tool_version__ = 'v0.1'
__tool_desc__ = 'simple ical decoding' 

def run(args):

    ical = args.ical

    if ical == None:
        sys.exit(1)

    with open(ical,'rb') as fr:
        gcal = Calendar.from_ical(fr.read())
        print('Results')
        print('-'*7)
        for item in gcal.walk():
            if item.name == 'VEVENT':
                print('Summary: {0}'.format(item.get('summary')))
                print('Start: {0}'.format(item.get('dtstart').dt))
                print('End: {0}'.format(item.get('dtend').dt))
                print('URL: {0}'.format(item.get('url')))
                print('Desc: {0}'.format(item.get('description')))

def main():

    parser_desc = '{0} by {1} version {2}'.format(
        __tool_name__, __tool_author__, __tool_version__)

    prog_desc = parser_desc
    parser = argparse.ArgumentParser(
        prog=prog_desc, description=__tool_desc__)

    parser.add_argument("-f", "--file", action="store", default=None,
                        required=True, help='specify ical file', dest='ical')
#    parser.add_argument("-p", "--no-pretty", action="store_false", default=True,
#                        required=False, help='Do not print pretty', dest='nopretty')
    args = parser.parse_args()
    run(args)


if __name__ == "__main__":
    main()
