def get_generation(cells, generation):
    cGen = [x[:] for x in cells]   #current generation
    editGen = [x[:] for x in cGen] #the edited generation
    yMax = len(cells)              #number of rows
    xMax = len(cells[0])           #number of columns
    
    for i in range(generation):    #iterating through each generation
        
        for y in range(yMax):      
            for x in range(xMax):  #iterating through each cell
                lifeCount = 0
                for neighY in range(3):
                    for neighX in range(3):
                        lifeCount += cGen[(y - 1 + neighY) % yMax][(x - 1 + neighX) % xMax]
                lifeCount -= cGen[y][x]
                
                #neighbour sum, essentially a sum of the 3x3 grid of the cell and then subtracting the original cells values
                #to only have the value of its neighbours
                
                    
                    
                if lifeCount <2 or lifeCount >3:
                    editGen[y][x] = 0
                if lifeCount == 3:
                    editGen[y][x] = 1
                #giving life or death to each cell depending on its neighbours
                
        
        cGen = [x[:] for x in editGen] #setting the current gen to the edited version
        
    
    return(cGen) #returning the final product mi amigos