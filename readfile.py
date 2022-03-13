def getlines():
    with open("input.txt", "r") as file:
        line = []    
        for i in file:
            stripped_line = i.strip()
            if not i.startswith("#"):
                line.append(i.strip())

        return line
            
def getwords():          
    word = []        
    for i in getlines():
        strippedword = i.split()
        word.append(i.split())
    return word

a = getwords()
print(a)


 
