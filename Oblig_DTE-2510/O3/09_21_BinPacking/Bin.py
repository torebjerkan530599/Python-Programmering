class Bin:  
    def __init__(self, maxWeight = 10):
        self.maxWeight = maxWeight
        self.totalWeight = 0
        self.objects = []
    
    def addItem(self, weight):
        if self.totalWeight + weight <= self.maxWeight:
            self.objects.append(weight)
            self.totalWeight += weight
            return True
        else:
            return False
    
    def getNumberOfObjects(self):
        return len(self.objects)
    
    def __str__(self):
        output = ""        
        for e in self.objects:
            output += str(e) + " "

        return output