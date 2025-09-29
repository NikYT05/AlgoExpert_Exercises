def isPalindrome(string):
    i=0
    k=-1
    while i != len(string)//2:
        if string[i]==string[k]:
            i+=1
            k-=1
        else:
            return False
    return True

assert isPalindrome('abcdcba') == True
assert isPalindrome('abcd') == False
