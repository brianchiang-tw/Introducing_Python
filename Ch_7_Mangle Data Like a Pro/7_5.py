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


# expected output:
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
print( email_template )