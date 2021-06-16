"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
unique_records = set()

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    for text in texts:
        unique_records.add(text[0])
        unique_records.add(text[1])

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for call in calls:
        unique_records.add(call[0])
        unique_records.add(call[1])
print(f"There are {len(unique_records)} different telephone numbers in the records.")


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
