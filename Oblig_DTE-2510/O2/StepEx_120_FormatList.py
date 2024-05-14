
def listToString(iList):

    if(len(iList) == 1) :
        return "The item is " + str(iList[0]) 

    for i in range(0,len(iList)-2):
        iList[i] += ", "
    
    iList.insert(len(iList)-1, " and ")
   
    string = ""
    for s in iList:
        string += s

    return "The items are " + string


def main():
    item = input("Enter an item (blank to quit): ")
    items = []
    
    while(item):
        items.append(item)
        item = input("Enter an item (blank to quit): ")
        
    print(listToString(items))

main()

