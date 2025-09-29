def reverseWordsInString(string):
    string = list(string)
    reverse = []
    final = []
    while string != []:
        if string[-1] == ' ':
            while reverse!=[]:
                final.append(reverse.pop())
            final.append(string.pop())
            
        else:
            reverse.append(string.pop())
            
    while reverse !=[]:
        final.append(reverse.pop())
        
    return ''.join(final)

reverseWordsInString("I am Nik!")
reverseWordsInString("   Allen Wee pls can I eat   ")