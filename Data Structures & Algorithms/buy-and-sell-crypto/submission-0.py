class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice=prices[0]
        maxprof=0
        for i in range(0,len(prices)):
            curprice=prices[i]
            if(curprice<minprice):
                minprice=curprice
            else:
                prof=curprice-minprice
                if(prof>maxprof):
                    maxprof=prof
        return maxprof