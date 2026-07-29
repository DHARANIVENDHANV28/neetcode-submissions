class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0]+flowerbed+[0]
        for i in range(len(flowerbed)-1):
            if n == 0:
                return True
            if sum(flowerbed[i:i+3]) == 0:
                flowerbed[i+1] = 1
                n -= 1

            
        return False