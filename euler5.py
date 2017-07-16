def euler5():
    """What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""
    
    #make an implementation in a for loop that accepts a number and does the test for all values up to that number
    i = 0
    while True:
        i+=20
        if (i % 11 != 0):
            continue
        elif (i % 12 != 0):
            continue
        elif (i % 13 != 0):
            continue
        elif (i % 14 != 0):
            continue
        elif (i % 15 != 0):
            continue
        elif (i % 16 != 0):
            continue
        elif (i % 17 != 0):
            continue
        elif (i % 18 != 0):
            continue
        elif (i % 19 != 0):
            continue
        else:
            return i;       