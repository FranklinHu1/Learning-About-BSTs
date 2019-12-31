
#This is the master file for all of the games to work together


from tkinter import *
#from randomTrees import generateTreeList
import random
from PIL import Image, ImageTk

#This animation framework and starter code was taken from the 15-112 website and adapted
# =============================================================================
# This is the master init function for ALL the data in the game
# =============================================================================       
def insertBST(tree, value): #Taken from the 110 course website
    if (tree == []):
        tree.extend([None]*2)
    position = 1
    while (position < len(tree) and tree[position] != None):
        if (value < tree[position]):
            position = position*2
        elif (value > tree[position]):
            position = position*2 + 1
        else:
            print('ERROR:', value, 'is already in the tree!')
            return
    if (position < len(tree)):
        tree[position] = value
    else:
        tree.extend([None] * len(tree)) #remove the *2 for the length of the tree
        tree[position] = value

def generateRandomTree(change):
    tree = []
    times = random.randint(5 + change , 10 + change ) 
    valueList = []
    for i in range(times):
        number = random.randint(0,100) 
        valueList.append(number)
    random.shuffle(valueList)
    valueSet = set(valueList)
    for value in valueSet:
        insertBST(tree, value)
    return tree

def generateTreeList(change):
    tree = generateRandomTree(change)
    treeList = []
    for i in range(len(tree)):
        if tree[i] != None:
            treeList.append(tree[i])
    return [treeList, tree]


def messUpTree(tree, treeList):
    tree = tree + [] 
    while True:
        beginningValue, endingValue = random.choice(treeList), random.choice(treeList) #guarantees we get an actual value, not a none
        if beginningValue != endingValue:
            break

    treeBeginningIndex, treeEndingIndex = tree.index(beginningValue), tree.index(endingValue)
    #FInds the indices of the first and second value
    tree[treeBeginningIndex], tree[treeEndingIndex] = endingValue, beginningValue
    newTreeList = []
    for i in range(len(tree)):
        if tree[i] != None:
            newTreeList.append(tree[i])
    return [tree, newTreeList]

def init(data):
    #This is the initialized data for the entire interface
    data.mode = 'startScreen'
    #isBstGame, helpScreen, helpScreen2, buildATree
    data.gameOverMaster = None
    #This is all data for the BAT game
    data.difficultyBAT = 0
    outPut = generateTreeList(data.difficultyBAT)
    data.circleCenters = [(500,50)]
    data.branches = []
    data.labels = outPut[0]
    data.correctTree = outPut[1] 
    data.labelCenters = [(500,50)]
    data.correct = None
    data.Resetcounter = 0
    data.Checkcounter = 0
    data.score = 0 
    data.gameOverBAT = None
    data.levelsCompletedBAT = 0
    
    #This is all the data for the is BST game
    
    data.difficultyIB = 0
    outPutIB = generateTreeList(data.difficultyIB)
    data.correctTreeIB = outPutIB[1] #This is the correct tree
    data.correctLabelsIB = outPutIB[0] #This is the correct labels
    data.correctOrNotIB = random.choice(['True','False'])
    outPutWrongIB = messUpTree(data.correctTreeIB, data.correctLabelsIB)
    data.incorrectTreeIB = outPutWrongIB[0] #This is the icorrect tree
    data.incorrectLabelsIB = outPutWrongIB[1] #This is the incorrect labels
    data.circleCenterIB = []
    data.circleCenterIB.append((500,50))
    data.branchesIB = []
    data.treeIB = None
    data.treeLabelsIB = None
    if data.correctOrNotIB == 'True':
        data.treeIB = data.correctTreeIB
        data.treeLabelsIB = data.correctLabelsIB
    else:
        data.treeIB = data.incorrectTreeIB
        data.treeLabelsIB = data.incorrectLabelsIB
    data.scoreIB = 0
    data.levelsCompletedIB = 0
    data.guessCounter = 0
    data.wrongIB = None
    generateTreeData(data)

    #Data for later things
# =============================================================================
# Start Screen (STS)
# =============================================================================
def mousePressedSTS(event, data):
    pass

