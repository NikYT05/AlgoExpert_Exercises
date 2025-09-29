# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 01:26:45 2022

@author: raphael luigi tan
"""

MyList = ["b", "a", "a", "c", "b", "a", "c", 'a']
res = {}

for i in MyList:
    res[i] = MyList.count(i)
    
print(res)

def tournamentWinner(competitions, results):
    list_of_winners = []
    for i in range(len(results)):
        if results[i] == 1:
            list_of_winners.append(competitions[i][0])
        else:
            list_of_winners.append(competitions[i][1])
    
    winners = {}
    for j in list_of_winners:
        winners[j] = list_of_winners.count(j)
        
    max_val = max(winners, key=winners.get)
        
    return max_val


tournamentWinner([
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"]
  ], [0, 0, 1])

tournamentWinner([
    ["HTML", "Java"],
    ["Java", "Python"],
    ["Python", "HTML"],
    ["C#", "Python"],
    ["Java", "C#"],
    ["C#", "HTML"],
    ["SQL", "C#"],
    ["HTML", "SQL"],
    ["SQL", "Python"],
    ["SQL", "Java"]
  ], [0, 1, 1, 1, 0, 1, 0, 1, 1, 0])