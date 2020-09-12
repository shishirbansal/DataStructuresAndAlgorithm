"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

#assumption is made that only calls file will be used 


telephone_dictionary = {}


#print(calls[0])


calls_length = len(calls)

#assuming calls cannot call themselves calls[i][0] != calls[i][1]

for i in range(calls_length):
	if(calls[i][0] in telephone_dictionary.keys()):
		telephone_dictionary[calls[i][0]] += int(calls[i][3])

	if(calls[i][0] not in telephone_dictionary.keys()):
		telephone_dictionary[calls[i][0]] = int(calls[i][3])	

	if(calls[i][1] in telephone_dictionary.keys()):
		telephone_dictionary[calls[i][1]] += int(calls[i][3])

	if(calls[i][1] not in telephone_dictionary.keys()):
		telephone_dictionary[calls[i][1]] = int(calls[i][3])		 



#print(len(telephone_dictionary))


# taking list of calls values in values_list 
values_list = list(telephone_dictionary.values()) 
  
# taking list of calls keys in keys_list 
keys_list = list(telephone_dictionary.keys()) 
  
#test printing the max value  
#print(keys_list[values_list.index(max(values_list))])


#print('********')
#print(longest_teleNumber_Val)


print('{} spent the longest time, {} seconds, on the phone during September 2016.'.format(keys_list[values_list.index(max(values_list))],max(values_list)))







