class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        res = 1
        i = -1
        while self.stack and len(self.stack)>= abs(i) and self.stack[i]<=price:
            res+=1
            i -= 1
        else:
            self.stack.append(price)
        return res
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)