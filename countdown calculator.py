'''Build a countdown calculator. Write some code that can take two dates as input, and
#then calculate the amount of time between them
'''

from datetime import datetime

print('')
date1 = input()
date2 = input()

#  convert them into a date format by using datetime.strptime


date_time1= datetime.strptime(date1,"%Y/%m/%d")

date_time2= datetime.strptime(date2,"%Y/%m/%d")


amountoftime= date_time2-date_time1

print(f'The amount of time between those two dates is {amountoftime}')

