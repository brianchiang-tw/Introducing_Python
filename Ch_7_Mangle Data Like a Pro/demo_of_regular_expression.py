import re

source = 'Young Frankenstein'
m = re.match('You', source)

if m:
    # you
    print( m.group() )


# -----------------------------

source = 'Young Frankenstein'
m = re.match('^You', source)

if m:
    # you
    print( m.group() )

# -----------------------------

source = 'Young Frankenstein'
m = re.match('Frank', source)

if m:
    # No mathchin
    print( m.group() )

# -----------------------------

source = 'Young Frankenstein'
m = re.search('Frank', source)

if m:
    # Frank
    print( m.group() )

# -----------------------------
source = 'Young Frankenstein'
m = re.match('.*Frank', source)

if m:
    # Young Frank
    print( m.group() )