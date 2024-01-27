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

col = 1 if gender == 'm' else 3 # effektivisering av søk

ranking = ''
for line in data.readlines():
    ranking = line.decode().split()
    if name in ranking[col]:
        print(f'ranking: {ranking[0]}')
        break

if(ranking[col] != name):
    print('name not found')
    exit()
else:
    print(f'Total description of entry: {" ".join(ranking)} ')



