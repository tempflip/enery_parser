import re

NEWLINE = 'XXX_NEW_LINE_XXX'
TITLE = 'AB Stora Tunabyggen'
PAGE_NUM = '2019-02-07Sida (\d+) av (\d+)'
ADDRESS = '.+\(Byggnad \)'
ADDRESS_FURTHER = '(\d+-\d+: \d+) +(.+)  \(Byggnad'
# MONTH_LINE = '(\d+)2018 ([a-z]{3})'
MONTH_LINE = '((?:\d+ )?\d+)2018 ([a-z]{3})'
MONTH_LINE_2 = '(\d+)2018 ([a-z]{3})(\d+)2018 ([a-z]{3}.*)'
TOTAL_LINE = '((?:\d+ )?\d+)Totalt'

METRIC_M3 = 'm3Period'
METRIC_MWH = 'MWh'
METRIC_KWH = 'kWhPeriod'


class ParsedPage:
    page_num = None
    address = None
    total = None
    month_map = {}
    metric = None
    adr_key = None
    month_ord = ['jan', 'feb', 'mar', 'apr', 'maj', 'jun', 'jul', 'aug', 'sep','okt', 'nov', 'dec']

    def __init__(self, page_lines):
        for line in page_lines:
            self.match_a_line(line)
    
    def match_a_line(self, line):
        if re.match(TITLE, line): 
            pass
        elif re.match(PAGE_NUM, line) : 
            self.page_num = re.match(PAGE_NUM, line).group(1)
            pass
        elif re.match(ADDRESS, line) : 
            if re.match(ADDRESS_FURTHER, line):
                match = re.match(ADDRESS_FURTHER, line)
                self.adr_key = match.group(1)
                self.address = match.group(2)
            else : 
                self.address = 'CANT PARSE : ' + line
            pass
        elif re.match(MONTH_LINE, line) : 
            match = re.match(MONTH_LINE, line)
            month = match.group(2)
            num = match.group(1)
            self.month_map[month] = num
            pass
        elif re.match(TOTAL_LINE, line) : 
            match = re.match(TOTAL_LINE, line)
            self.total = match.group(1)
            pass
        # elif re.match(METRIC_M3, line) : 
            # self.metric = 'm3'
        elif re.match(METRIC_KWH, line) : 
            self.metric = 'kwh'
            # print ("## METRIC\t\t kwh")
        # elif re.match(METRIC_MWH, line) : 
            # self.metric = 'mwh'
            # print ("## METRIC\t\t mwh")
        else :
            # print ('#NO MATCH', line)
            pass

    
    def print(self):
        print('PAGE NUM\t\t', self.page_num)

        if self.metric != 'kwh':
            print ('PAGE CONTAINS NO kwh data')
            return

        print('ADDRESS KEY\t\t', self.adr_key)
        print('ADDRESS\t\t', self.address)
        print('TOTAL\t\t', self.total)
        print('METRIC\t\t', self.metric)
        # print('month_map\t\t', self.month_map)
        for month_key in self.month_ord:
            if month_key not in self.month_map : continue
            print(month_key, '\t\t', self.month_map[month_key])

def pre_process(page):
    pp = page
    # pre-process for splitting bad month lines the lines like this:
    st_to_do = True
    while st_to_do:
        st_to_do = False
        p = []
        for line in pp:
            if re.match(MONTH_LINE_2, line) : 
                match = re.match(MONTH_LINE_2, line)
                l1 = match.group(1) + '2018' + ' ' + match.group(2) + '\n'
                l2 = match.group(3) + '2018' + ' ' + match.group(4) + '\n'
                p.append(l1)
                p.append(l2)
                st_to_do = True
                # print ('###' ,line, l1, l2)
            else :
                p.append(line)
        pp = p
    return p


### organizing to pages
page_list = []
with open("energy_usage.txt", "r") as f:
    ll = []
    for line in f:
        if re.match(NEWLINE, line):
            page_list.append(ll)
            ll = []
        else :
            ll.append(line)

### parse individual pages
for page in page_list[0:100]:
    p = ParsedPage(page)
    p.print()
    print ("...........................................")
