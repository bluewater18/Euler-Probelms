from functions import findDiv
def euler12(x):
    """What is the value of the first triangle number to have over x divisors?"""
    i =1
    c=1
    while True:
        
        #print("i is :"+ str(i))
        #print("*************")
        #print("*************")
        temp = len(findDiv(i))
        #print(temp)
        
        if temp>x:
            return i
        c+=1
        i+=c