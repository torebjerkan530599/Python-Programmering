
from MyClock import Clock
import unittest

class Test_Clock(unittest.TestCase):

  def setUp(self):  # RUNS BEFORE EACH TEST!
    self.__clock = Clock()

  def test_set_clock_illegal_values(self):
    self.__clock.set_clock(-1, 13, 42, 40, 70, 80)
    self.assertEqual(str(self.__clock), "0000-01-01 00:00:00")

  def test_inc_sec_from_default_values(self):
    self.__clock.inc_sec()
    self.assertEqual(str(self.__clock), "0000-01-01 00:00:01")

  def test_inc_min_from_default_values(self):
    self.__clock.inc_min()
    self.assertEqual(str(self.__clock), "0000-01-01 00:01:00")

  def test_inc_sec_from_midnight_jan(self):
    self.__clock = Clock(2021, 1, 31, 23, 59, 59)
    self.__clock.inc_sec()
    self.assertEqual(str(self.__clock), "2021-02-01 00:00:00")

  def test_inc_sec_from_feb_to_feb_leap_year_2021(self):
    self.__clock = Clock(2020, 2, 28, 23, 59, 59)
    self.__clock.inc_sec()
    self.assertEqual(str(self.__clock), "2020-02-29 00:00:00")

  def test_inc_sec_from_feb_to_mar_not_leap_year(self):
    self.__clock = Clock(2019, 2, 28, 23, 59, 59)
    self.__clock.inc_sec()
    self.assertEqual(str(self.__clock), "2019-03-01 00:00:00")

  def test_inc_sec_from_2000_to_2001(self):
    self.__clock = Clock(2000, 12, 31, 23, 59, 59)
    self.__clock.inc_sec()
    self.assertEqual(str(self.__clock), "2001-01-01 00:00:00")

  def test_inc_days_not_leap_year(self):
    self.__clock = Clock(2021, 1, 15, 13, 30, 10)
    for x in range(365):
      self.__clock.inc_day()
    self.assertEqual(str(self.__clock), "2022-01-15 13:30:10")

  def test_inc_days_leap_year(self):
    self.__clock = Clock(2004, 1, 12, 12, 15, 10)
    for x in range(366):
      self.__clock.inc_day()
    self.assertEqual(str(self.__clock), "2005-01-12 12:15:10")

  def test_inc_year_from_default_values(self):
    self.__clock.inc_year()
    self.assertEqual(str(self.__clock), "0001-01-01 00:00:00")

  def test_inc_day_middle_of_august(self):
    self.__clock = Clock(2005, 8, 13, 15, 30, 59)
    self.__clock.inc_day()
    self.assertEqual(str(self.__clock), "2005-08-14 15:30:59")

  def test_inc_sec_from_feb_to_feb_leap_year_2000(self):
    self.__clock = Clock(2000, 2, 28, 23, 59, 59)
    self.__clock.inc_sec()
    self.assertEqual(str(self.__clock), "2000-02-29 00:00:00")

  def test_inc_min_from_feb_to_feb_leap_year(self):
    self.__clock = Clock(2000, 2, 28, 23, 59, 00)
    self.__clock.inc_min()
    self.assertEqual(str(self.__clock), "2000-02-29 00:00:00")

#   def main(self):
#     self.setUp()
#     self.test_set_clock_illegal_values()
#     self.test_set_clock_from_default_values()
#     self.test_set_clock_from_midnight_jan()
#     self.test_set_clock_from_feb_to_feb_leap_year_2021()
#     self.test_set_clock_from_feb_to_mar_not_leap_year()
#     self.test_set_clock_from_2000_to_2001()
#     self.test_inc_days_not_leap_year()
#     self.test_inc_days_leap_year()
#     self.test_inc_year_from_default_values()
#     self.test_inc_day_middle_of_august()
#     self.test_inc_sec_from_feb_to_feb_leap_year_2000()
#     self.test_inc_min_from_feb_to_feb_leap_year()


if __name__ == '__main__':
    unittest.main()
