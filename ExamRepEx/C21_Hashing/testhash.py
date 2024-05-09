import math
def highest_power_2(n):
    p = int(math.log(n,2))
    return int(pow(2,p))


HASHCODE = hash("Etternavn Fornavn")
N = highest_power_2(HASHCODE)
index = HASHCODE % N
print(index)
index = HASHCODE & (N-1)
print(index)
