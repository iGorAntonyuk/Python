
import random

def main():
    
    menuSelection = 0
    menuSelection = displayMenu(menuSelection)
    writeToFile(menuSelection)
    compare(menuSelection)
    
def displayMenu(menuSelection):
        
    menuSelection = input('Select medium for sound travel. 1. Air  2. Water  3. Steel ')
    while menuSelection < 1 or menuSelection > 3:
        print('Invalid selection. Enter 1,2, or 3 ')
        menuSelection = input('Select medium for sound travel. 1. Air  2. Water  3. Steel ')
    return menuSelection

def writeToFile(menuSelection):
    outFile = open('selection.txt', 'a')
    print >> outFile, 'User Input'
    
    outFile.write(str(menuSelection) + '\n')
    outFile.close()
    inFile = open('selection.txt', 'r')
    str1 = inFile.read()
    print str1

def compare(menuSelection):
    pnumber = random.randint(1,6)
    if pnumber > menuSelection:
        print 'Random Number is greater'
    elif pnumber < menuSelection:
            print 'Random Number is less'
    else: print 'Random Numbe is equal'
    print ('Random Number is '), + pnumber
                 
    
main()
