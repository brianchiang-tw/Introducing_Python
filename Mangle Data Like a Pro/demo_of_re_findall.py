import re

source = 'Young Frankenstein'
m = re.findall('n', source)

if m:
    # Found 4 matches
    # ['n', 'n', 'n', 'n']
    print(f'Found {len(m)} matches')
    print( m )

# ---------------------------------

source = 'Young Frankenstein'
m = re.findall('n.', source)

if m:
    # Found 3 matches
    # ['ng', 'nk', 'ns']    
    print(f'Found {len(m)} matches')
    print( m )

# ----------------------------------

source = 'Young Frankenstein'
m = re.findall('n.?', source)

if m:
    # Found 4 matches
    # ['ng', 'nk', 'ns', 'n']    
    print(f'Found {len(m)} matches')
    print( m )