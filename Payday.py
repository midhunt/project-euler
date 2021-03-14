"""
Gets pay date for the year 
"""

import calendar
from datetime import datetime


def payday(year=2021):

    for mon in range(1,13):
        month_range = calendar.monthrange(year, mon)
        last_day = str(year) + '-' + str(mon) + '-' + str(month_range[1])
        last_day = datetime.strptime(last_day, '%Y-%m-%d').weekday()

        if calendar.day_name[last_day] == 'Sunday':
            pay_day = str(year) + '-' + str(mon) + '-' + str(month_range[1] - 2)
        elif calendar.day_name[last_day] == 'Saturday':
            pay_day = str(year) + '-' + str(mon) + '-' + str(month_range[1] - 1)
        else:
            pay_day = str(year) + '-' + str(mon) + ' ' + str(month_range[1])

        print(pay_day)

# payday(2021)