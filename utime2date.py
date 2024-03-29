#!/usr/bin/env python

import os
import sys

unixt = (sys.argv[1])


from datetime import datetime
ts = int(unixt)

# if you encounter a "year is out of range" error the timestamp
# may be in milliseconds, try `ts /= 1000` in that case
print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
