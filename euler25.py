def euler25(length):
    fibList = [1,1]
    i=len(fibList)
    while len(str(fibList[-1]))<length:
        i+=1
        fibList.append(fibList[-1]+fibList[-2])
        
    return i