"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
texts_messages_sender_receivers ={}
incoming_calls_receivers = {}

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

    for x in texts:
        texts_messages_sender_receivers[x[0]] = x[0]
        texts_messages_sender_receivers[x[1]] = x[1]


with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    for x in calls:
        incoming_calls_receivers[x[1]] = x[1]

possible_marketers = {}

for x in calls:
    if incoming_calls_receivers.get(x[0]) == None and texts_messages_sender_receivers.get(x[0]) == None:
        possible_marketers[x[0]] = x[0]
print("These numbers could be telemarketers: ")
print(' \n'.join(sorted(possible_marketers.values())))

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

