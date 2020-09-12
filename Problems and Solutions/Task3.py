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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""



#PARTA

calls_length = len(calls)

list_of_codes =set()

counter_partB_receiver = 0

counter_partB_caller =0

index1 = 0

index2 =0



for i in range(calls_length):
	if(calls[i][0].startswith('(080)')):
		if(calls[i][1].startswith('140')):
			list_of_codes.add(calls[i][0])

		if(' ' in calls[i][1]):
			list_of_codes.add(calls[i][1][0:4])

		if( ('(' in calls[i][1]) and (')' in calls[i][1]) ):
			index1 = calls[i][1].find('(')
			index2 = calls[i][1].find(')')+1

			list_of_codes.add(calls[i][1][index1 :index2])

			

		counter_partB_receiver +=1

	if(calls[i][0].startswith('(080)')) and (calls[i][1].startswith('(080)')):
		counter_partB_caller +=1
		

#part A 

print('The numbers called by people in Bangalore have codes:')
print("\n".join(sorted(list_of_codes)))	



#part B




result_percent = (counter_partB_caller/counter_partB_receiver)*100



print('\n{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.'.format(result_percent))




