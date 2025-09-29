#positive number is savory, negative is sweet
#pairing never too savory than target
#if no pairing, then return [0,0]
def sweetAndSavory(dishes, target):
    import math
    dishes = sorted(dishes)
    negatives = []
    positives = []
    closest = 9999
    pair = [0,0]
    
    for flavors in dishes:
        if flavors < 0:
            negatives.append(flavors)
        else:
            positives.append(flavors)
    
    #this condition checks 
    if len(negatives) == 0 or len(positives) == 0:
        return [0,0]
            
    for i in negatives:
        for j in positives:
            if i + j > target:
                continue
            elif math.sqrt((i+j)**2 + target**2) < math.sqrt(closest**2 + target**2):
                pair = [i,j]
                closest = i + j
            else:
                continue
                
        print(closest)
        print(pair)
    return pair

#assert sweetAndSavory([-3, -5, 1, 7], 8) == [-3, 7]

print(sweetAndSavory([-3, -5, 1, 7], 8))