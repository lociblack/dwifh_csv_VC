import csv
from matplotlib import pyplot as plt
from datetime import datetime

file_one = 'data/dwifh_all_sales.csv'
file_two = 'data/dwifh_bc_sales.csv'

with open(file_one) as fo:
    reader = csv.reader(fo)
    header = next(reader)

    album_titles = []

    for row in reader:
        title = row[2].strip()
        album_titles.append(title)

    album_titles = set(album_titles)
    print(album_titles)




# fo.seek(0)  - seek can only be done on the underlying file object,
# not on the reader object.
# or: build a list from the reader object, then iterate through that
# list multiple times


# can't you just build -all- the data sets (lists) you need in one pass
# through the rows, then close the 'with open' block of code, and then set
# about building the dictionaries you want with those data lists?
