def commonCharacters(strings):
    if len(strings)==1:
        return strings
    
    else:
        Common= []
        i=0
        firstchar=strings[0]
        
        while i<len(firstchar):
            k=1
            while k<len(strings)-1:
                if firstchar[i] in strings[k]:
                    k+=1
                    
                else:
                    break
                
            if k == len(strings)-1 and firstchar[i] not in Common:
                Common.append(firstchar[i])
                i+=1
                
            else:
                i+=1
        return print(Common)

commonCharacters(["abcd", 'cd43', 'hauc'])
commonCharacters(["hbc", "bcd", "bci", "obc"])
commonCharacters(["hbc", "bcd"])
commonCharacters(['a'])
commonCharacters(["ab&cdef!", "f!ed&cba", "a&bce!d", "ae&fb!cd", "efa&!dbc", "eff!&fff&fffffffbcda", "eeee!efff&fffbbbbbaaaaaccccdddd", "*******!***&****abdcef************", "*******!***&****a***********f*", "*******!***&****b***********c*"])