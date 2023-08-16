from datetime import datetime


class Clock:

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
        if self.__day < self.get_daysInMonth(self.__month):
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

    def __str__(self):
        # Returns a string representation of the clock in this format: "2021-01-25 00:00:00"
        # self.__strYear = f"{self.__year:04}"
        # self.__strHour = f"{self.__hour:02}"
        d = datetime(self.__year, self.__month, self.__day, self.__hour,
                     self.__min, self.__sec)
        s = '{:%Y-%m-%d %H:%M:%S}'.format(d)
        return '{:%Y-%m-%d %H:%M:%S}'.format(d)

    def set_clock(self, year, month, day, hour, min, sec):
        self.__year = year if year >= 0 else 0
        self.__month = month if 0 < month <= 12 else 1
        self.__day = day if 0 < day <= self.get_daysInMonth(month) else 1
        self.__hour = hour if 0 <= hour < 24 else 0
        self.__min = min if 0 <= min < 60 else 0
        self.__sec = sec if 0 <= sec < 60 else 0

    def get_daysInMonth(self, month):
        if (self.isLeapYear() and month == 2):
            return 29
        elif (not self.isLeapYear() and month == 2):
            return 28
        elif (((month % 2 != 0) and (month < 8))
              or ((month % 2 == 0) and (month > 7))):
            return 31
        else:
            return 30

    def isLeapYear(self):
        return (self.__year % 4 == 0
                and self.__year % 100 != 0) or (self.__year % 400 == 0)


def main():
    clock = Clock(2021, 1, 30, 23, 59, 59)
    clock.inc_sec()
    s = str(clock)
    print(s)


if __name__ == "__main__":
    main()
