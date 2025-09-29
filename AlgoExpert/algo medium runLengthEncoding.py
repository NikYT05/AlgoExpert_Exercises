"""
def runLengthEncoding(string):
    x = []
    y = list(string)
    i = 0
    j = 1
    while i<len(string):
        if y[1]!=string[i] or j==9 or i==len(string)-1:
            x.append(str(j))
            x.append(string[i])
            y.pop(0)
            y.append(string[i])
            j=0
            i+=1
        else:
            i+=1
            j+=1
            y.pop(0)
            y.append(0)
        return print(''.join(x))


#runLengthEncoding('AAb') 
"""

def runLengthEncoding(string):
    x = []
    y = list(string)
    letter = y[0]
    y.pop(0)
    i = 1
    j = 0
    
    while y != []:
        
        if i == 9 or letter != y[0]:
            j = i
            x.append(str(j))
            x.append(letter)
            letter = y[0]
            y.pop(0)
            i = 1
            
        else:
            i += 1
            y.pop(0)
    
    x.append(str(i))
    x.append(letter)
    return ''.join(x)
    
assert runLengthEncoding("AAAABBBCD") == "4A3B1C1D"
            