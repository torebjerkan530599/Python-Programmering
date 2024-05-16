from Ex_11_NineTailModel import NineTailModel
from Ex_11_NineTailModel import getIndex
from Ex_11_NineTailModel import getNode
from Ex_11_NineTailModel import printNode

def main():
    # Prompt the user to enter nine coins H's and T's
    initialNode = \
        input("Enter an initial nine coin H's and T's: ").strip()

    # Create the NineTaileModel
    model = NineTailModel()
    path = model.getShortestPath(getIndex(initialNode))

    print("The steps to flip the coins are ");
    for i in range(len(path)):
        printNode(getNode(path[i]))  
        
main()