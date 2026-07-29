class MyCalendar:
    
    def __init__(self):
        self.Booking = []
        

    def book(self, startTime: int, endTime: int) -> bool:

        if self.Booking:
            for i in self.Booking:
                s,e = i[0],i[1]
                if max(startTime, s) < min(endTime, e): #or startTime<=s<endTime or startTime<=e<endTime:
                    return False
        self.Booking.append([startTime,endTime])
        print(self.Booking)
      
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)