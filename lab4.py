############################################################
# Name: Aidan Miller
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# CS115 Lab 4
#
############################################################

def knapsack(capacity, itemList):
    '''
    This function returns the maximum value and the list of items without exceeding the capacity of le knapsack using recursion.
    '''
    if itemList == [] or capacity <= 0:
        return [0, []]
    elif capacity < itemList[0][0]:
        return knapsack(capacity, itemList[1:])
    else:
        use = knapsack(capacity - itemList[0][0], itemList[1:])
        lose = knapsack(capacity, itemList[1:])
        if lose[0] < itemList[0][1] + use[0]:
            return [itemList[0][1] + use[0]] + [[itemList[0]] + use[1]]
        else:
            return [lose[0]] + [lose[1]]
