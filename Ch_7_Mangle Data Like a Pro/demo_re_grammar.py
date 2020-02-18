import re

source = '''I wish I may, I wish I might 
Have a dish of fish tonight.'''

result = re.findall('wish',source)
# ['wish', 'wish']
print( result )

result = re.findall('wish|fish', source)
# ['wish', 'wish', 'fish']
print( result )

result = re.findall('^I wish', source)
# ['I wish']
print( result )

result = re.findall('fish tonight.$', source)
# ['fish tonight']
print( result )

result = re.findall('fish tonight\.$',source)
# ['fish tonight.']
print( result )

result = re.findall('[wdf]ish', source)
# ['wish', 'wish', 'dish', 'fish']
print( result )

result = re.findall('[wsh]+', source)
# ['w', 'sh', 'w', 'sh', 'h', 'sh', 'sh', 'h']
print( result )

result = re.findall('ght\W', source)
# ['ght ', 'ght.']
print( result )

result = re.findall('I (?=wish)', source )
# ['I ', 'I ']
print( result )

result = re.findall('(?<=I )wish', source )
# ['wish', 'wish']
print( result )

result = re.findall(r'\bfish\b', source)
# ['fish']
print( result )

result = re.findall(r'\bwish\b', source)
# ['wish', 'wish']
print( result )



result = re.search(r'(. dish\b).*(\bfish)', source)

# a dish of fish
print( result.group() )

# ('a dish', 'fish')
print( result.groups() )



result = re.search(r'(?P<DISH>. dish\b).*(?P<FISH>\bfish)', source)
# a dish of fish
print( result.group() )
# ('a dish', 'fish')
print( result.groups() )
# a dish
print( result.group('DISH') )
# fish
print( result.group('FISH') )