class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Function to find the Lowest Common Ancestor
def lowComAnc(root, p, q):
    if not root or root == p or root == q:
        return root

    left = lowComAnc(root.left, p, q)
    right = lowComAnc(root.right, p, q)

    if left and right:
        return root
    return left if left else right

# Helper function to build a binary tree from a list (level order)
def buildTree(nodes):
    from collections import deque
    if not nodes or nodes[0] is None:
        return None

    root = TreeNode(nodes[0])
    q = deque([root])
    i = 1
    while q and i < len(nodes):
        curr = q.popleft()
        if i < len(nodes) and nodes[i] is not None:
            curr.left = TreeNode(nodes[i])
            q.append(curr.left)
        i += 1

        if i < len(nodes) and nodes[i] is not None:
            curr.right = TreeNode(nodes[i])
            q.append(curr.right)
        i += 1
    return root
nodes = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
root = buildTree(nodes)

# Find references to p and q
def findNode(root, val):
    if not root:
        return None
    if root.val == val:
        return root
    return findNode(root.left, val) or findNode(root.right, val)

p = findNode(root, 5)
q = findNode(root, 1)

# Call func
ans = lowComAnc(root, p, q)

print("Lowest Common Ancestor:", ans.val)
