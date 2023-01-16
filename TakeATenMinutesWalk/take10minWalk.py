def is_valid_walk(walk):
    #determine if walk is valid
    if len(walk) == 10:  #walk length check
        checkV = 0
        checkH = 0
        
        #coordinate grid math check, original position = 0 
        for i in walk:
            if i == "n":
                checkV += 1
            elif i == "s":
                checkV -= 1
            elif i == "e":
                checkH += 1
            elif i == "w":
                checkH -= 1
                
        if checkV == 0 and checkH == 0:
            return ( True )
        else:
            return ( False )
        
    else:
        return ( False )
    