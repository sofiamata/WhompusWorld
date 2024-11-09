#!/usr/bin/python3
import random

class Node:
    def __init__(self, nodeNumber, row, column, f, g, h, breeze, stench, pit, whompus, gold, facingDirection, permanentWhompus, permanentPit):
        self.nodeNumber = nodeNumber
        self.row = row
        self.column = column
        self.f = f
        self.g = g
        self.h = h
        self.breeze = breeze      # 0 = no  1 = yes
        self.stench = stench      # 0 = no  1 = yes 
        self.pit = pit            # 0 = no  1 = maybe  2 = yes
        self.whompus = whompus    # 0 = no  1 = maybe  2 = yes
        self.gold = gold          # 0 = no  1 = yes
        self.facingDirection = facingDirection  # 0 = no direction   1 = north   2 = west   3 = south   4 = east
        self.permanentWhompus = permanentWhompus # 0 = no  1 = yes
        self.permanentPit = permanentPit         # 0 = no  1 = yes

    def setNodeNUmber(self,nodeNumber):
        self.nodeNumber = nodeNumber

    def setF(self, num):
        self.f = num

    def setG(self,num):
        self.g = num

    def setH(self, num):
        self.h = num

    def setBreeze(self, b):
        self.breeze = b

    def setStench(self, s):
        self.stench = s

    def setPit(self,p):
        self.pit = p
    
    def setWhompus(self, w):
        self.whompus = w

    def setGold(self, g):
        self.gold = g
    
    def setFacingDirection(self, direction):
          self.facingDirection = direction

    def setPermanentWhompus(self, w):
        self.permanentWhompus = w
    
    def setPermanentPit(self, p):
        self.permanentPit = p

    def getRow(self):
        return self.row
    
    def getColumn(self):
        return self.column
    
    def getNodeNUmber(self):
        return self.nodeNumber

    def getF(self):
        return self.f

    def getG(self):
        return self.g

    def getH(self):
        return self.h

    def getBreeze(self):
        return self.breeze

    def getStench(self):
        return self.stench

    def getPit(self):
        return self.pit
    
    def getWhompus(self):
        return self.whompus

    def getGold(self):
        return self.gold   

    def getFacingDirection(self):
          return self.facingDirection
    
    def getPermanentWhompus(self):
        return self.permanentWhompus
    
    def getPermanentPit(self):
        return self.permanentPit

class PotentialNeighbors:
    def __init__(self, x, y, facing):
        self.x = x
        self.y = y
        self.facing = facing

    def getFacingDirection(self):
          return self.facing
    
    def setFacingDirection(self, direction):
          self.facing = direction

class minHeap:
	def __init__(self, capacity):
		self.storage = [0] * capacity
		self.capacity = capacity
		self.size = 0
		
	def getParentIndex(self, index):
		return (index -1)//2
	
	def getLeftChildIndex(self,index):
		return 2*index+1
	
	def getRighttChildIndex(self,index):
		return 2*index+2
	
	def hasParent(self,index):
		return self.getParentIndex(index) >= 0
	
	def hasLeftChild(self,index):
		return self.getLeftChildIndex(index) < self.size
	
	def hasRightChild(self,index):
		return self.getRighttChildIndex(index) < self.size
	
	def parent(self,index):
		return self.storage[self.getParentIndex(index)]
	
	def leftChild(self,index):
		return self.storage[self.getLeftChildIndex(index)]
	
	def rightChild(self,index):
		return self.storage[self.getRighttChildIndex(index)]
	
	def isFull(self):
		return self.size == self.capacity
	
	def swap(self,index1,index2):
		temp = self.storage[index1]
		self.storage[index1] = self.storage[index2]
		self.storage[index2] = temp
		
	def insert(self, data):
		if(self.isFull()):
			raise("Heap is full!")
		self.storage[self.size] = data
		self.size += 1
		self.heap(self.size-1)
		self.heapDown(0)
		
	def heap(self,index):
		if(self.hasParent(index) and self.parent(index).f > self.storage[index].f ): #compare f cost
			self.swap(self.getParentIndex(index),index)
			index = self.getParentIndex(index)
			
	def removeMin(self):
		if(self.size == 0):
			raise("Empty Heap")
		data = self.storage[0]
		self.storage[0] = self.storage[self.size - 1]
		self.size -= 1
		self.heapDown(0)
		return data
		
	def heapDown(self,index):
		smallest = index
		if (self.hasLeftChild(index) and self.storage[smallest].f > self.leftChild(index).f):
			smallest = self.getLeftChildIndex(index)
		if (self.hasRightChild(index) and self.storage[smallest].f > self.rightChild(index).f):
			smallest = self.getRighttChildIndex(index)
		if (smallest != index):
			self.swap(index,smallest)
			self.heapDown(smallest)
		
	def contains(self, node):
		flag = False
		for i in range(self.size):
			if self.storage[i].row == node.row and self.storage[i].column == node.column and self.storage[i].nodeNumber == node.nodeNumber:
				flag = True
		return flag
	
	def printHeap(self):
		for i in range(self.size):
			print("node: " + str(self.storage[i].nodeNumber) + "  row: " + str(self.storage[i].row) + "  col: " + str(self.storage[i].column) + "  f: " + str(self.storage[i].f) + " i: " + str(i)) # 

