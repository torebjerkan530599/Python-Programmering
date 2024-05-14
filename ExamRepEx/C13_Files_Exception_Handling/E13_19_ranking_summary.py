import urllib.request
from urllib.error import HTTPError

base_address = "https://liveexample.pearsoncmg.com/data/babynameranking"

girls = []
boys = []

print('Year\tRank 1\tRank 2 Rank 3\tRank 4\tRank 5\tRank 1\tRank 2\tRank 3\tRank 4\tRank 5')
for year in range(2001,2011):
    data = urllib.request.urlopen(base_address+str(year)+".txt")
    year_string = str(year).rstrip() + ' '
    girls.append(year_string)
    for i in range(5):
        line = next(data) #using an iterator
        girls.append(line.decode().split()[3]) # girls
        boys.append(line.decode().split()[1]) # boys
    girls.extend(boys)
    print(*girls, sep='\t')
    girls.clear()
    boys.clear()
        
            



