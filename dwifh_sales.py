import csv
from matplotlib import pyplot as plt
from datetime import datetime

file_one = 'data/dwifh_all_sales.csv'
file_two = 'data/dwifh_bc_sales.csv'

# create code to automatically build a dictionary for each album?

with open(file_one) as fo:
    reader = csv.reader(fo)
    header = next(reader)

    album = {}
    dates, cd_income, dd_income, total_profit, artist_payout = [], [], [], [], []

    for row in reader:
        if row[2].strip() == 'Harm\'s Way':
            dates.append(float(row[0].strip()))
            cd_income.append(int(float(row[4].strip())))
            dd_income.append(int(float(row[5].strip())))
            total_profit.append(int(float(row[7].strip())))
            artist_payout.append(int(float(row[8].strip())))
        else:
            pass

album_alltime_profit = sum(total_profit)
artist_alltime_payout = sum(artist_payout)

# complete the dictionary for this album
album['title'] = 'Harm\'s Way'
album['period of sales'] = dates
album['cd_income_data'] = cd_income
album['dd_income_data'] = dd_income
album['all_time_profit'] = album_alltime_profit
album['all_time_payout'] = artist_alltime_payout

for key, value in album.items():
    print(f'{key}: {value}')

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(album['period of sales'], album['dd_income_data'], c='red')
ax.plot(album['period of sales'], album['cd_income_data'], c = 'blue')

plt.title('{} Sales - All Time'.format(album['title']))
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('CD (blue) and DD (red)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

#plt.show()

# TASK:
# 1. get the names of the albums from the .csv file and store
# them in a list. make sure there are no duplicates.

# parse the csv file and create a dictionary for each album,
# assigning it the name taken from the name list.
# use:  for album in album_list: so the process is done once
# for each album name.
# the dict created for each album contains all the data pulled
# from the csv file. create the dict, then append it to
# a list of dicts. this list will, when done, contain four
# dictionaries, one for each album.
# but since it's done in a loop, all four dicts get created
# automatically, but they contain different data, respective to
# each album.
















