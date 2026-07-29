class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize:
            return False
        
        count = {}
        for h in hand:                              #O(n)
            count[h] = 1+count.get(h,0)
        hand.sort()                                 #O(nlogn)
        for num in hand:                            #O(n)
            if count[num]:
                for i in range(num,num+groupSize):  
                    if i not in count or not count[i]:
                        return False
                    count[i] -= 1
        return True