def randomPlacements(section, array, rows, columns):
    #section: 1 = pits 2 = breeze 3 = stench and whompus
    randomNum1 = random.randint(0, (rows-1))
    randomNum2 = random.randint(0, (columns-1))
    
    if (section == 1):
        # handles preventing start to be a pit, or an existing whompus or  pit
        while((array[randomNum1][randomNum2].getNodeNUmber()) == ((rows * columns) - (columns - 1)) or (array[randomNum1][randomNum2].getPermanentWhompus() == 1) or (array[randomNum1][randomNum2].getPermanentPit() == 1)):
            randomNum1 = random.randint(0, (rows-1))
            randomNum2 = random.randint(0, (columns-1))
            
        array[randomNum1][randomNum2].setPermanentPit(1)

        # setting breeze around the pit
        try:
            # check if column left
            if(randomNum2 - 1) > -1: # -1 or less then is out of bound
                array[randomNum1][randomNum2 - 1].setBreeze(1)
                 
            # check if column right
            if (randomNum2 + 1) < columns: # 4 or greater is out of bound
                array[randomNum1][randomNum2 + 1].setBreeze(1)

            # check if there are rows above
            if (randomNum1 - 1) > -1 : # -1 or less then is out of bound
                array[randomNum1 - 1][randomNum2].setBreeze(1)
            
            # check if there are rows below
            if (randomNum1 + 1) < rows : # 4 or greater then is out of bound
                array[randomNum1 + 1][randomNum2].setBreeze(1)
                
        except IndexError:
            print("** index error **")

    elif (section == 2):
        # handles preventing start or pit to have whompus
        while((array[randomNum1][randomNum2].getNodeNUmber()) == ((rows * columns) - (columns - 1)) or (array[randomNum1][randomNum2].getPermanentPit() == 1)):
            randomNum1 = random.randint(0, (rows-1))
            randomNum2 = random.randint(0, (columns-1))

        # setting whompus
        array[randomNum1][randomNum2].setPermanentWhompus(1)
         
        try:
            # check if column left
            if(randomNum2 - 1) > -1: # -1 or less then is out of bound
                array[randomNum1][randomNum2 - 1].setStench(1)
            # check if column right
            if (randomNum2 + 1) < columns: # 4 or greater is out of bound
                array[randomNum1][randomNum2 + 1].setStench(1)

            # check if there are rows above
            if (randomNum1 - 1) > -1 : # -1 or less then is out of bound
                array[randomNum1 - 1][randomNum2].setStench(1)
                
            # check if there are rows below
            if (randomNum1 + 1) < rows : # 4 or greater then is out of bound
                array[randomNum1 + 1][randomNum2].setStench(1)
                
        except IndexError:
            print("** index error **")
    
    elif(section == 3):
         # handles preventing gold to be in pit or with whompus
        while((array[randomNum1][randomNum2].getPermanentPit() == 1) or (array[randomNum1][randomNum2].getPermanentWhompus() == 1)):
            randomNum1 = random.randint(0, (rows-1))
            randomNum2 = random.randint(0, (columns-1))
        # setting gold location
        array[randomNum1][randomNum2].setGold(1)
        
def printArray(array, row, column):
    for row in array:
        print("[ " ,  end=' ' )
        for column in row:
            print( (column.nodeNumber) ,  end='  ')   
        print("]")    

