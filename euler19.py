import datetime
import calendar
    

def euler19Calender(start,end,weekday):
    """returns the number of times the weekday occurs at the start of the month between the start and end end years inclusive"""
    summ = 0
    for y in range(start,end+1):
        #print(y)
        for m in range(1,13):
            
            day,days = calendar.monthrange(y,m)
            if day == weekday:
                summ += 1
    return summ

def euler19Datetime(start,end,weekday,monthday):
    """returns the number of times the WEEKDAY occurs at MONTHDAY of the month between the START and END years inclusive"""
    total = 0
    for y in range(start,end+1):
        for m in range(1,13):
            if datetime.datetime(y,m,monthday).weekday()==weekday:
                total+=1
    return total


