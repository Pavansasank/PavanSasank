def Bestchooice(prices,windowsize):
    currentprice = sum(prices[:windowsize])
    maxprice = currentprice
    for i in range(windowsize,len(prices)):
        left_c = prices[i-windowsize]
        right_c = prices[i]
        currentprice = currentprice-left_c+right_c
        if currentprice>maxprice:
            maxprice = currentprice
    return maxprice

prices = [2,4,6,7,1,3,5]
windowsize = 3
Bestchooice(prices,windowsize)
print(Bestchooice(prices,windowsize))