    """
    created on june 17, 2019
    @author: Risasi
    
"""

import re

para = "Mesut is a player. Mesut is the best. Mesut is running Mesut Mesut Mesut"

print(re.search(r'player', para))

print(re.search(r'r....', 'rohan'))

match = re.search(r'12....', 'r1234ohan')
print(match.group())

email_id = "morisasy@gmail.com"
match = re.search(r'([\W.-]+)@([\W.-]+)', email_id)
uname = match.group(1)
domain = match.group(2)
print(f'Your username is {uname} and domain is {domain}')