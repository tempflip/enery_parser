import csv
import re

PATH  = '/Users/tempflip/Desktop/uni/thesis_data/AB_data.csv'
ADDRESSES = 'addresses.csv'

addr_by_key = {}
with open(ADDRESSES) as f:
    reader = csv.reader(f, delimiter="\t")
    for row in reader:
        # if (row[1] in addr_by_key) : print(row[1])
        addr_by_key[row[1]] = (row[0], row[2])

# print (addr_by_key)
# exit()

ANL = "(\d+ \(anl\)).+\((m3|MWh|kWh)\)"
DATE_LINE = '\d\d\d\d \D\D\D'
NUMEX = '((\d+)(,| ))?(\d+)'

counter = 0
key = None
page_num = None
address = None
with open(PATH) as f:
    reader = csv.reader(f)
    for row in reader:
        if re.match(ANL, row[0]) :
            key = re.match(ANL, row[0]).group(1)
            metric = re.match(ANL, row[0]).group(2)
            page_num = addr_by_key[key][0]
            address = addr_by_key[key][1]
        
        if re.match(DATE_LINE, row[0]):
            if (len(row[0]) > 10) :
                date_line = row[0].split('\n')
                num_line = row[3].split('\n')
                try :
                    for j, dt in enumerate(date_line):
                        print(page_num + ';' + metric +';;' + 'EXTRA_PARSING' + ';' + address + ';' + dt + ';' + num_line[j])
                except IndexError:
                    pass
                pass
            else :
                dt = row[0].lower()
                num = 'NO_NUM'
                for i in range(1, len(row)):
                    match = re.match(NUMEX, row[i])
                    if match:
                        if match.group(2):
                            num = match.group(2) + match.group(4)
                        else:
                            num = match.group(4)
                        # num = row[i] + ' || ' + num
                        break
                
                print(page_num + ';' + metric + ';' + ';' + key + ';' + address + ';' + dt + ';' + num, end = '\n')
                
                # print(';'.join(row))
                pass
        counter+= 1
        # if (counter > 1000): exit()