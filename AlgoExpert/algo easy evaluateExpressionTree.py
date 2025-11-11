"""
You're given a binary expression tree. Write a function to evaluate this tree mathematically and return a single resulting integer.

All leaf nodes in the tree represent operands, which will always be positive integers. All of the other nodes represent operators. There are 4 operators supported, each of which is represented by a negative integer:

-1: Addition operator, adding the left and right subtrees.

-2: Subtraction operator, subtracting the right subtree from the left subtree.

-3: Division operator, dividing the left subtree by the right subtree. If the result is a decimal, it should be rounded towards zero.

-4: Multiplication operator, multiplying the left and right subtrees.

You can assume the tree will always be a valid expression tree. Each operator also works as a grouping symbol, meaning the bottom of the tree is always evaluated first, regardless of the operator.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def evaluateExpressionTree(root):
    stack = []
    
    def postOrder(tree):
        if tree is None:
            return
        
        postOrder(tree.left)
        postOrder(tree.right)
        # addition
        if tree.value == -1:
            result = stack.pop() + stack.pop()
            stack.append(result)
        # subtraction
        elif tree.value == -2:
            num2 = stack.pop()
            num1 = stack.pop()
            result = num1 - num2
            stack.append(result)
        # division
        elif tree.value == -3:
            num2 = stack.pop()
            num1 = stack.pop()
            if num1 / num2 < 0:
                stack.append(round(num1/num2))
            else:
                result = num1 // num2
                stack.append(result)
            
        # multiplication
        elif tree.value == -4:
            result = stack.pop() * stack.pop()
            stack.append(result)

        else:
            stack.append(tree.value)
        return
    
    postOrder(root)
    return stack.pop()

# Example tree:
#      -1
#      / \
#     3  -4
#        / \
#       7   9
root = Node(-1)
root.left = Node(3)
root.right = Node(-4)
root.right.left = Node(7)
root.right.right = Node(9)

root2 = Node(-2)
root2.left = Node(2)
root2.right = Node(3)

values = evaluateExpressionTree(root)
print("Values (post-order):", values)

print(evaluateExpressionTree(root2))

#print("Sum of all nodes:", sum(values))
