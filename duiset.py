# Binary Tree Node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to compute the left-most, right-most, and depth-most nodes
def compute_extents(root):
    if root is None:
        return None

    left_most = None
    right_most = None
    depth_most = None

    # Perform a level-order traversal
    queue = [(root, 0)]  # (node, depth)
    while queue:
        node, depth = queue.pop(0)

        # Update left-most node
        if left_most is None or depth < left_most[1]:
            left_most = (node, depth)

        # Update right-most node
        if right_most is None or depth > right_most[1]:
            right_most = (node, depth)

        # Update depth-most node
        if depth_most is None or depth > depth_most[1]:
            depth_most = (node, depth)

        # Enqueue left and right children
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))

    return left_most[0], right_most[0], depth_most[0]
