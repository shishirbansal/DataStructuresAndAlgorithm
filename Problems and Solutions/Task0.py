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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

#print('first testing texts')
#print(texts[0])
#print(texts[0][0])

texts_length = len(texts)

if texts_length >0:
	print('First record of texts, {} texts {} at time {}'.format(texts[0][0],texts[0][1],texts[0][2]))

calls_length = len(calls)

if calls_length >0:
	print('Last record of calls, {} calls {} at time {}, lasting {} seconds'.format(calls[calls_length-1][0],calls[calls_length-1][1],calls[calls_length-1][2],calls[calls_length-1][3]))


#print('First record of texts, <incoming number> texts <answering number> at time <time>'.format(texts[0]))
#print(calls[0])



