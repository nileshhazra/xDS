from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def depth_first_values(root):
    if root is None:
        return []
    values = []
    stack = [root]
    while stack:
        current = stack.pop()
        values.append(current.val)
        if current.right is not None:
            stack.append(current.right)
        if current.left is not None:
            stack.append(current.left)
    return values


def r_depth_first_values(root):
    if root is None:
        return []
    left_values = r_depth_first_values(root.left)
    right_values = r_depth_first_values(root.right)
    return [root.val, *left_values, *right_values]


def breadth_first_values(root):
    if root is None:
        return []
    values = []
    # queue = [root]
    queue = deque([root])
    while queue:
        # current = queue.pop(0) # because of this - TC - O(n^2)
        current = queue.popleft()  # now it's O(n)
        values.append(current.val)

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

    return values


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

# depth_first_values(a)
res = r_depth_first_values(a)
print(res)
#   -> ['a', 'b', 'd', 'e', 'c', 'f']
