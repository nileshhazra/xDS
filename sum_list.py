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


def linked_list_find(head, target):
    curr = head
    while curr is not None:
        if curr.val == target:
            return True
        curr = curr.next
    return False


def r_linked_list_find(head, target):
    if head is None:
        return False
    if head.val == target:
        return True
    return linked_list_find(head.next, target)


def get_node_value(head, index):
    curr = head
    count = 0
    while curr is not None:
        if count == index:
            return curr.val
        count += 1
        curr = curr.next

    return None


def get_node_value_r(head, index):
    if head is None:
        return None

    if index == 0:
        return head.val

    return get_node_value(head.next, index - 1)


def reverse_list(head):
    prev = None
    current = head
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev


def reverse_list(head, prev=None):
    if head is None:
        return prev
    next = head.next
    head.next = prev
    return reverse_list(next, head)