def keyPressedSTS(event, data):
    if event.char == '1':
        data.mode = 'buildATree'
        pass
    elif event.char == 'q':
        data.gameOverMaster == True 
    elif event.char == '3':
        data.mode = 'helpScreen'
    elif event.char == '2':
        data.mode = 'isBstGame'
    pass


def redrawAllSTS(canvas, data):
    canvas.create_rectangle(300,400,700,600, fill = 'green', width = 5)
    canvas.create_rectangle(0,0, 1000, data.height/5, fill = 'green', width = 5)
    canvas.create_text((data.width / 2)-10, data.height / 10, font = 'Arial 90 italic bold', fill = 'white', text = 
'Welcome to BST!')
    canvas.create_text(data.width/2, (data.height/10) + 80, font = 'Arial 12 italic bold', fill = 'white', text = 
'A game about Binary Search Trees, by Mark Coopershlyak and Frank Hu') 

    canvas.create_text(data.width/2, data.height/2, font = 'Arial 20 italic bold', fill = 'white', text = '''
Options:
Press 1 for Build A Tree
Press 2 for Is It A BST?
Press 3 for help
                           ''')
    pass
                          

# =============================================================================
# Is BST Game (IB)
# =============================================================================1
    
def resetIB(data):
    outPutIB = generateTreeList(data.difficultyIB)
    data.correctTreeIB = outPutIB[1] #This is the correct tree
    data.correctLabelsIB = outPutIB[0] #This is the correct labels
    data.correctOrNotIB = random.choice(['True','False'])
    outPutWrongIB = messUpTree(data.correctTreeIB, data.correctLabelsIB)
    data.incorrectTreeIB = outPutWrongIB[0] #This is the icorrect tree
    data.incorrectLabelsIB = outPutWrongIB[1] #This is the incorrect labels
    data.circleCenterIB = []
    data.circleCenterIB.append((500,50))
    data.branchesIB = []
    data.treeIB = None
    data.treeLabelsIB = None
    if data.correctOrNotIB == 'True':
        data.treeIB = data.correctTreeIB
        data.treeLabelsIB = data.correctLabelsIB
    else:
        data.treeIB = data.incorrectTreeIB
        data.treeLabelsIB = data.incorrectLabelsIB
    data.guessCounter = 0
    data.wrongIB = None
    generateTreeData(data)
        

def masterResetIB(data):
    data.difficultyIB = 0
    outPutIB = generateTreeList(data.difficultyIB)
    data.correctTreeIB = outPutIB[1] #This is the correct tree
    data.correctLabelsIB = outPutIB[0] #This is the correct labels
    data.correctOrNotIB = random.choice(['True','False'])
    outPutWrongIB = messUpTree(data.correctTreeIB, data.correctLabelsIB)
    data.incorrectTreeIB = outPutWrongIB[0] #This is the icorrect tree
    data.incorrectLabelsIB = outPutWrongIB[1] #This is the incorrect labels
    data.circleCenterIB = []
    data.circleCenterIB.append((500,50))
    data.branchesIB = []
    data.treeIB = None
    data.treeLabelsIB = None
    if data.correctOrNotIB == 'True':
        data.treeIB = data.correctTreeIB
        data.treeLabelsIB = data.correctLabelsIB
    else:
        data.treeIB = data.incorrectTreeIB
        data.treeLabelsIB = data.incorrectLabelsIB
    data.scoreIB = 0
    data.levelsCompletedIB = 0
    data.guessCounter = 0
    data.wrongIB = None
    generateTreeData(data)
    
        
def mousePressedIB(event, data):
    pass

