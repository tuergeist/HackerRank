# https://www.hackerrank.com/challenges/camelcase

import re

ins = input().strip()
print(len(re.findall('([A-Z])', ins))+1)
