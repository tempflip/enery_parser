import csv
import re

PATH  = 'parsed_spr.csv'


tbl = {}

with open(PATH) as f:
    reader = csv.reader(f, delimiter=";")
    for row in reader:
        rw = row[5] + ' / ' + row[1]
        if rw not in tbl:
            tbl[rw] = {}
        tbl[rw][row[7]] = row[8]


dts = ['2018 jan', '2018 feb', '2018 mar', '2018 apr', '2018 maj', '2018 jun', '2018 jul', '2018 aug', '2018 sep', '2018 okt', '2018 nov', '2018 dec']
print ('ADDRESS;' + ';'.join(dts))
for rw in tbl:
    print(rw, end=';')
    for dt in dts:
        num = "NO_NUM"
        if dt in tbl[rw] : num = tbl[rw][dt]
        print(num, end=';')
    print('\n', end='')