def implementArray(array, rows, columns):
     pitCounter = 0
     counter = 1
     rowCounter = 0
     colCounter = -1

     for rowCounter in range(rows):
        while counter <= (columns * (rowCounter + 1)):
            colCounter += 1
            if (counter < 10):
                array[rowCounter][colCounter] = Node(("{:02d}".format(counter) ),rowCounter, colCounter,0,0,0,0,0,0,0,0,0,0,0)
            else:
                array[rowCounter][colCounter] = Node(counter,rowCounter, colCounter,0,0,0,0,0,0,0,0,0,0,0)
            counter += 1	
        colCounter = -1

    # radomize placements for pits and breeze
     print("--------------------------------------------------")
     print("Hidden information from player, locations of... ")
     while (pitCounter < ((rows * columns)*.15)):
        randomPlacements(1, array, rows, columns)
        pitCounter += 1
         
    # stenchs take up 4 tiles around the whompus
     randomPlacements(2, array, rows, columns)
    #radomize placement for gold
     randomPlacements(3, array, rows, columns)
     print("--------------------------------------------------")
     print()

def lookForParent(array, rows, columns, list, parentNumber):
	for rowNum in range(rows):
			for columnNum in range(columns):
                    
				# check for number that match end-goal
				if (array[rowNum][columnNum].nodeNumber == parentNumber):
					#updating to the next parent number
					parentNumber = array[rowNum][columnNum].parent

					if not ( array[rowNum][columnNum].nodeNumber == ((rows * columns)-(columns - 1))): #checks to see if it's the stating node
						# added to list of parents
						list.append(array[rowNum][columnNum].nodeNumber)
						lookForParent(array, rows, columns, list, parentNumber)
	
def markArrayWorld(array, row, column, goldRow, goldColumn):
    activeParentList = False
    #collect the node number of the node with gold
    num = array[goldRow][goldColumn].getNodeNUmber()

    #first check if the parent list is filled
    if ( int(array[goldRow][goldColumn].parent) > 0):
          activeParentList = True

    if not activeParentList:
        for rowNum in range(row):
            for columnNum in range(column):
                # check for node that is the start
                if (array[rowNum][columnNum].nodeNumber ==  ((rows * column) - (column - 1))):
                    array[rowNum][columnNum].nodeNumber = "Start:" + str(array[rowNum][columnNum].nodeNumber) 
                # check for node that has the gold 
                elif (array[rowNum][columnNum].getGold() == 1):
                    array[rowNum][columnNum].nodeNumber = "  Gold:" + str(num) 
                # check for node that has the breeze
                elif (array[rowNum][columnNum].getBreeze() == 1):
                    array[rowNum][columnNum].nodeNumber = "    Breeze" 
                # check for node that has the stench
                elif (array[rowNum][columnNum].getStench() == 1):
                    array[rowNum][columnNum].nodeNumber = "    Stench"
                          
                # check for node that has the whompus
                elif (array[rowNum][columnNum].getWhompus() == 2):
                    array[rowNum][columnNum].nodeNumber = "    Whompus"
                # check for node that has the pit
                elif (array[rowNum][columnNum].getPit() == 2):
                     array[rowNum][columnNum].nodeNumber = "    Pit"
                else:
                     array[rowNum][columnNum].nodeNumber = "      " + str(array[rowNum][columnNum].nodeNumber) 
    else:
        for rowNum in range(row):
             for columnNum in range(column):
                # check for number that match node with goldS
                if (array[rowNum][columnNum].getGold() == 1):
                    array[rowNum][columnNum].nodeNumber = "  Gold:" + str(num) 
                    
                    list = []
                    lookForParent(array, row, column, list, array[rowNum][columnNum].parent)
        
        print()
        print("Here is the list of parents from node with the gold to starting node")
        print(" From 'Gold'  "+ str(list) + "  'start' ")
        print()
        print("Here is an illustration of the path:")
        print("The X marks is the path from the starting node to the where the gold was found")
        
        for rowNum in range(row):
             for columnNum in range(column):
                if ( (array[rowNum][columnNum].nodeNumber) in list):
                    array[rowNum][columnNum].nodeNumber = "      X:" + str(array[rowNum][columnNum].nodeNumber) 
                
                # check for number that match start
                elif (array[rowNum][columnNum].nodeNumber == ((rows * column) - (column - 1))):
                    array[rowNum][columnNum].nodeNumber = "X Start:" + str(array[rowNum][columnNum].nodeNumber) 
                
                elif (array[rowNum][columnNum].getGold() == 1):
                    array[rowNum][columnNum].setNodeNUmber(" X Gold:" + str(num))   
                
                else:
                    array[rowNum][columnNum].nodeNumber = "        " + str(array[rowNum][columnNum].nodeNumber) 
    print("-----------------------------------------------------")
    printArray(array,row,column)
    print("-----------------------------------------------------")

