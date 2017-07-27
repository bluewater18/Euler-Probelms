def euler22(filename):
    """Names to Scores"""
    names = getFile(filename)
    summ = 0
    for x in range(1,len(names)):
        getNameNum(names[x])
        summ += x * getNameNum(names[x])   
        
    return summ
    
    
def getFile(filename):
    """creates a list of names from the filename passed in"""
    f = open(filename)
    lines = f.readlines()
    f.close()
    names = []
    names.append("")
    for name in lines[0].split(','):
        
        names.append(name[1:-1])
    names = sorted(names)
    return names

        
        
def getNameNum(name):
    """takes a name and returns a score based on the sum of the letters"""
    dicto = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
    summ = 0
    for letter in name:
        summ += dicto.get(letter.lower())
    return summ
