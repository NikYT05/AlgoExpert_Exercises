# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        array = []
        array.append(self.name)
        q = []
        q.extend(self.children)
        for i in q:
            array.append(i.name)
            q.extend(i.children)
            
        return array
            
parent = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')

parent.addChild('B')
parent.addChild('C')
parent.children[0].addChild('D')
parent.children[0].addChild('E')
parent.children[1].addChild('F')
parent.children[0].children[0].addChild('G')


print(parent.breadthFirstSearch([]))