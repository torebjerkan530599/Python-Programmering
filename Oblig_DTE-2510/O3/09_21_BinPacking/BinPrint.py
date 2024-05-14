from Bin import Bin

inputWeights = input('Enter the weight of the objects: ').split(' ')
weights = [int(i) for i in inputWeights]

weights.sort(reverse=True)

print(weights)

bins = []

while(weights):
    bin = Bin()
    
    for idx, w in enumerate(weights):
        if bin.addItem(w):
                weights.pop(idx)
             
    if len(weights) == 1:
        if bin.addItem(weights[-1]):
            del weights[-1]
    
    bins.append(bin)
    
for idx, b in enumerate(bins):
    print(f'Container {idx + 1} contains objects with weight {b}') # calls __str__
    
    
