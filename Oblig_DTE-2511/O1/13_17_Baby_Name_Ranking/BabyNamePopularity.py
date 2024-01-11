import urllib.request

base_address = "https://liveexample.pearsoncmg.com/data/babynameranking"

#year = input("please enter year [2001-2010]: ")
#year = input("please enter gender: ")
#year = input("please enter name: ")

#testdata
year = "2001"
gender = "girl" 
name = "Jonathan"

data = urllib.request.urlopen(base_address+year+".txt")

for line in data.readlines():
    ranking = line.decode().split()
    if name in ranking:
        print(ranking[0])
        break


# hvorfor er det viktig å vite kjønn?

