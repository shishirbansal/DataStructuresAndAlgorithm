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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""


# we will use set data structure to remove duplicated and later we will calculate the size.





texts_length = len(texts) 


set_dataStructure =set()




for i in range(texts_length):
	set_dataStructure.add(texts[i][0])
	set_dataStructure.add(texts[i][1])


calls_length = len(calls)

for i in range(calls_length):
	set_dataStructure.add(calls[i][0])
	set_dataStructure.add(calls[i][1])

#we use set so that we can remove duplicates and later we can calculate the length


print('There are {} different telephone numbers in the records.'.format(len(set_dataStructure)))	