def generateHcost(array, rows, columns, currentRow, currentColumn, neighborRow, neighborColumn, listMovesMade, origntation): 
    unsafePitDanger = 0
    unsafeWhompusDanger = 0
    # safe if no breeze and stench
    if ((array[currentRow][currentColumn].getBreeze() == 0) and (array[currentRow][currentColumn].getStench() == 0)):
        unsafePitDanger = 0
        unsafeWhompusDanger = 0

    # not safe if breeze but no stench
    elif ((array[currentRow][currentColumn].getBreeze() == 1) and (array[currentRow][currentColumn].getStench() == 0)):
        # handles if breeze but no stench
        unsafeWhompusDanger = 0
        unsafePitDanger = 5

        #check neighbers around to increase accuracy
        if(len(listMovesMade) > 0):
            try:
                #north
                if (origntation == 1):
                  # checks rows x2 above
                  if (neighborRow - 2) > -1 : # -1 or less then is out of bound
                       if ( (array[neighborRow - 2][neighborColumn].getBreeze() == 1) and ((array[neighborRow - 2][neighborColumn]) in listMovesMade) ): # chekcs if theres a breeze and node has been stepped on before
                            array[neighborRow][neighborColumn].setPit(1) # this means array[neighborRow][neighborColumn] maybe has a pit
                            unsafePitDanger = 10   

                       elif ( (array[neighborRow - 2][neighborColumn].getBreeze() == 0) and ((array[neighborRow - 2][neighborColumn]) in listMovesMade) ): # chekcs if theres no breeze and node has been stepped on before
                            unsafePitDanger = 5   
                              
                #west
                if (origntation == 2):
                  # checks column x2 right
                  if (neighborColumn + 2) < columns: # 4 or greater is out of bound
                        if((array[neighborRow][neighborColumn + 2].getBreeze() == 1) and ((array[neighborRow][neighborColumn + 2]) in listMovesMade)):
                              array[neighborRow][neighborColumn].setPit(1) # this means array[neighborRow][neighborColumn] maybe has a pit
                              unsafePitDanger = 10

                        elif ( (array[neighborRow][neighborColumn + 2].getBreeze() == 0) and ((array[neighborRow][neighborColumn + 2]) in listMovesMade) ): # chekcs if theres no breeze and node has been stepped on before
                            unsafePitDanger = 5       
                        
                #south
                if (origntation == 3):
                  # checks rows x2 below
                  if (neighborRow + 2) < rows : # 4 or greater then is out of bound
                        if((array[neighborRow + 2][neighborColumn].getBreeze() == 1) and ((array[neighborRow + 2][neighborColumn]) in listMovesMade)):
                             array[neighborRow][neighborColumn].setPit(1) # this means array[neighborRow][neighborColumn] maybe has a pit
                             unsafePitDanger = 10

                        elif ( (array[neighborRow + 2][neighborColumn].getBreeze() == 0) and ((array[neighborRow + 2][neighborColumn]) in listMovesMade) ): # chekcs if theres no breeze and node has been stepped on before
                            unsafePitDanger = 5 
                        
                #east
                if (origntation == 4):
                  # checks column x2 left 
                  if(neighborColumn - 2) > -1: # -1 or less then is out of bound
                        if ((array[neighborRow][neighborColumn - 2].getBreeze() == 1) and ((array[neighborRow][neighborColumn - 2]) in listMovesMade)):
                             array[neighborRow][neighborColumn].setPit(1) # this means array[neighborRow][neighborColumn] maybe has a pit
                             unsafePitDanger = 10

                        elif ( (array[neighborRow][neighborColumn - 2].getBreeze() == 0) and ((array[neighborRow][neighborColumn - 2]) in listMovesMade) ): # chekcs if theres no breeze and node has been stepped on before
                            unsafePitDanger = 5 
                        
            except IndexError:
                  print("** index error in h calculations **")

    # not safe if stench but no breeze
    elif ((array[currentRow][currentColumn].getStench() == 1) and (array[currentRow][currentColumn].getBreeze() == 0)):
        unsafeWhompusDanger = 5
        unsafePitDanger = 0

        #check neighbers around to increase accuracy
        if(len(listMovesMade) > 0):
            try:
                #north
                if (origntation == 1):
                  # checks rows x2 above
                  if (neighborRow - 2) > -1 : # -1 or less then is out of bound
                       if ( (array[neighborRow - 2][neighborColumn].getStench() == 1) and ((array[neighborRow - 2][neighborColumn]) in listMovesMade)): # chekcs if theres a breeze and node has been  stepped on before
                            array[neighborRow][neighborColumn].setWhompus(1) # this means array[neighborRow][neighborColumn] maybe has a whompus
                            unsafeWhompusDanger = 10  

                       elif ( (array[neighborRow - 2][neighborColumn].getBreeze() == 0) and ((array[neighborRow - 2][neighborColumn]) in listMovesMade) ): # chekcs if theres no stench and node has been stepped on before
                            unsafeWhompusDanger = 5  
                #west
                if (origntation == 2):
                  # checks column x2 right
                  if (neighborColumn + 2) < columns: # 4 or greater is out of bound
                        if((array[neighborRow][neighborColumn + 2].getStench() == 1) and ((array[neighborRow][neighborColumn + 2]) in listMovesMade)):
                              array[neighborRow][neighborColumn].setWhompus(1) # this means array[neighborRow][neighborColumn] maybe has a whompus
                              unsafeWhompusDanger = 10

                        elif ( (array[neighborRow][neighborColumn + 2].getBreeze() == 0) and ((array[neighborRow][neighborColumn + 2]) in listMovesMade) ): # chekcs if theres no stench and node has been stepped on before
                            unsafeWhompusDanger = 5
                #south
                if (origntation == 3):
                  # checks rows x2 below
                  if (neighborRow + 2) < rows : # 4 or greater then is out of bound
                        if((array[neighborRow + 2][neighborColumn].getStench() == 1) and ((array[neighborRow + 2][neighborColumn])) in listMovesMade):
                             array[neighborRow][neighborColumn].setWhompus(1) # this means array[neighborRow][neighborColumn] maybe has a whompus
                             unsafeWhompusDanger = 10
                        
                        elif ( (array[neighborRow + 2][neighborColumn].getBreeze() == 0) and ((array[neighborRow + 2][neighborColumn]) in listMovesMade) ): # chekcs if theres no stench and node has been stepped on before
                            unsafeWhompusDanger = 5
                #east
                if (origntation == 4):
                  # checks column x2 left 
                  if(neighborColumn - 2) > -1: # -1 or less then is out of bound
                        if ((array[neighborRow][neighborColumn - 2].getStench() == 1) and ((array[neighborRow][neighborColumn - 2])) in listMovesMade):
                             array[neighborRow][neighborColumn].setWhompus(1) # this means array[neighborRow][neighborColumn] maybe has a whompus
                             unsafeWhompusDanger = 10

                        elif ( (array[neighborRow][neighborColumn - 2].getBreeze() == 0) and ((array[neighborRow][neighborColumn - 2]) in listMovesMade) ): # chekcs if theres no stench and node has been stepped on before
                            unsafeWhompusDanger = 5
            except IndexError:
                  print("** index error in h calculations **")

    # not safe if stench and breeze
    elif ((array[currentRow][currentColumn].getStench() == 1) and (array[currentRow][currentColumn].getBreeze() == 1)):
        unsafeWhompusDanger = 5
        unsafePitDanger = 5
         
         #check neighbers around to increase accuracy
        if (len(listMovesMade) > 0):
            try:
                #north
                if (origntation == 1):
                  # checks rows x2 above
                  if (neighborRow - 2) > -1 : # -1 or less then is out of bound
                       if ( (array[neighborRow - 2][neighborColumn].getStench() == 1) and (array[neighborRow - 2][neighborColumn].getBreeze() == 1) and ((array[neighborRow - 2][neighborColumn]) in listMovesMade)): # chekcs if theres a breeze and node has been  stepped on before
                            array[neighborRow][neighborColumn].setWhompus(1) # this means array[neighborRow][neighborColumn] maybe has a whompus
                            unsafeWhompusDanger = 10 
                            unsafePitDanger = 10 

                       elif ( (array[neighborRow - 2][neighborColumn].getStench() == 0) and (array[neighborRow - 2][neighborColumn].getBreeze() == 0) and ((array[neighborRow - 2][neighborColumn]) in listMovesMade) ): # chekcs if theres no stench and node has been stepped on before
                            unsafeWhompusDanger = 5 
                            unsafePitDanger = 5 
                #west
                if (origntation == 2):
                  # checks column x2 right
                  if (neighborColumn + 2) < columns: # 4 or greater is out of bound
                        if((array[neighborRow][neighborColumn + 2].getStench() == 1) and (array[neighborRow][neighborColumn + 2].getBreeze() == 1) and ((array[neighborRow][neighborColumn + 2]) in listMovesMade)):
                              array[neighborRow][neighborColumn].setWhompus(1) # this means array[neighborRow][neighborColumn] maybe has a whompus
                              unsafeWhompusDanger = 10 
                              unsafePitDanger = 10 

                        elif ( (array[neighborRow][neighborColumn + 2].getStench() == 0) and (array[neighborRow][neighborColumn + 2].getBreeze() == 0) and ((array[neighborRow][neighborColumn + 2]) in listMovesMade) ): # chekcs if theres no stench and node has been stepped on before
                            unsafeWhompusDanger = 5
                            unsafePitDanger = 5
                #south
                if (origntation == 3):
                  # checks rows x2 below
                  if (neighborRow + 2) < rows : # 4 or greater then is out of bound
                        if((array[neighborRow + 2][neighborColumn].getStench() == 1) and (array[neighborRow + 2][neighborColumn].getBreeze() == 1) and ((array[neighborRow + 2][neighborColumn])) in listMovesMade):
                             array[neighborRow][neighborColumn].setWhompus(1) # this means array[neighborRow][neighborColumn] maybe has a whompus
                             unsafeWhompusDanger = 10
                             unsafePitDanger = 10 
                        
                        elif ( (array[neighborRow + 2][neighborColumn].getStench() == 0) and (array[neighborRow + 2][neighborColumn].getBreeze() == 0) and ((array[neighborRow + 2][neighborColumn]) in listMovesMade) ): # chekcs if theres no stench and node has been stepped on before
                            unsafeWhompusDanger = 5
                            unsafePitDanger = 5
                #east
                if (origntation == 4):
                  # checks column x2 left 
                  if(neighborColumn - 2) > -1: # -1 or less then is out of bound
                        if ((array[neighborRow][neighborColumn - 2].getStench() == 1) and (array[neighborRow][neighborColumn - 2].getBreeze() == 1) and ((array[neighborRow][neighborColumn - 2])) in listMovesMade):
                             array[neighborRow][neighborColumn].setWhompus(1) # this means array[neighborRow][neighborColumn] maybe has a whompus
                             unsafeWhompusDanger = 10
                             unsafePitDanger = 10 

                        elif ( (array[neighborRow][neighborColumn - 2].getStench() == 0) and (array[neighborRow][neighborColumn - 2].getBreeze() == 0) and ((array[neighborRow][neighborColumn - 2]) in listMovesMade) ): # chekcs if theres no stench and node has been stepped on before
                            unsafeWhompusDanger = 5
                            unsafePitDanger = 5
            except IndexError:
                  print("** index error in h calculations **")
    #TESTING
    else:
        print("PROBLEM READING CURRENT ROW AND COLUMN IN H-CALC")

    #Scale: 20% unsafe   15% unsafe   10% unsafe  5% unsafe  0% unsafe
    unsafe = unsafePitDanger + unsafeWhompusDanger
    return unsafe
   
