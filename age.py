from datetime import *

def get_date():
    year = int(input("Please input a year (4 digit): "))
    month = int(input("Please input a month (2 digit): "))
    day = int(input("Please input a day (2 digit): "))

    d = date(year, month, day)
    return d

def diff_dates(inp_date):
    cur_date = datetime.now()
    cur_year = cur_date.year

    inp_year = inp_date.year
    diff = cur_year - inp_year
    return diff

def age_calc():
    return diff_dates(get_date())

print(age_calc())




