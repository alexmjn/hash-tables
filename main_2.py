class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def find(self, value):
        # start at head, loop through list, find value, return node.
        cur = self.head
        while cur is not None:
            if cur.value == value:
                return cur
            cur = cur.next

        return None

    def delete(self, value):
        # find index
        # make previous "next" skip this
        cur = self.head
        if cur.value == value:
            self.head = cur.next
            return cur
        # traditional linked list delete: return the node that you delete.

        prev = cur
        cur = cur.next

        while cur is not None:
            if cur.value == value:
                prev.next = cur.next
                return cur

            else:
                prev = cur
                cur = cur.next

        return None

# in hash tables, should return values, not nodes.

    def insert_at_head(self, node):
        node.next = self.head
        self.head = node
