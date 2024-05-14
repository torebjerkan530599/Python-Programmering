class solution_clock:
        
    def __init__(self, year=0, month=0, day=0, hour=0, min=0, sec=0):
        self.set_clock(year, month, day, hour, min, sec)
        
    def inc_sec(self):
        if self.__sec < 59:
            self.__sec += 1
        else:
            self.__sec = 0
            self.inc_min()

    def inc_min(self):
        if self.__min < 59:
            self.__min += 1
        else:
            self.__min = 0
            self.inc_hour()

    def inc_hour(self):
        if self.__hour < 23:
            self.__hour += 1
        else:
            self.__hour = 0
            self.inc_day()

    def inc_day(self):
        if self.__day < self.__days_in_month(self.__month, self.__year):
            self.__day += 1
        else:
            self.__day = 1
            self.inc_month()
        

    def inc_month(self):
        if self.__month < 12:
            self.__month += 1
        else:
            self.__month = 1
            self.inc_year()
    
    def inc_year(self):
        self.__year += 1
    
    def __days_in_month(self, month, year):        
        solution_clock.months_31 = [1, 3, 5, 7, 8, 10, 12] # static variable
        solution_clock.months_30 = [4, 6, 9, 11] # static variable
        if month in solution_clock.months_30:
            return 30
        elif month in solution_clock.months_31:
            return 31
        else:            
            if self.__is_leapyear(year):
                return 29
            else:
                return 28

    def __is_leapyear(self, year):
        return (year % 4 == 0) and (year % 100 != 0) or (year % 400) == 0

    def __str__(self):
        return (f'{self.__year:04d}-{self.__month:02d}-{self.__day:02d} {self.__hour:02d}:{self.__min:02}:{self.__sec:02}')

    def set_clock(self, year, month, day, hour, min, sec):
        self.__year = year if year >= 0 else 0
        self.__month = month if 0 < month <= 12 else 1
        self.__day = day if 0 < day <= self.__days_in_month(self.__month, self.__year) else 1
        self.__hour = hour if 0 <= hour < 24 else 0
        self.__min = min if 0 <= min < 60 else 0
        self.__sec = sec if 0 <= sec < 60 else 0


def main():
    clock = solution_clock(2021, 1, 30, 23, 59, 59)
    clock.inc_min()
    s = str(clock)
    print(s)


if __name__ == "__main__":
    main()
