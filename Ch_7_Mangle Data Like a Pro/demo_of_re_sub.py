import re

source = 'Young Frankenstein'

m = re.sub('n', '?', source)

if m:
    # You?g Fra?ke?stei?
    print(m)