def balancedBrackets(string):
    x = [ ]
    for i in string:
        if i == '[' or i == '{' or i == '(':
            x.append(i)
            
        elif (i == ')' or i == ']' or i == '}'):
            if x == []:
                return False
            
            if i == ')' and x[-1] == '(':
                x.pop()
                
            elif i == ']' and x[-1] == '[':
                x.pop()
                
            elif i == '}' and x[-1] == '{':
                x.pop()
            else:
                return False
                    
        else:
            continue
            
    if x == []:
        return True
    else:
        return False
    
balancedBrackets("([])(){}(())()()")