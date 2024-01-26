import urllib.request
from urllib.error import HTTPError

base_address = "https://liveexample.pearsoncmg.com/data/babynameranking"

year = input("please enter year [2001-2010]: ")

gender = input("please enter gender [m,f]: ")
if(gender != 'm' and gender != 'f'):
    print('Incorrect gender')
    exit()

name = input("please enter name: ")

try:
    data = urllib.request.urlopen(base_address+year+".txt")
except HTTPError as ex:
    print(f'The address {ex.url} is incorrect')
    print(f'may be you entered the wrong year?')
    exit()

ranking = ''
for line in data.readlines():
    ranking = line.decode().split()
    if gender == 'm':
        if name in ranking[1]:
            print(f'ranking: {ranking[0]}')
            break
    else:
         if name in ranking[3]:
            print(f'ranking: {ranking[0]}')
            break

if(ranking[1] != name and ranking[3] != name):
    print('name not found')
    exit()
    
print(f'Total description of entry: {" ".join(ranking)} ')



