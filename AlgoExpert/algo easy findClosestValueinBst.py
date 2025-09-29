null = None
'''
def findClosestValueInBst(tree, target):
    diff = abs(tree.value-target)
    if diff == 0:
        return target
    
    if tree.value > target:
        if tree.left == None and abs(target - tree.left.value) > diff:
            return tree.value
        
        if diff > abs(target-tree.left.value):
            findClosestValueInBst(tree.left, target)
        else:
            return tree.value
        
    else:
            if tree.right == None and abs(target - tree.left.value) > diff:
                return tree.value
            
            if diff > abs(target - tree.right.value):
                findClosestValueInBst(tree.right, target)
            else:
                return tree.value
'''

def findClosestValueInBst(tree, target):
    from sys import maxsize
    closest = maxsize
    current = tree
    while current is not None:
        if abs(current.value - target) < abs(closest-target):
            closest = current
            
        if current.value > target:
            current = current.right
        elif current.value < target:
            current = current.left
        else:
            break
        
    return closest
    
findClosestValueInBst({"nodes": [
    {"id": "10", "left": "5", "right": "15", "value": 10},
    {"id": "15", "left": "13", "right": "22", "value": 15},
    {"id": "22", "left": null, "right": null, "value": 22},
    {"id": "13", "left": null, "right": "14", "value": 13},
    {"id": "14", "left": null, "right": null, "value": 14},
    {"id": "5", "left": "2", "right": "5-2", "value": 5},
    {"id": "5-2", "left": null, "right": null, "value": 5},
    {"id": "2", "left": "1", "right": null, "value": 2},
    {"id": "1", "left": null, "right": null, "value": 1}
  ],
  "root": "10"}, 12)


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
