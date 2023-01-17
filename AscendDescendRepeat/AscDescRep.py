def ascend_descend(length, minimum, maximum):
    # Your code here
    if maximum < minimum or length == 0:
        return ""
    
    x = ""
    cNum = minimum
    while cNum < maximum and len(x) < length:
        x += str(cNum)
        cNum += 1
    
    if len(x) > length:
        return x[:length]
    
    while cNum > minimum and len(x) < length:
        x += str(cNum)
        cNum -= 1
        
    if len(x) > length:
        return x[:length]

    if minimum == maximum:
        x = str(minimum)
    
    y = x
    while len(x) < length:
        x += y
        
    return x[:length]