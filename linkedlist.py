class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")

a.next = b
b.next = c
c.next = d
d.next = None


def print_list(head):
    current = head
    while current is not None:
        print(current.value)
        current = current.next


def print_recursive(head):
    if head is None:
        return
    if head.next is None:
        print(head.value)
        return
    print(head.value)
    print_recursive(head.next)


print_list(a)
print_recursive(a)
