import csv

filename = 'data/sitka_weather_2018_simple.csv'

with open(filename) as fo:
    reader = csv.reader(fo)
    header_row = next(reader)

    for i, v in enumerate(header_row):
        print(i, v)
    print()

    for row in reader:
        print(row[2])