def generateNewFacingDirection(oldRow, oldColumn, newRow, newColumn, array):
     newfacingDirection = -1

     #if newRow is above oldRow
     if ((newRow == oldRow) and (newColumn == oldColumn)):
          newfacingDirection = array[newRow][newColumn].getFacingDirection()
     else:
        if (newRow < oldRow):
            newfacingDirection = 1
        #if newRow is below oldRow
        elif (newRow > oldRow):
            newfacingDirection = 3

        elif (newRow == oldRow):
             #left
            if (newColumn < oldColumn):
                newfacingDirection = 4
            #right
            elif(newColumn > oldColumn):
                newfacingDirection = 2

     return newfacingDirection 

def generateGCost(orintation, oldOrintation, oldGcost):
     counter = 0
     if orintation < oldOrintation:
        counter = (oldOrintation - orintation) + 1  # cost-to-turn + cost-to-move
     elif orintation > oldOrintation:
        counter = (orintation - oldOrintation) + 1
     else:
        counter += 1

     return (counter + oldGcost)

def aStar(array, row, column, score):
    openList = minHeap( row * column)
    closedList = []
    parentList = []
    steppedNodes = []
    currentRow = -1
    startingRow = -1
    currentColumn = -1
    startingColumn = -1
    goalRow = -1
    goalColumn = -1

    currentOrintation = -1 
    oldRow = -1
    oldColumn = -1
	# Keep searching until the conditions is met
    stopSearching = False
    goalFound = False
    
    for iterate in range(2):
        for rowNum in range(row):
              for columnNum in range(column):
                    if iterate == 0:
                          if (array[rowNum][columnNum].getGold() == 1):
                            goalRow = array[rowNum][columnNum].getRow()
                            goalColumn = array[rowNum][columnNum].getColumn()
                    else:
                        # check for number that match start and adds it to the openList
                        if (array[rowNum][columnNum].getNodeNUmber() == ((row * column)-(column-1))): #in a 4x4 getNodeNUmber is compared to 13
                            startingRow = array[rowNum][columnNum].getRow()
                            startingColumn = array[rowNum][columnNum].getColumn()
                            currentRow = array[rowNum][columnNum].getRow() 
                            currentColumn = array[rowNum][columnNum].getColumn()
                            # generate g h and f cost
                            array[startingRow][startingColumn].setG(0)
                            array[startingRow][startingColumn].setH(0) #set to zero because there is no likelyhood of dying # generateHcost(goalRow, goalColumn, (startingRow), (startingColumn), startingColumn, startingRow)
                            array[startingRow][startingColumn].setF( array[startingRow][startingColumn].getG() + array[startingRow][startingColumn].getH() )
                            array[startingRow][startingColumn].parent = 0

                            # agents starts game facing right
                            currentOrintation = array[startingRow][startingColumn].setFacingDirection(2)
                            # current facing direction of agent
                            currentOrintation =  array[rowNum][columnNum].facingDirection

						    # add to open list
                            openList.insert(array[rowNum][columnNum])
                          
                            # added to list of discovered nodes
                            steppedNodes.append(array[startingRow][startingColumn])

    #list used to check horizontal/verticle neighbors
    potentialNeighbor = [
          PotentialNeighbors(-1, 0, 1), #up
          PotentialNeighbors(0, -1, 4), #left
          PotentialNeighbors(0, 1, 2), #right
          PotentialNeighbors(1, 0, 3) #down
          ]
    
    #check if current node has the gold, otherwise the while loop will execute
    if (array[startingRow][startingColumn].getGold() == 1):
        stopSearching = True
        print("The gold was found!!")
        if (len(parentList) == 0):
            print("There is no path because the stating node was in the same spot as the goal node")
            score = 1000

    while not stopSearching:
        oldRow = currentRow
        oldColumn = currentColumn

        #pop off the node with lowest value and set to it as "current" node
        currenntNode = openList.removeMin()
        currentRow = currenntNode.row  
        currentColumn = currenntNode.column
        
        currentOrintation = (generateNewFacingDirection(oldRow,oldColumn,currentRow,currentColumn, array) )   # use this to pass to h cost and g cost  #currenntNode.setFacingDirection(
        array[currentRow][currentColumn].setFacingDirection(currentOrintation)
 
        #check if theres a high chance whompus is ahead, option to shoot
        if( (array[currentRow][currentColumn].getH() > 4) and (array[currentRow][currentColumn].getStench() == 1) ):
            print()
            print("Theres high chance the whompus is on node ahead of you, want to shoot your arrow? (shooting will dedeuct 10 points)" )
            decision = int(input(" Select  1 for yes  or  2 for no : ") )
            print()
            if (decision == 1):
                 #check if whompus is there
                 if (array[currentRow][currentColumn].getPermanentWhompus() == 1):
                      print(" YAYY SHOOT WHOMPUS!!!")
                      array[currentRow][currentColumn].setPermanentWhompus(0) 
                 else:
                      print("Darn whompus was not there, lost the last arrow available..")
                 useArrow = True
                 score -= 10
                 print()

        #check if current node has the gold, otherwise the while loop will continue to execute
        if (array[currentRow][currentColumn].getGold() == 1):
            stopSearching = True
            goalFound = True
            break

        #check if there agent stepped in a pit or there is whompus
        elif (array[currentRow][currentColumn].getPermanentWhompus() == 1):
            stopSearching = True
            print()
            print("Xx Found Whompus !!! xX")
            print("   Game Over  ")
            score -= 1000
            break
        elif (array[currentRow][currentColumn].getPermanentPit() == 1):
            stopSearching = True
            print()
            print("Xx Fell into Pit !!! xX")
            print("   Game Over  ")
            score -= 1000
            break  
        
        #generate neighbors: use nested for-loop
        for neighbor in potentialNeighbor:
            dontExecute = False
            neighborRow = neighbor.x
            neighborColumn = neighbor.y 
            neighborOrintation = neighbor.facing


            #ignore neighbors out of bounds of the world
            if (currentRow + neighborRow) < 0 or (currentColumn + neighborColumn) < 0 or (currentColumn + neighborColumn) > (column - 1) or (currentRow + neighborRow) > (row - 1):
                #print("Out of bounds!")
                dontExecute = True
            else:
                #ignore neighbors in the closed list   (might adjust to allow agent to step on a tile again)
                if (array[currentRow + neighborRow][currentColumn + neighborColumn] in closedList):
                    #print("Node is already in the closed list")
                    dontExecute = True
                if (openList.contains(array[currentRow + neighborRow][currentColumn + neighborColumn])):
                    #print("Node is already in the open list")
                    #if the neighbor is already in the open list,  update the g cost to what it cost now (update f too)
                    array[currentRow + neighborRow][currentColumn + neighborColumn].setG(generateGCost(neighborOrintation, currentOrintation, array[currentRow + neighborRow][currentColumn + neighborColumn].getG())) 
                    array[currentRow + neighborRow][currentColumn + neighborColumn].setF(array[currentRow + neighborRow][currentColumn + neighborColumn].getG() + array[currentRow + neighborRow][currentColumn + neighborColumn].getH())
                    array[currentRow + neighborRow][currentColumn + neighborColumn].parent = array[currentRow][currentColumn].nodeNumber
                    #print("Node in the open list was updated!")

                    dontExecute = True
        
            if not dontExecute : 
                    # generate g h and f cost
                    array[currentRow + neighborRow][currentColumn + neighborColumn].setG(generateGCost(neighborOrintation, currentOrintation, array[currentRow][currentColumn].getG()))
                    array[currentRow + neighborRow][currentColumn + neighborColumn].h = generateHcost(array, row, column, currentRow, currentColumn, (currentRow + neighborRow), (currentColumn + neighborColumn), steppedNodes, neighborOrintation)
                    array[currentRow + neighborRow][currentColumn + neighborColumn].f = array[currentRow + neighborRow][currentColumn + neighborColumn].g + array[currentRow + neighborRow][currentColumn + neighborColumn].h
                    array[currentRow + neighborRow][currentColumn + neighborColumn].parent = array[currentRow][currentColumn].nodeNumber

                    #add neighbors to open list
                    openList.insert(array[currentRow + neighborRow][currentColumn + neighborColumn])
                
                    if (openList.size == 0):
                        print("Ran out of safe tiles! The gold was unreachable!")
                        stopSearching = True

                    #move the old current to the closed list
                    closedList.append(array[currentRow][currentColumn])
                    # added to list of discovered nodes
                    steppedNodes.append(array[currentRow + neighborRow][currentColumn + neighborColumn])
                    #updating score
                    score -= 1

        #print("******* end of generating neighbors **********")
        #print()
    
    if(goalFound):
        print()
        print("You have found the gold!!!")
        print("Gold has been picked up and will now return to the stairs")
        markArrayWorld(arrayOfWorld, rows, cols,goalRow, goalColumn )
        score += 1000

    return score

	

# START OF GAME
# set up world with a 2D array
rows, cols = 4,4
arrayOfWorld = [[0] * cols for _ in range(rows)]

stopPlaying = False

while not stopPlaying:
    print(" ~~~~~~  Welcome to Whompus World! ~~~~~~ ")
    print()
    quitGame = int( input("Please press the number zero if you would like to quit or the number one to continue: ") )
    print()

    if quitGame == 0:
        stopPlaying = True
    else:
        playerScore = 0
        # randomize the locations of breeze, stench, whompus, gold, pit
        implementArray(arrayOfWorld, rows, cols)
        
        print(" ~~~  Starting grid of the world  ~~~  ")
        printArray(arrayOfWorld, rows, cols)

        # A* will keep track of the players score
        playerScore = aStar(arrayOfWorld, rows, cols, playerScore)

       
        # END OF GAME
        # prints the players score at the end of every game
        print()
        print(" Final Score: " + str(playerScore))
        print()
        print(" ~~~~  You have reached the end of the gane  ~~~~  ")
        print() 

print("Come back and play!")

'''
Score Rubric:
 +1000 for climbing out of the cave with the gold
 -1000 for falling into a pit or being eaten by the Wumpus
 -1 for each action taken
 -10 for using up the arrow
'''