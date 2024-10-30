class Node:
    def __init__(self, pre=None, next=None, val=0):
        self.pre = pre
        self.next = next
        self.val = val

# Node constructor
head = Node(None, None, 7)  # First node
second = Node(head, None, 3)  # Second node
head.next = second  # Link second node to first

# Linked list usage
print("First node value:", head.val)  # Should print 7
print("Second node value:", head.next.val)  # Should print 3

# Sum values
sum_val = 0
sum_val += head.val
current_node = head
while current_node.next:
    current_node = current_node.next
    sum_val += current_node.val

print("Sum of values:", sum_val)
