# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 17:24:51 2023

@author: raphael luigi tan
"""

def questions():
    chinese = ["你叫什么名字？", '你爸爸叫什么名字？', '你的生日是哪天？', "你妈妈叫什么名字？", "你今年几岁？", "你在哪里读书？"]
    
    import random
    n = 'yes'
    while n=='yes':
        word = random.choice(chinese)
        chinese.remove(word)
        print(word)
        
        if chinese == []:
            print("Congratulations!")
            break
        else:
            print()
            n = input("Conitnue? ")
            
def dates(questions):
    import random
    months = ["Jan.", "Feb.", "Mar.", "Apr.", "May", "June", "July", "Aug.", "Sept.", "Oct.", "Nov.", "Dec."]
    i = 0
    while i < questions:
        month  = random.choice(months)
        
        if month == "Feb.":
            days = random.randint(1,29)
            
        else: 
            days = random.randint(1,30)
            
        print(str(i+1) + ".", month, str(days)+",", "2023", "  ", "________________________")
        months.remove(month)
        if months == []:
            months = ["Jan.", "Feb.", "Mar.", "Apr.", "May", "June", "July", "Aug.", "Sept.", "Oct.", "Nov.", "Dec."]
        i += 1
    
    
def randomnum():
    import random
    content = []
    n = int(input())
    i = 1
    
    while i < n:
        num = random.randint(1,101)
        if num in content:
            continue
        else:
            content.append(num)
            i += 1
          
    k = 1
    for j in content:
        print(str(k) + '.', str(j), "__________")
        k += 1
    
        
        
#randomnum()
dates(20)
#questions()

    
    