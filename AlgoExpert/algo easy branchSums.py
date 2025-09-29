# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root, branch_sum = 0, sums = None):
    if sums is None:
        sums = []
    
    if root is None:
        return sums # my mistake here is that I wrote return only. 
    # When this happens with a tree with a single leaf, it would move down to the next code block and return nothing. 
    
    if root.left is None and root.right is None:
        branch_sum += root.value
        sums.append(branch_sum)
        return
    
    
    branch_sum += root.value
    branchSums(root.left, branch_sum, sums)
    branchSums(root.right, branch_sum, sums)

    # My initial code looked like this:
    # if root is None:
    #     sums.append(sums)
    #     return
    
    # branch_sum += root.value
    # branchSums(root.left, branch_sum, sums)
    # branchSums(root.right, branch_sum, sums)
    # This returned a list with many unexpected behaviour.
    # Notice that when branchSums(root.left...) reaches a leaf, it appends to sums. But the same happens for root.right so duplicate sums are appended.
    # Hence, we preemptively check whether the node is a leaf by checking if it does not have any children and append it to the list.

    return sums

tree_data = {
  "nodes": [
    {"id": "1", "left": "2", "right": "3", "value": 1},
    {"id": "2", "left": "4", "right": "5", "value": 2},
    {"id": "3", "left": "6", "right": "7", "value": 3},
    {"id": "4", "left": "8", "right": "9", "value": 4},
    {"id": "5", "left": "10", "right": None, "value": 5},
    {"id": "6", "left": None, "right": None, "value": 6},
    {"id": "7", "left": None, "right": None, "value": 7},
    {"id": "8", "left": None, "right": None, "value": 8},
    {"id": "9", "left": None, "right": None, "value": 9},
    {"id": "10", "left": None, "right": None, "value": 10}
  ],
  "root": "1"
}

tree_data2 = {
    "nodes": [
        {"id": "1", "left": "2", "right": None, "value": 1},
        {"id": "2", "left": None, "right": None, "value": 2}
    ],
    "root": "1"
}

# Step 1: Create all nodes in a dictionary
node_map = {}
for node in tree_data["nodes"]:
    node_map[node["id"]] = BinaryTree(node["value"])

# Step 2: Assign children
for node in tree_data["nodes"]:
    current = node_map[node["id"]]
    if node["left"]:
        current.left = node_map[node["left"]]
    if node["right"]:
        current.right = node_map[node["right"]]

# Step 3: Get root and test
root = node_map[tree_data["root"]]
depths = branchSums(root)

print("Branch Sums", depths)
