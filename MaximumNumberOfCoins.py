def maxCoins( piles):
    piles.sort()
    itvalue = len(piles)//3
    ptr = -2
    counter = 0

    while itvalue:
        counter += piles[ptr]
        ptr -= 2
        itvalue -=1
    
    return counter

piles = [2,0,2,1,1,0]
print(maxCoins(piles))
