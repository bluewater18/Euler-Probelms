def euler14(x):
    """which starting number, under x, produces the longest collatz chain?"""
    #use dp
    dic = {1:1}
    for x in range(1,x):
        collatzHelper(x,dic)
    
    #print(max(list(dic.keys())))
    #print(dic.items())
    maxs = (0,0)
    for key in sorted(dic.keys()):
        
        if key < x and dic.get(key) != None:
            if dic.get(key) > maxs[1]:
                maxs = [key,dic.get(key)]
    return maxs[0]
    
    
    
def collatzHelper(x,dic):
    #dic = number : length of chain?
    
        
        
    if x%2 == 0:
        n = x/2
        if n in dic.keys():
            dic[x] = dic.get(n)+1
            return dic.get(x)
        else:
            
            dic[x] = collatzHelper(n,dic)+1
            return dic.get(x)
    else:
        n=3*x+1
        if n in dic.keys():
            dic[x] = dic.get(n)+1
            return dic.get(x)
        else:
            dic[x] = collatzHelper(n,dic) +1   
            return dic.get(x)