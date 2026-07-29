class MovingAverage:

    def __init__(self, size: int):
        self.ws = size
        self.cur = [] 

    def next(self, val: int) -> float:
        self.cur.append(val)

        if len(self.cur) > self.ws:
            self.cur.pop(0)
        
        return sum(self.cur)/len(self.cur)

        
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
