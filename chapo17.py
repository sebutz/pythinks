class Time:
    '''
     the parameters are optional
    '''

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def print_time(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))

    def time_to_int(self):
        return self.second + self.minute * 60 + self.hour * 3600
    '''
    when invoke print __str__ method is called
    '''

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    '''
    overloading +
    '''
    def __add__(self, other):
        print("self time to int: ", self.time_to_int())
        print("other time to int: ", other.time_to_int())
        seconds = self.time_to_int() + other.time_to_int()
        print("seconds added: ",  seconds)
        return int_to_time(seconds)



def int_to_time(seconds):
        minutes, second = divmod(seconds, 60)
        hour, minute = divmod(minutes, 60)
        return Time(hour, minute, second)


time = Time()
time.print_time()  # 00:00:00
print(str(time))
print(time)  #


start = Time(9, 45)
print(start)
duration = Time(1, 35)
print(duration)

print(start + duration)   # __add__
