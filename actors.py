import csv

filename = 'data/actors.csv'

# reading rows as lists
# note how python receives each row (line) of the reader as a list
# this is default csv / reader behavior: a line is returned as a list,
# with each comma-separated value being an item in the list.

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    data = [r for r in reader]

print(data)


x = data[0][1]
print(x)


# dictionary version
# csv.DictReader will automatically use the header row as keys, and the
# other (corresponding) rows as values for those keys. wow!

with open(filename) as fo:
    reader = csv.DictReader(fo)
    data_two = [r for r in reader]

print(data_two)
print(data_two[0]['Last Name'])
