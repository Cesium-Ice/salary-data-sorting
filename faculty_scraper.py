import requests
import re

URL = 'https://www.directory.ubc.ca/index.cfm?d=83I%3E%3CR%5F%2A%23O%2D6OD8%21%243%2EW2%22I5RT%2C6H%24H%3A%3C%0A'

payload = {
	'keywords': 'CASIRO OSCAR',
	'andorexactkeywords': 'start',
	'resultsperpagestaff': 10,
	'submitAnd': 'search using exact fields'
}

r = requests.post(URL, data=payload)

def return_string(a_text, jump):

	for i in range(98, 123):
	 	a_text = re.sub(r'%c' % chr(i), chr(i - jump), a_text)
			
	return a_text


matches = re.findall(r'printString\("(.*)",1\);', r.text)

for m in matches:
	print return_string(m, 1)
