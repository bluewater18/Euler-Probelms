def euler11():


    grid = getGrid('grid.txt')
    largest = 0
    ##horozontal
    for y in range(len(grid)):
        for x in range(len(grid[y])-3):
            #print(grid[y][x])
            pro = grid[y][x] * grid[y][x+1] * grid[y][x+2] * grid[y][x+3]
            if pro > largest:
                largest = pro
    ##diagonal
    for y in range(len(grid)-3):
        #right
        for x in range(len(grid[y])-3):
            #print(grid[y][x])
            pro = grid[y][x] * grid[y+1][x+1] * grid[y+2][x+2] * grid[y+3][x+3]
            if pro > largest:
                largest = pro
        #left
        for x in range(3,len(grid[y])):
            pro = grid[y][x] * grid[y+1][x-1] * grid[y+2][x-2] * grid[y+3][x-3]
            if pro > largest:
                largest = pro            
                

                
    ##vertical            
    for y in range(len(grid)-3):
        for x in range(len(grid)):
            #print(grid[y][x])
            pro = grid[y][x] * grid[y+1][x] * grid[y+2][x] * grid[y+3][x]
            if pro > largest:
                largest = pro            
        
    #print(largest)
    return largest
    
def getGrid(filename):
    grid = []
    f = open(filename)
    lines = f.readlines()
    for line in lines:
        line.strip()
        lineList = line.split(' ')
        for x in range(len(lineList)):
            lineList[x] = int(lineList[x])
        grid.append(lineList)    
    return grid