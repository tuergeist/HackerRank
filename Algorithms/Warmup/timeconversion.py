#!/bin/python3

import time
timestr = input().strip()
x = time.strptime(timestr, "%I:%M:%S%p")
print(time.strftime('%H:%M:%S', x ))