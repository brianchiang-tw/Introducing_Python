import re

source = 'Young Frankenstein'

m = re.split('n', source)

if m:
    # Young Frankenstein splited by n
    # ['You', 'g Fra', 'ke', 'stei', '']
    print(f"{source} splited by n")
    print(m)