"""
Created on May 21, 2017
@author: Risasi

"""
import re

"""
para = "Mesut is a player. Mesut is the best. Mesut is running Mesut Mesut Mesut"

print(re.search(r'player', para))

print(re.search(r'r....', 'rohan'))

match = re.search(r'12....', 'r1234ohan')
print(match.group())

if re.search(r'hi', 'hi, how are you?'):
    print('data found')
else:
    print('data not found')

"""

 


email_id = "morisasy@gmail.com"
pattern  = r'([\w.-]+)@([\w.-]+)'
match = re.search(pattern, email_id)
print(match.group())
uname = match.group(1)
domain = match.group(2)
print(f'Your username is {uname} and domain is {domain}')
    
      
