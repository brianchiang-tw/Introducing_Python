email_template = \
'''
Dear {salutation} {name},

Thank you for your letter. We are sorry that our {product} {verbed} in your
{room}. Please note that it should never be used in a {room}, especially 
near any {animals}.

Send us your receipt and {amount} for shipping and handling. We will send
you another {product} that, in our test, is {percent}% less likely to
have {verbed}.

Thank your for your support

Sincerely,
{spokesman}
{job_title}
'''

response = \
{
    'salutation':'Colonel',
    'name':'Hackenbush',
    'product':'duck blind',
    'verbed':'imploded',
    'room':'conservatory',
    'animals':'emus',
    'amount':'$1.38',
    'percent':'1',
    'spokesman':'Edgar Schmeltz',
    'job_title':'Licensed Podiatrist'
}

print( email_template.format( **response) )