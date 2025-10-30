"""
Write a function that takes a positive integer represented as a string number and an integer numDigits. 
Remove numDigits from the string so that the number represented by the string is as large as possible afterwards.

Note that the order of the remaining digits cannot be changed. 
You can assume numDigits will always be less than the length of number and greater than or equal to 0.
"""

def bestDigits(number, numDigits):
    stack, check = [], 0
    for i in range(len(number)):

        if i == 0:
            stack.append(number[i])
            top = int(stack[-1])
            continue
            
            
        while int(number[i]) > top and check < numDigits:
            stack.pop()
            check += 1            

            if stack == []:
                break
            else:
                top = int(stack[-1])
                
        
        stack.append(number[i])
        top = int(stack[-1])
    
    while check < numDigits:
        stack.pop()
        check += 1
        
    return "".join(stack)

print(bestDigits("462839", 2))
print(bestDigits("129847563", 4))
print(bestDigits("21", 1))
print(bestDigits('1003002', 4)) #302