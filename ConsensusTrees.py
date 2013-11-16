
from Caesal import *
partitionD = {}

def consensusValues():
    tipL = flatten(treeList[0])
    for tree in treeList:
        partitionL = partition(tree)
        partitionString(tipL, partitionL)

    for key in partitionD.keys():
        partitionD[key] *= 100.0/len(treeList)
        
    return partitionD



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
        # Start at 1 because our special leaf always is '1'
        partitionStr = '1'

        # If the partition contains a tip, it is not grouped with special leaf
        for tip in tipL[1:]:
            if tip in newPartition:
                partitionStr += '0'
            else:
                partitionStr += '1'
        if not partitionD.has_key(partitionStr):
            partitionD[partitionStr] = 1

        # If we've seen it before, increase it's count
        else:
            partitionD[partitionStr] += 1
    return partitionD
                
