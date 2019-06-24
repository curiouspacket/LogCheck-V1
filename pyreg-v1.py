#!/usr/bin/python3.6

import re

pattern = '((172)\.)((16)\.)((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.)(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9])'
#[1-9]{2,3}\.[1-9]{2,3}'
test_string = input('What would you like to match ? ')
result = re.match(pattern, test_string)



if result:
    print('Search Succesful.')
    print(result)
else:
    print('Search unsuccessful.')
    print(result)
    