def keyPressedIB(event, data):
    if event.char == 'r':
        if data.scoreIB > 0 and data.scoreIB % 5 == 0 and data.difficultyIB < 5:
            data.difficultyIB += 5
        resetIB(data)
    elif event.char == 'q':
        data.mode = 'startScreen'
        masterResetIB(data)
    elif event.char == 'y':
        data.guessCounter += 1
        if data.wrongIB != None:
            return None
        if data.correctOrNotIB == 'True' and data.guessCounter == 1:
            data.scoreIB += 1
            data.wrongIB = False
            data.levelsCompletedIB += 1
        elif data.correctOrNotIB == 'True' and data.guessCounter > 1:
            data.wrongIB = False
        elif data.correctOrNotIB == 'False':
            data.scoreIB -= 1
            data.wrongIB = True
    elif event.char == 'n':
        data.guessCounter += 1
        if data.wrongIB != None:
            return None
        elif data.correctOrNotIB == 'False' and data.guessCounter == 1:
            data.scoreIB += 1
            data.wrongIB = False
            data.levelsCompletedIB += 1
        elif data.correctOrNotIB == 'False' and data.guessCounter > 1:
            data.wrongIB = False
        elif data.correctOrNotIB == 'True':
            data.scoreIB -= 1
            data.wrongIB = True
        
def powerOfTwo(n): #Now recrusively calculates the exponent of base 2. If not pwr of 2, returns negative num
    #Just a quick and dirty function I made to determine if a number is a power of two, this is used when drawing the tree to make a new line
    if n == 1:
        return 0
    elif n < 1:
        return -10000000000000
    else:
        return powerOfTwo(n/2) +1
        
def generateTreeData(data): #draws the tree, right or wrong
    circleLateralDistance = 900
    for i in range(2, len(data.treeIB)):
        if powerOfTwo(i) > 0:
            rowNum = powerOfTwo(i)
            circleLateralDistance //= 2
        if data.treeIB[i] != None:
            if i % 2 == 0: #We know it's going to be the left child
                childIndex, parentIndex = i, i//2 #integer divide to avoid floats
                childValue, parentValue = data.treeIB[childIndex], data.treeIB[parentIndex]
                childLabelIndex, parentLabelIndex = data.treeLabelsIB.index(childValue), data.treeLabelsIB.index(parentValue) #Finds the index of the values in the data.labelsIB list
