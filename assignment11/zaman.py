class Time:
    def __init__(self, hh, mm, ss):
        self.hour=hh
        self.minute=mm
        self.second=ss
        self.fix()

    def show(self):
        print(self.hour, ":", self.minute, ":", self.second)

    def sum(self, other): #other=zaman_2
        s_new = self.second + other.second
        m_new = self.minute + other.minute
        h_new = self.hour + other.hour
        result = Time(h_new, m_new, s_new)
        return result

    def sub(self, other):
        s_new = self.second - other.second
        m_new = self.minute - other.minute
        h_new = self.hour - other.hour
        result = Time(h_new, m_new, s_new)
        return result

    def time_to_second(self):
        second=self.hour * 3600 + self.minute * 60 + self.second
        return second

    def second_to_time(self):
        hour = self//3600
        minute = (self % 3600)//60
        second = self % 60
        result= Time (hour,minute, second)
        return result


    def GMT_to_Tehran(self):
        tehran_time = Time(3, 30, 00)
        result= self.sum(tehran_time)
        return result

    def fix(self):
        if self.second >=60:
            self.second -=60
            self.minute += 1

        if self.minute >= 0:
            self.minute -=60
            self.hour +=1

        if self.second <0:
            self.second +=60
            self.minute -= 1
        
        if self.minute < 0:
            self.minute += 60
            self.hour -= 1
        

t1=Time(3, 45, 17)
t1.show()

t2=Time(4, 13, 2)
t2.show()

#t1+t2
t3=t1.sum(t2)
t3.show()

#t2-t1
t4=t2.sub(t1)
t4.show()

#time to second
t5=t1.time_to_second()
print(t5)

#second to time
t6=Time.second_to_time(3665)
t6.show()

#GMT to tehran time
tehran_time= t1.GMT_to_Tehran()
tehran_time.show()