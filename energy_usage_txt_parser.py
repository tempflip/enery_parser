import re

NEWLINE = 'XXX_NEW_LINE_XXX'
TITLE = 'AB Stora Tunabyggen'
PAGE_NUM = '2019-02-07Sida (\d+) av (\d+)'
ADDRESS = '.+\(.+\)'
MONTH_LINE = '(\d+)2018 ([a-z]{3})'
MONTH_LINE_2 = '(\d+)2018 ([a-z]{3})(\d+)2018 ([a-z]{3}.*)'
page_list = []

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

def parse_page(page):


    for line in page:
        if re.match(TITLE, line): 
            pass
        elif re.match(PAGE_NUM, line) : 
            print ("PAGE NUM:\t\t", re.match(PAGE_NUM, line).group(1))
            pass
        elif re.match(ADDRESS, line) : 
            print ("ADDRESS:\t\t", line)
            pass
        elif re.match(MONTH_LINE, line) : 
            match = re.match(MONTH_LINE, line)
            month = match.group(2)
            num = match.group(1)
            
            print ("MONTH_LINE:\t\t", month, num, '\t\t', line)
            pass
        else :
            print ('#NO MATCH', line)
            pass
### organizing to pages
with open("energy_usage.txt", "r") as f:
    ll = []
    for line in f:
        if re.match(NEWLINE, line):
            page_list.append(ll)
            ll = []
        else :
            ll.append(line)

### parse individual pages
# for page in page_list:
page = page_list[4]
p = pre_process(page)
parse_page(p)