#                print(parentLabelIndex)
                parentCenter = data.circleCenterIB[parentLabelIndex]
                parentCenterX, parentCenterY = parentCenter[0], parentCenter[1]
                childCenterY = 100 + 50*rowNum
                childCenterX = parentCenterX - (circleLateralDistance//2)
                data.circleCenterIB.append((childCenterX, childCenterY))
                x1,y1,x2,y2 = parentCenterX, parentCenterY, childCenterX, childCenterY
                data.branchesIB.append((x1,y1,x2,y2))
            elif i % 2 != 0:
                childIndex, parentIndex = i, (i-1)//2
                childValue, parentValue = data.treeIB[childIndex], data.treeIB[parentIndex]
                childLabelIndex, parentLabelIndex = data.treeLabelsIB.index(childValue), data.treeLabelsIB.index(parentValue) #Finds the index of the values in the data.labelsIB list
                parentCenter = data.circleCenterIB[parentLabelIndex]
                parentCenterX, parentCenterY = parentCenter[0], parentCenter[1]
                childCenterY = 100 + 50*rowNum
                childCenterX = parentCenterX + (circleLateralDistance//2)
                data.circleCenterIB.append((childCenterX, childCenterY))
                x1,y1,x2,y2 = parentCenterX, parentCenterY, childCenterX, childCenterY
                data.branchesIB.append((x1,y1,x2,y2))
        else:
            pass
    

def redrawAllIB(canvas, data):
    canvas.create_rectangle(0, 800, 200, 1000, fill = 'green', width = 5)
    canvas.create_rectangle( 800, 800,1000,1000, fill = 'green', width = 5)
    canvas.create_text(100,850, font = 'Arial 12 bold',text = 'Your Score: '+str(data.scoreIB), fill = 'white')
    canvas.create_text(100,900, font = 'Arial 12 bold',text = 'Levels Completed: '+str(data.levelsCompletedIB), fill = 'white')
    canvas.create_text(900, 825, font = 'Arial 10 bold', text = 'Press y if it is a BST', fill = 'white')
    canvas.create_text(900, 875, font = 'Arial 10 bold', text = "Press n if it isn't a BST", fill = 'white' )
    canvas.create_text(900, 925, font = 'Arial 10 bold', text = 'Press r for new tree', fill = 'white')
    canvas.create_text(900,975, font = 'Arial 10 bold', text = 'Press q to quit', fill = 'white')
    for coordinates in data.branchesIB: #The lines come before the circles so that the drawing order is correct
        x1,y1,x2,y2 = coordinates[0], coordinates[1], coordinates[2], coordinates[3]
        canvas.create_line(x1,y1,x2,y2,width = 3, fill = 'black') #Hexadecimal values 2work, just Google them 
    for i in range(len(data.circleCenterIB)):
        circleCenter = data.circleCenterIB[i]
        x,y = circleCenter[0], circleCenter[1]
        r = 20
        canvas.create_oval(x-r, y-r, x+r, y+r, fill = 'green', width = 2)
        canvas.create_text(x,y, font = 'bold',text = data.treeLabelsIB[i], fill = 'white')
    if data.wrongIB == True:
        canvas.create_rectangle(50, 550, 550, 650, fill = 'green', width = 5)
        canvas.create_text(300,600, font = 'Arial 20 bold', text = 'Try another tree! Press r for a new tree', fill = 'white')
    elif data.wrongIB == False:
        canvas.create_rectangle(50, 550, 550, 650, fill = 'green', width = 5)
        canvas.create_text(300,600,font = 'Arial 20 bold', text = 'Good Job! Press r for another tree', fill = 'white')
    elif data.wrongIB == None:
        pass

    
#    canvas.create_text(300,950, text = str(data.difficultyIB))
    
    
# =============================================================================
# Help Screen (HS)
# =============================================================================
    
def mousePressedHS(event, data):
    pass
def keyPressedHS(event, data):
    if event.char == 'q':
        data.mode = 'startScreen'
    if event.char == 'n':
        data.mode = 'helpScreen2'
def redrawAllHS(canvas, data):
    canvas.create_rectangle(0, 600, 1000, 1000, fill = 'green', width = 5)
    canvas.create_rectangle((data.width/2)-150, (data.height/15) - 30, (data.width/2)+150, (data.height/15)+30, fill = 'green', width = 5)
    canvas.create_text(data.width / 2, data.height / 15, font = 'Arial 30 bold',fill = 'white', text = 'What is a BST?')
    canvas.create_text(data.width/2, (data.height/4)*3.15, font = 'Arial 12 bold', fill = 'white', text = '''
They are not real trees, and they do not produce oxygen (unfortunately).
Binary Search Trees, or BST for short, are a special kind of data structure within CS. Trees allow for the 
storage of information and makes for efficient searching when you're trying to retrieve a piece of information. 
Information is stored in the form of nodes, with the first node at the beginning (top) of the tree called the 
root of the tree. Nodes are the children of the node that they are connected to above, and they themselves are the 
parent nodes of the nodes that are connected below.

BSTs only have unique values (meaning no repeats), and they are ordered in a specific way:
    1. If the value is less than the node, it is placed to the left of the node
    2. If the value is greater than the node, it is placed to the right of the node
    3. All values connected to the left of a node must be less than that node
    4. All values connected to the right of the node must be greater than that node
The picture above is a good example of a valid binary search tree. Note that all values connected to the left of 7
(the root of the tree) are less than 7, and that all values connected to the right of 7 are greater than 7. The same
rules can be applied to each node, and it is valid for each node. 
                       ''')
    canvas.create_text(800, 975, font = 'Arial 12 bold', fill = 'white', text = 'Press n to go to the next page for game help')
    canvas.create_text(175, 975, font = 'Arial 12 bold', fill = 'white', text = 'Press q to go back to the start screen')
# =============================================================================
# Help Screen 2 (HS2)
# =============================================================================
    
def mousePressedHS2(event, data):
    pass
def keyPressedHS2(event, data):
    if event.char == 'b':
        data.mode = 'helpScreen'
    elif event.char == 'q':
        data.mode = 'startScreen'
def redrawAllHS2(canvas, data):
    canvas.create_rectangle(0, 600, 1000, 1000, fill = 'green', width = 5)
    canvas.create_rectangle(((data.width)/2)-500, ((data.height)/3)-100,((data.width)/2)+500, ((data.height/3)+100), fill = 'green', width = 5) 
    canvas.create_rectangle((data.width/2)-150, (data.height/15) - 30, (data.width/2)+150, (data.height/15)+30, fill = 'green', width = 5)
    canvas.create_text(data.width / 2, data.height / 15, font = 'Arial 30 bold',fill = 'white', text = 'The Games')
    canvas.create_text(data.width/2, data.height/3, font = 'Arial 13 bold', fill = 'white', text = '''
FOR BOTH BUILD A TREE AND IS BST:
    1. You will not get more points for repeating a level multiple time. But it is good practice!
    2. You can choose to get a new tree any time you want in Build A Tree, same with Is BST
Please keep in mind also that the difficulty will get harder as you progress, but that it caps out after a certain point. 
So, if you feel discouraged, just keep going! You will do fine! Have fun and learn something along the way too!
                       ''')
    canvas.create_text(data.width/2, (data.height/4)*3.15, font = 'Arial 12 bold', fill = 'white', text = '''
The rules are pretty straightforward for both games, and all button controls are listed in the game panels. Here are the 
objectives and controls, summarized for your convenience.

Build a Tree:

The objective of this game is to build a tree! You will be given the next number in the bottom left corner of the screen, and
your job is to click where that node should go in the tree. Once you've built the tree, you can press t to check if it's right 
or wrong. You can press z to undo your previous move, q to quit altogether, p to move on to a new tree, or r to clear the board. 
Your score is based off of the number of correct trees you make. 

Is it a BST?:

Here, the game will generate a tree for you. Your job is to determine if the tree is a valid Binary Search Tree (BST). If it is,
you simply press yes (y), and if it isn't, you press no (n). You can press r to go to a new tree, or q to quit altogether. Your score
is based off the number of correct identifications you make.
                       ''')
    canvas.create_text(800, 975, font = 'Arial 12 bold', fill = 'white', text = 'Press q to go back to the start screen')
    canvas.create_text(175, 975, font = 'Arial 12 bold', fill = 'white', text = 'Press b for explanation on BSTs')

#    canvas.create_text(data.width / 2, data.height / 2, text = 'THIS WILL BE FILLED WITH TEXT SOME DAY TOO', fill = 'white')


####################################
#Build a tree (Abbreviated as BAT)
####################################1
def reset(data): #Resets the data for BAT IN THE GAME
    a = generateTreeList(data.difficultyBAT)
    data.circleCenters = [(500,50)]
    data.branches = []
    data.labels = a[0]
    data.correctTree = a[1]
    data.labelCenters = [(500,50)]
    data.correct = None
    data.Resetcounter = 0
    data.Checkcounter = 0 #Call this function when you move on to a new tree

def masterResetBAT(data): #this function is called when you quit back to the starting screen
    data.difficultyBAT = 0
    a = generateTreeList(data.difficultyBAT)
    data.circleCenters = [(500,50)]
    data.branches = []
    data.labels = a[0]
    data.correctTree = a[1]
    data.labelCenters = [(500,50)]
    data.correct = None
    data.Resetcounter = 0
    data.Checkcounter = 0
    data.score = 0
    data.gameOverBAT = None
    data.levelsCompletedBAT = 0
    
def distanceCalc(x1,y1,x2,y2):
    return (((x2-x1)**2) + ((y2-y1)**2))**0.5

def mousePressedBAT(event, data): #This works for now
    # use event.x and event.y
    if event.x <= 200 and event.y >= 0 and event.y <= 200:
        return None #Makes sure that nothing happens if you click in the box
    if event.x >= 800 and event.y >= 0 and event.y <= 200:
        return None
    if len(data.circleCenters) == len(data.labels):
        return None #This breaks you out of the game if you've reached the end
    newCircleCenter = (event.x, event.y)
    x1,y1 = event.x, event.y #The location of the new circle
    distances = []
    for i in range(len(data.circleCenters)):
        possibleConnectingCircleCenter = data.circleCenters[i]
        x2, y2 = possibleConnectingCircleCenter[0],possibleConnectingCircleCenter[1]
        distances.append(distanceCalc(x1,y1,x2,y2))
    minimumDistance = min(distances) #Connects only to the closest circle
    connectingCircleIndex = distances.index(minimumDistance)
    connectingCircle = data.circleCenters[connectingCircleIndex]
    x2,y2 = connectingCircle[0], connectingCircle[1]
    data.branches.append((x1,x2,y1,y2))
    data.circleCenters.append(newCircleCenter) #The circle centers are the same as the label centers because the numbers go over the circles
    data.labelCenters.append(newCircleCenter)    
    
def keyPressedBAT(event, data):
    if event.char == 'z': #undo's the previous move
        if len(data.circleCenters) != 1 and len(data.labelCenters) != 1 and len(data.branches) != 0:
            data.circleCenters.pop()
            data.branches.pop()
            data.labelCenters.pop()
            data.correct = None
        else:
            pass
    elif event.char == 'p': #resets the entire board
        data.branches = []
        data.circleCenters = [data.circleCenters[0]]
        data.labelCenters = [data.labelCenters[0]]
        data.correct = None
        data.Resetcounter += 1
        data.Checkcounter = 0 
    elif event.char == 't' and len(data.circleCenters) == len(data.labels):
       #tests if the tree is correctly formatted as a BST
#        print(data.branches)
#        print(data.labelCenters)
#        print(data.labels)
#        print(data.circleCenters)
#        print(data.correctTree)
        data.Checkcounter += 1
        if data.correct != None:
            return None
        if treeCheck(data.correctTree, data.labels, data.labelCenters, data.branches) == False and data.Checkcounter == 1 and data.Resetcounter == 0:
            data.correct = False
            data.score -= 1 #Because we're cruel, you can lose infinite points
        elif treeCheck(data.correctTree, data.labels, data.labelCenters, data.branches) == True and data.Checkcounter == 1 and data.Resetcounter == 0:
#            data.Checkcounter += 1
            data.levelsCompletedBAT += 1
#            if data.Resetcounter == 0 and data.Checkcounter == 1:
            data.correct = True
            data.score += 1
        else:
            if treeCheck(data.correctTree, data.labels, data.labelCenters, data.branches) == False:
                data.correct = False
            if treeCheck(data.correctTree, data.labels, data.labelCenters, data.branches) == True:
                data.correct = True
#            elif data.Resetcounter != 0 or data.Checkcounter > 1:
#            data.correct = True
                #You only get a point if you haven't reset the board, and you only get 1 point per check
    elif event.char == 'r': #This way yo can reinitialize the tree anytime you want
        if data.score > 0 and data.score % 5 == 0 and data.difficultyBAT < 15:
            data.difficultyBAT += 5
        reset(data)
    elif event.char == 'q':
        data.gameOverBAT = True

#EDIT TO MAKE SURE THAT THE TREES ARE CORRECTLY DETERMINED AS RIGHT OR WRONG
#USE INTEGER DIVISION by 2 (//2) TO RELATE THE LABELS AND BRANCHES
def treeCheck(tree, labels, centers, branches): #labels will be data.labels, tree will be data.tree
    for i in range(2, len(tree)): #we want to skip indices 0 and 1
        if tree[i] != None: 
            if i % 2 == 0: #check if is even, if it is, we know it's the left child of a node
                childIndex, parentIndex = i, i//2
                childValue, parentValue = tree[childIndex], tree[parentIndex]
                childLabelIndex, parentLabelIndex = labels.index(childValue), labels.index(parentValue) #The indices for the labels and centers are the same because data.labels has the same length as data.
                #The .index() method works because we know all values in a BST are unique
                childCenter, parentCenter = centers[childLabelIndex], centers[parentLabelIndex]
                childCenterX, childCenterY = childCenter[0], childCenter[1]
                parentCenterX, parentCenterY = parentCenter[0], parentCenter[1]
#                print((parentCenterX, parentCenterY))
#                print((childCenterX, childCenterY))
#                childAndParentBranchesIndex = childLabelIndex//2 #Either index works, because both parent and child are stored in the same index of the branches list
#                parentChildConnection = branches[childAndParentBranchesIndex] #Finds the list of coordinats connecting the parent and child by line
#                parentBranchCenterX, parentBranchCenterY, childBranchCenterX, childBranchCenterY = parentChildConnection[1],parentChildConnection[3],parentChildConnection[0],parentChildConnection[2]
#                print((parentBranchCenterX, parentBranchCenterY))
                lineQuad = (childCenterX, parentCenterX, childCenterY, parentCenterY)               
                if lineQuad not in branches:
                    return False
                if childCenterX >= parentCenterX or childCenterY <= parentCenterY: #The child must be to the left and below of parent
                    return False
            elif i % 2 != 0: #If it's odd, then we know it's the right child of a node
                childIndex, parentIndex = i, (i-1)//2
                childValue, parentValue = tree[childIndex], tree[parentIndex]
                childLabelIndex, parentLabelIndex = labels.index(childValue), labels.index(parentValue)
                childCenter, parentCenter = centers[childLabelIndex], centers[parentLabelIndex]
                childCenterX, childCenterY = childCenter[0], childCenter[1]
                parentCenterX, parentCenterY = parentCenter[0], parentCenter[1]
#                print((parentCenterX, parentCenterY))
#                print((childCenterX, childCenterY))
#                childAndParentBranchesIndex = childLabelIndex//2
#                parentChildConnection = branches[childAndParentBranchesIndex] #Finds the list of coordinats connecting the parent and child by line
#                parentBranchCenterX, parentBranchCenterY, childBranchCenterX, childBranchCenterY = parentChildConnection[1],parentChildConnection[3],parentChildConnection[0],parentChildConnection[2]
#                print((parentBranchCenterX, parentBranchCenterY))
                lineQuad = (childCenterX, parentCenterX, childCenterY, parentCenterY)
                if lineQuad not in branches:
                    return False
                if childCenterX <= parentCenterX or childCenterY <= parentCenterY: #The child must be to the right and below of parent
                    return False
        else:
            pass
    return True

def redrawAllBAT(canvas, data): 
    canvas.create_rectangle(0, 0, 200, 200, fill = 'green', width = 5)
    canvas.create_rectangle( 800, 0,1000,200, fill = 'green', width = 5)
    canvas.create_text(900, 40, font = 'Arial 10 bold', fill = 'white', text = 'Press p to reset the board')
    canvas.create_text(900, 80, font = 'Arial 10 bold', fill = 'white', text = 'Press q to quit')
    canvas.create_text(900, 120, font = 'Arial 10 bold', fill = 'white', text = 'Press z to undo')
    canvas.create_text(900, 160, font = 'Arial 10 bold', fill = 'white', text = 'Press r to do another tree')
    for coordinates in data.branches: #The lines come before the circles so that the drawing order is correct
        x1,x2,y1,y2 = coordinates[0], coordinates[1], coordinates[2], coordinates[3]
        canvas.create_line(x1,y1,x2,y2,width = 3, fill = 'black') #Hexadecimal values work, just Google them 
    for i in range(len(data.circleCenters)):
        circleCenter = data.circleCenters[i]
        x,y = circleCenter[0], circleCenter[1]
        r = 20
        canvas.create_oval(x-r, y-r, x+r, y+r, fill = 'green', width = 2)
        canvas.create_text(x,y, font = 'bold',text = data.labels[i], fill = 'white')
    if len(data.circleCenters) == len(data.labels):
        canvas.create_text(100, 50, font = 'Arial 12 bold', text = 'Check your tree! Press t',fill='white')
    if data.correct == True:
        canvas.create_rectangle(50, 550, 550, 650, fill = 'green', width = 5)
        canvas.create_text(300,600, font = 'Arial 20 bold', text = 'Good Job! Press r for another tree!', fill = 'white')
    elif data.correct == False:
        canvas.create_rectangle(50, 550, 550, 650, fill = 'green', width = 5)
        canvas.create_text(300,600, font = 'Arial 20 bold', text ='Try Again! press p to clear the board', fill = 'white')   
    canvas.create_text(100,100, font = 'Arial 12 bold', text ='Your Score: '+ str(data.score), fill = 'white')
    if len(data.labelCenters) < len(data.labels):
        canvas.create_text(100, 50, font = 'Arial 12 bold', text = 'Next up: ' + str(data.labels[len(data.labelCenters)]), fill = 'white')#Creates a list of the numbers so you know what's next
#    canvas.create_text(300, 700, text = str(data.difficultyBAT), fill = 'white')
    canvas.create_text(100,150, font = 'Arial 12 bold', text ='Levels Completed: '+ str(data.levelsCompletedBAT), fill = 'white')


####################################
# use the run function as-is
####################################
#EDIT DATA.MODE FOR EACH OF THE SCREENS!
def run(width=300, height=300):
    
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        if data.mode == 'startScreen':
            canvas.create_image(data.width/2, data.height/2, image = treePhoto1)
            redrawAllSTS(canvas,data)
        elif data.mode == 'isBstGame':
            canvas.create_image(data.width/2, data.height/2, image = treePhoto2)
            redrawAllIB(canvas,data)
        elif data.mode == 'helpScreen':
            canvas.create_image(data.width/2, data.height/2, image = treePhoto3)
            canvas.create_image(data.width/2, data.height/3, image = BSTexample)
            redrawAllHS(canvas, data)
        elif data.mode == 'helpScreen2':
            canvas.create_image(data.width/2, data.height/2, image = treePhoto4)
            redrawAllHS2(canvas, data)
        elif data.mode == 'buildATree':
            canvas.create_image(data.width/2, data.height/2, image = treePhoto5)
            redrawAllBAT(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        if data.mode == 'startScreen':
            mousePressedSTS(event, data)
            redrawAllWrapper(canvas, data)
        elif data.mode == 'isBstGame':
            mousePressedIB(event, data)
        elif data.mode == 'helpScreen':
            mousePressedHS(event, data)
            redrawAllWrapper(canvas, data)
        elif data.mode == 'helpScreen2':
            mousePressedHS2(event, data)
            redrawAllWrapper(canvas, data)
        elif data.mode == 'buildATree':
            mousePressedBAT(event, data)
            redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        if data.mode == 'startScreen':
            keyPressedSTS(event, data)
        elif data.mode == 'isBstGame':
            keyPressedIB(event,data)
#            return None
        elif data.mode == 'helpScreen':
            keyPressedHS(event, data)
        elif data.mode == 'helpScreen2':
            keyPressedHS2(event, data)
        elif data.mode == 'buildATree':
            keyPressedBAT(event, data)
            if data.gameOverBAT == True:
                data.mode = 'startScreen'
                masterResetBAT(data)
        redrawAllWrapper(canvas, data)
    
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    init(data)

    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    image1 = Image.open('Trees.jpg')
    image2 = Image.open('Trees2.jpg')
    image3 = Image.open('Trees3.jpg')
    image4 = Image.open('Trees4.jpg')
    image5 = Image.open('Trees5.jpg')
    image6 = Image.open('BSTExample.jpg')
    treePhoto1 = ImageTk.PhotoImage(image1, master = root)
    treePhoto2 = ImageTk.PhotoImage(image2, master = root)
    treePhoto3 = ImageTk.PhotoImage(image3, master = root)
    treePhoto4 = ImageTk.PhotoImage(image4, master = root)
    treePhoto5 = ImageTk.PhotoImage(image5, master = root)
    BSTexample = ImageTk.PhotoImage(image6, master = root)
    
    redrawAllWrapper(canvas,data)
    # and launch the app

    root.mainloop()
    # blocks until window is closed
    print("bye!")

run(1000, 1000)


