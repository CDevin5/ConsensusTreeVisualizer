# Rachel Sherman, Ben Johnson, Coline Devin, and Sophia Williams

partitionD = {}

t1 = ('7', (('2', ('1', '3')), ('6', ('0', ('4', '5')))))
t2 = ('0', (('7', ('1', '3')), ('6', ('2', ('4', '5')))))
t3 = ('0', (('7', ('1', '3')), ('2', ('6', ('4', '5')))))
t4 = ('6', (('2', ('1', '3')), ('7', ('0', ('5', '4')))))
t5 = ('2', (('6', ('1', '3')), ('0', ('7', ('4', '5')))))
miniTreeL= [t1, t2, t3, t4, t5]

def consensusValues(treeL):
    tipL = flatten(treeL[0])
    for tree in treeL:
        partitionL = partition(tree)
        partitionString(tipL, partitionL)

    for key in partitionD.keys():
        partitionD[key] *= 100.0/len(treeL)
        
    return tipL



def partition(tree):
    ''' Given a tree, puts possible partitionings in dictionary '''

    # This creates a list of partitions such that the partition is a tuple
    # containing things that are NOT grouped with the special leaf
    partitionL = []
    if type(tree[0]) == tuple:
        partitionL.append(tree[0])
        partitionL.extend(partition(tree[0]))
    if type(tree[1]) == tuple:
        partitionL.append(tree[1])
        partitionL.extend(partition(tree[1]))
    return partitionL

def flatten(tree):
    ''' Returns a list of tips given a tree in Newick format '''
    tipL = []
    if type(tree) != tuple:
        tipL.append(tree)
    else:
        tipL.extend(flatten(tree[0]))
        tipL.extend(flatten(tree[1]))
    return tipL

def partitionString(tipL, partitionL):
    ''' Turns a list of partitions into a binary string and puts in a dictionary '''
    for partition in partitionL:
        newPartition = flatten(partition)
        partitionStr = ''

        # If the partition contains a tip, it is not grouped with special leaf
        for tip in tipL:
            if tip in newPartition:
                partitionStr += '0'
            else:
                partitionStr += '1'
        if not partitionD.has_key(partitionStr):
            partitionD[partitionStr] = 1

        # If we've seen it before, increase it's count
        else:
            partitionD[partitionStr] += 1
    return 

def flipBits(string):
    newString = ""
    for char in string:
        if char == "1":
            newString += "0"
        else:
            newString += "1"
    return newString

def stringNor(string1,string2):
    newS = ""
    for i in range(len(string1)):
        if (string[i] == '0') and (string2[i] == '0'):
            newS += "1"
        else:
            newS += "0"
    return newS

def stringAnd(string1,string2):
    newS = ""
    for i in range(len(string1)):
        if (string1[i] == '1') and (string2[i] == '1'):
            newS += "1"
        else:
            newS += "0"
    return newS

def stringOr(string1,string2):
    newS = ""
    for i in range(len(string1)):
        if (string1[i] == '0') and (string2[i] == '0'):
            newS += "0"
        else:
            newS += "1"
    return newS

def stringIsZeros(string):
    for char in string:
        if char == '1':
            return False
    return True

def countOnes(string):
    return string.count('1')

def findOnes(string):
    L = []
    for i in range(len(string)):
        if string[i] == '1':
            L += [i]
    return L

def findZeros(string):
    L = []
    for i in range(len(string)):
        if string[i] == '0':
            L += [i]
    return L

def bitwiseSubtract(string1, string2):
    newString = ''
    for i in range(len(string1)):
        if (string1[i] == string2[i]):
            newString += '0'
        elif (string1[i] == '1') and (string2[i] == '0') :
            newString += '1'
        else:
            newString += '0'
    return newString

def partitionsToTree(partitionStringL, tipL):
    ''' Takes a list of partition bitstrings with same consensus percentage,
    and outputs a newick consensus tree '''

    for i in range(len(partitionStringL)):
        s = partitionStringL[i]

        # Make the 1s represent the smaller partition
        if s.count('1') >= len(s)/2:
            partitionStringL[i] = flipBits(s)

    sortedPartitionStringL = sorted(partitionStringL, key=countOnes)
    seenTips = "0"*len(tipL)
    possibleChildren = []

    for i in range(len(sortedPartitionStringL)):
        
        currStr = sortedPartitionStringL[i]

        andedString = stringAnd(seenTips, currStr)
        onesIndices = findOnes(andedString)

        newick = "("
        if not stringIsZeros(andedString):
            newPossibleChildren = [] 
            for child in possibleChildren:

                wasAChild = False
                for oneIndex in onesIndices:

                    if child[0][oneIndex] == '1':
                        newick += child[1] + ","
                        wasAChild = True
                        break
                if not wasAChild:
                    newPossibleChildren.append(child)
                
            leftovers = bitwiseSubtract(currStr, andedString)
            possibleChildren = newPossibleChildren

        else:
            leftovers = currStr
        
        for j in range(len(leftovers)):
            if leftovers[j] == '1':
                newick += str(tipL[j]) + ","

        newick = newick [:-1] + ")"
        seenTips = stringOr(seenTips, currStr)
        
        possibleChildren.append([currStr, newick])
        
    finalLeftoverIndices = findZeros(seenTips)
    finalLeftovers = []
    for i in finalLeftoverIndices:
        finalLeftovers.append(str(tipL[i]))
    finalNewick = '(('
    for child in possibleChildren:
        finalNewick += child[1] + ","
    for leftover in finalLeftovers:
        finalNewick += leftover + ","
    finalNewick = finalNewick[:-1] + '))'
    
    return finalNewick

def main(consensusValue, filename):
    data = __import__(filename)
    if consensusValue <= 50:
        print "Invalid input, must be greater than 50"
        return
    tipL = consensusValues(data.treeList)
    partitionStringL = []
    for partition in partitionD:
        if partitionD[partition] >= consensusValue:
            partitionStringL += [partition]
    
    return partitionsToTree(partitionStringL, tipL)
