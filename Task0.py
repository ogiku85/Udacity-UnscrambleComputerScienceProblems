"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    print(f"First record of texts, {texts[0][0]} texts {texts[0][1]} at time {texts[0][2]}")

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    lenghtOfData = len(calls)
    print(f"Last record of calls, {calls[lenghtOfData -1][0]} calls {calls[lenghtOfData -1][1]} at time {calls[lenghtOfData -1][2]}, lasting {calls[lenghtOfData -1][3]} seconds")


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

