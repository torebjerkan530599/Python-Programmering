class MysticNumberIterator:
    def __init__(self):
        self.n = 1
    
    
    def __iter__(self):
        self.result = 1
        return self
    
    def __next__(self):
        self.result = self.n * (3*self.n-1)/2 # exam version
        # self.result = (self.n * (self.n + 1))// 2 # liang 18.13
        self.n += 1
        return self.result
    

MSI = MysticNumberIterator()
iterator = iter(MSI)

# for i in range(1000):
#     if i%10 == 0: print()
#     print(next(iterator), end = ' ' )

# for i,n in enumerate(MSI):
#     if i%10 == 0: print()
#     if(n < 1000):
#         print(next(iterator), end = ' ' )
#     else:
#         break

for i,n in enumerate(MSI):
    if i%10 == 0: print()
    if n > 1000: 
        break 
    print(n, end = ' ') 
