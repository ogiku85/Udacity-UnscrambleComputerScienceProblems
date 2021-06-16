"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
telephone_number_with_max_time = ""
numbers_and_time_spent_dict = {}
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    max_time = 0
    for call in calls:
        if call[0] in numbers_and_time_spent_dict:
            numbers_and_time_spent_dict[call[0]] += int(call[3])
        else:
           numbers_and_time_spent_dict[call[0]] = int(call[3]) 
        if call[1] in numbers_and_time_spent_dict:
            numbers_and_time_spent_dict[call[1]] += int(call[3])
        else:
           numbers_and_time_spent_dict[call[1]] = int(call[3]) 

# the phone number with the hightest total time
telephone_number_with_max_time = max(numbers_and_time_spent_dict, key = lambda k: numbers_and_time_spent_dict[k])
max_time = numbers_and_time_spent_dict[telephone_number_with_max_time]
print(f"{telephone_number_with_max_time} spent the longest time, {max_time} seconds, on the phone during September 2016.")
    

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

