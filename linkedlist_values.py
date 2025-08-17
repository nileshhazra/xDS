class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d


def linked_list_values(a):
    values = []
    _linked_list_values(a, values)
    return values


def _linked_list_values(a, values):
    if a is None:
        return
    values.append(a.val)
    _linked_list_values(a.next, values)


print(linked_list_values(a))  # -> [ 'a', 'b', 'c', 'd' ]
