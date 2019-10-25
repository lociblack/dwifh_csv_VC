import csv
from collections import namedtuple

filename = 'data/actors.csv'

# ONE: reading rows as lists   final result: list of lists

# note how python receives each row (line) of the reader as a list
# (CONFIRMED): this is default csv / reader behavior: a line is returned
# from the reader as a list,
# with each comma-separated value being an item in the list.

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    data = [r for r in reader] # data is a list of lists

for r in data:
    print(r)

# print(data)

# x = data[0][1]
# print(x)

# TWO: dictionary version   final result: list of dictionaries

# csv.DictReader will automatically use the header row as keys, and the
# other (corresponding) rows as values for those keys. wow!

with open(filename) as fo:
    reader = csv.DictReader(fo)
    data_two = [r for r in reader]  # data_two is a list of dictionaries

# with csv.DictReader, each line is read as a dictionary, using the header
# as the keys (corresponding by row). YOU DO NOT NEED TO READ IN THE
# HEADER LINE, IT'S AUTOMATIC. We use a listcomp to build one list that
# contains each line/row of the file as a dictionary.

#print(data_two[0]['Last Name'])     # access dictionary inside list

# print data from all dictionaries via nested for loops:
count = 1
for dict in data_two:
    print('Dict {}:'.format(count))
    for key, val in dict.items():
        print('{} - {}'.format(key, val))
    count+= 1
    print()


# THREE: named tuple version    final result: list of named tuples

# allows access via dot notation, not just indexing with []

# 1st param: name of class
# 2nd param: all fields (keys) that will be used, *space separated*

# how a named tuple works, basic example:
# define the named tuple; it's a Class, so capitalize
Person = namedtuple('Person', 'name age') # this is just defining it

# create an instance
person = Person("Tom", 55) # this is feeding in the actual instance data

# print(person.name)
# print(person.age)

# now the actual example, reading a csv with namedtuple:

with open(filename) as fo:
    reader = csv.reader(fo)
    Data = namedtuple('Data', next(reader))   # interesting....

    # RUN-TIME BRAIN, MICHAEL!!
    # next(reader) evaluates to the first line of the file, in list form.
    # then the namedtuple gets created, named 'Data', with all the items from the list
    # as arguments for the keys that the named tuple will have.

    # there is no magic here. think through it in RUNTIME, watch all Evaluations.
    # next(reader) returns ['First_Name', 'Last_Name', 'Date_of_Birth']
    # so that line is then: Data = namedtuple('Data', ['First_Name', 'Last_Name', 'Date_of_Birth'])
    # those items are the arguments sent to namedtuple(), and will become the Keys for it.

    # that's why the namedtuple has keys that = the header items, and that's why it can
    # receive the *r arguments, of which there will be three.

    data = [Data(*r) for r in reader]  # listcomp to create list,
                                       # each item is a named tuple

for t in data:
    print(t.First_Name)                 # namedtuple allows dot operator access
    print(t.Last_Name)
    print(t.Date_of_Birth)

# Data(*r)  Data calls the namedtuple constructor
#           *r sends all items in that row (r) to the constructor
#           (instead of sending the item r itself, it sends each item
#           hel -inside- r. this is the same as the use of * you were
#           learning recently re: tuple unpacking. same thing!

# when * is used in an Argument, think of it is saying:
# Unpack this container and send its contents as the arguments.

# above, each row is read in by the listcomp for loop; one at a time,
# a row  (which is a list full of strings) is unpacked, to send each
# string in the list as the arguments to Data(), the named tuple
# constructor.
# so, one namedtuple object is created for each row in reader
# and the end result of the litcomp is a list containing as items
# the namedtuple objects.

# THE CONFUSING PART HERE IS USING next(reader) AS THE PARAMETER(S)
# FOR THE namedtuple constructor.
# why does next(reader) work as a parameter set that can take the
# arbitrary arguments sent to it from Data(*r) ??

# FOUR: Pandas version

import pandas as pd

data = pd.read_csv(filename).to_dict(orient="row")

print(data)































