class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next = b
b.next = c
c.next = d


def sum_list(a):
    sum = 0
    curr = a
    while curr is not None:
        sum += curr.val
        curr = curr.next

    return sum


print(sum_list(a))


def sum_list_r(head):
    if head.next is None:
        return head.val
    return head.val + sum_list_r(head.next)


print(sum_list_r(a))
