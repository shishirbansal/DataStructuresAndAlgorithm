"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


list_of_codes = set()


calls_length = len(calls)


for i in range(calls_length):
	#if (calls[i][0].startswith('140')):
	list_of_codes.add(calls[i][0])


for i in range(calls_length):
	if( calls[i][1] in list_of_codes):
		list_of_codes.discard(calls[i][1])

text_length = len(texts)

for i in range(text_length):
	if(texts[i][0] in list_of_codes):
		list_of_codes.discard(texts[i][0])

	if(texts[i][1] in list_of_codes):
		list_of_codes.discard(texts[i][0])
		



print('These numbers could be telemarketers:')
print('\n'.join(sorted(list_of_codes)))



