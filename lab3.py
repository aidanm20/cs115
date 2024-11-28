############################################################
# Name: Aidan Miller
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# CS115 Lab 3
#
############################################################

def change(amount, coins):
    """
    This function returns the smallest number of coins it takes to reach amount
    """
    if amount == 0:
        return 0
    if coins == [] or amount < 0:
        return float("inf")
    elif coins[0] > amount:
        return change(amount, coins[1:])
    else:
        use_it = 1 + change(amount - coins[0], coins)
        lose_it = change(amount, coins[1:])
        return min(use_it, lose_it)



