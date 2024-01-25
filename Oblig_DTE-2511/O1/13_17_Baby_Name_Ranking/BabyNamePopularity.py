import urllib.request

base_address = "https://liveexample.pearsoncmg.com/data/babynameranking"

#year = input("please enter year [2001-2010]: ")
#year = input("please enter gender: ")
#year = input("please enter name: ")

#testdata
year = "2001"
gender = 'f'
name = "Alyssa"

data = urllib.request.urlopen(base_address+year+".txt")

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
        

