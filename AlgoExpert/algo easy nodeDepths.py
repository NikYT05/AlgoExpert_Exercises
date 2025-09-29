def nodeDepths(root, depth_sum = 0, node_depths = []):
    # if node_depths is None:
    #     node_depths = []
    
    if root is None:
        return sum(node_depths)
        
    node_depths.append(depth_sum)
    nodeDepths(root.left, depth_sum + 1, node_depths)
    nodeDepths(root.right, depth_sum + 1, node_depths)

    return node_depths

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

tree_data = {
    "nodes": [
        {"id": "1", "left": "2", "right": None, "value": 1},
        {"id": "2", "left": None, "right": None, "value": 2}
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
depths = nodeDepths(root)

print("Node Depths:", depths)
print("Sum of Depths:", sum(depths))

node_map = {}
for node in tree_data2["nodes"]:
    node_map[node["id"]] = BinaryTree(node["value"])

# Step 2: Assign children
for node in tree_data2["nodes"]:
    current = node_map[node["id"]]
    if node["left"]:
        current.left = node_map[node["left"]]
    if node["right"]:
        current.right = node_map[node["right"]]

# Step 3: Get root and test
root = node_map[tree_data2["root"]]
depths = nodeDepths(root)

print("Node Depths:", depths)
print("Sum of Depths:", sum(depths))