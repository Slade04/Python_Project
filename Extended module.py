x=range(1,10,2)
print(list(x))
print(tuple(x))

from math import *
print(max([1,24,37,94]))
print(min([1,24,37,94]))
print(log10(1000))
print(log(64,2))
print(pow(2,0.5))
# If module "math" is imported, function "pow" cannot have the third parameter

from random import *
ml=[2,3,4,5,6,7,8,9,10,11,12,13]
print(choice(ml))
print(choice(range(2,33,4)))
# The sentence above is equal to that below
print(randrange(2,33,4))
print(round(random()))
print(sample([1,4,2,6,4,8],3))
# It's easy to see that the result of function "semple" is a list, whose elements are shuffled
print(shuffle(ml))
# It's incorrect to use this function in this way(above)
shuffle(ml)
print(ml)
shuffle(ml)
print(ml)
shuffle(ml)
print(ml)
print(uniform(2,39))
# Real number generator
print('\n')

import time as t_m
print(t_m.time())
# Function "time" returns the time as in second since 1970AD in the form of "float"
print(t_m.localtime(t_m.time()))
print('The year is'+str(t_m.localtime(t_m.time())[0]))
print(t_m.asctime())
print(t_m.ctime(t_m.time()))
print(t_m.strftime('%Y - %m - %d   %H:%M:%S'))
print('\n')


from calendar import *
setfirstweekday(0)
# Monday as the first day of a week
print(firstweekday())
print(isleap(2020))
# Give judgement to whether a year is a leap year
print(leapdays(2000,2020))
# Enter the number of years between two parameters as in year that are leap years
print(month(2020,2))
print(weekday(2020,2,2))
print(monthrange(2020,2))
