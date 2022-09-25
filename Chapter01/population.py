pop = 312032486

seconds_per_year = 60 * 60 * 24 * 365

births_per_year = 60 * 60 * 24 * 365 / 7
deaths_per_year = 60 * 60 * 24 * 365 / 13
immigrants_per_year = 60 * 60 * 24 * 365 / 45

inc_per_year = births_per_year - deaths_per_year + immigrants_per_year
year1 = (inc_per_year * 1) + pop
year2 = (inc_per_year * 2) + pop
year3 = (inc_per_year * 3) + pop
year4 = (inc_per_year * 4) + pop
year5 = (inc_per_year * 5) + pop

print(year1)
print(year2)
print(year3)
print(year4)
print(year5)