def euler16(y,x):
    """What is the sum of the digits of the number y^x"""
    
    summ = 0
    for x in list(str(y**x)):
        summ += int(x)
    return summ