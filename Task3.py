"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
from collections import OrderedDict

receiving_numbers_code = {}
percentage_of_fixed_line_calls = 0
#this variable will hold all banglore numbers which participated in outgoing calls
calling_bangalore_fixed_lines = []
#this variable will hold all banglore numbers which recieved calls from a bangalore line
receiving_bangalore_fixed_lines = []
bangalore_numbers_called_from_bangalore_lines = []
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    bangalore_area_code = '(080)'
    telemarketer_code = '140'
    mobile_prefix = ['7','8','9']

    for x in calls:
      if x[0].startswith(bangalore_area_code):
        # update array for all numbers called from bangalore
        calling_bangalore_fixed_lines.append(x[0])
        #compare the first 5 digits of the receiving number to determine it area code
        if x[1][0:5].startswith('('):
          index_closing_bracket = x[1].index(')')
          #if there's a closing barcket then get the code contained within it and store in dictionary to get unique values
          if index_closing_bracket > -1:
            current_receiving_number_prefix = x[1][0: index_closing_bracket + 1]
            receiving_numbers_code[current_receiving_number_prefix] = current_receiving_number_prefix
            if current_receiving_number_prefix == bangalore_area_code:
              receiving_bangalore_fixed_lines.append(x[1])

        elif x[1][0:5].startswith(telemarketer_code):
          current_receiving_number_prefix = telemarketer_code
          receiving_numbers_code[current_receiving_number_prefix] = current_receiving_number_prefix

        elif x[1].index(' ') > -1 and mobile_prefix.index(x[1][0]) > -1:
          current_receiving_number_prefix = x[1][0:4]
          receiving_numbers_code[current_receiving_number_prefix] = current_receiving_number_prefix

        if len(receiving_bangalore_fixed_lines) <= 0:
          percentage_of_fixed_line_calls = 0
        else:
          # len(receiving_bangalore_fixed_lines) equals all calls from and to a bangalore line
          #len(calling_bangalore_fixed_lines) equals all calls made from a bangalore line
          percentage_of_fixed_line_calls = round((len(receiving_bangalore_fixed_lines) / len(calling_bangalore_fixed_lines)* 100), 2)

print("The numbers called by people in Bangalore have codes:")
print('\n'.join(sorted(receiving_numbers_code.values())))

print(f"{percentage_of_fixed_line_calls} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")



"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
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
