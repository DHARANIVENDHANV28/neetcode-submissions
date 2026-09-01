class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l,r = 0,len(people)-1
        res = 0
        while l<=r:
            if people[l]+people[r]<=limit:
                res+=1
                l+=1
                r-=1
            elif people[r]<=limit:
                res+=1
                r-=1
            elif people[l]<=limit:
                res+=1
                l+=1
        return res


































        # res = 0
        # l = 0
        # r = len(people)-1
        # people = sorted(people)
        # while l<=r:
        #     remain = limit - people[r]
        #     r -= 1
        #     res += 1
        #     if l <= r and remain >= people[l]:
        #         l += 1
        # return res
                

        