# Parametere til en Lambda funksjon
# Et lambda uttrykk kan tilordnes en variabel som så kan brukes som et ordinært funksjonskall.
# Du kan bruke samme metoder for å overføre parametere til en lambda, som du bruker til en
# funksjon.
# Dette inkluderer positional arguments, keyword arguments, variabel liste av argumenter (*args) og
# variabel liste keyword arguments (**kwargs):
sumV1 = lambda a, b, c: a + b + c
sumV2 = lambda a, b, c=3: a + b + c
sumV3 = lambda *args: sum(args)
sumV4 = lambda **kwargs: sum(kwargs.values())
print(sumV1(3,2,1))
print(sumV2(1,2))
print(sumV2(3,5,10))
print(sumV3(5,5,6,7,8))
print(sumV4(k=1, l=2, m=3, n=4))


# Demo sort og key parameteren
def sort_by_second(name):
    return name[1]


names = ["Peter", "David", "John"]
names.sort(key=sort_by_second) # merk uten parantes, sender adressen til funksjonen

# Neste kodesnutt viser hvordan vi kan erstatte en funksjon (slik som den over) med et lambda uttrykk.
# Først en anonym lambda funksjon, deretter en som vi gir et navn. MERK at koden IKKE sjekker index
# out of bound, koden er laga minimalistisk for å få fram prinsippene. Kode fra eksemplene over også
# med:

names.sort(key=lambda x : x[2] )
print(names) # 3
named_lambda_func = lambda x : x[3]
names.sort(key=named_lambda_func)
print(names) # 4
names_sorted = sorted(names)
print(names_sorted) # 5
names_sorted = sorted(names, key = lambda x : x[3])
print(names_sorted) # 6

# A Python program to demonstrate packing of
# dictionary items using **
def fun(**kwargs):
 
    # kwargs is a dict
    print(type(kwargs))
 
    # Printing dictionary items
    for key in kwargs:
        print("%s = %s" % (key, kwargs[key]))
 
# Driver code
fun(name="geeks", ID="101", language="Python")


def fun(a,b,c,d,e):
    print(a,b,c,d,e)
        
dictators = {'a':'Hitler', 'b':'Putin', 'c':'Chavsjesko', 'd':'Tito', 'e':'Amin'}

fun(**dictators)

# unpacking with *args
aListOfStr = ["oranges", "apples", "bananas"]
print(aListOfStr)
print(*aListOfStr, ",")


# filter(function, iterable)
# Construct an iterator from those elements of iterable for which function is
# true. iterable may be either a sequence, a container which supports iteration,
# or an iterator. If function is None, the identity function is assumed, that is, all
# elements of iterable that are false are removed.
# Note that filter(function, iterable) is equivalent to the generator
# expression (item for item in iterable if function(item))

result = list(filter(lambda x: 'o' in x, dictators.values())) # equivalent to the generator expression (item for item in iterable if function(item))
print(result)

