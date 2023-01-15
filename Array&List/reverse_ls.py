class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList_iterative(head):
    '''
    given a head of a list, reverse the entire list iteratively and returns the new head.
    '''
    pre = None
    cur = head
    while cur:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
    return pre


def reverse_recursive(node):
    '''
    given a head of a list, reverse the entire list recursively and returns the new head.
    '''
    if (node == None):
        return node
         
    if (node.next == None):
        return node
         
    res = reverse_recursive(node.next)
    # reverse the curr_node and the reversed rest of node.
    node.next.next = node # node.next now is the next pointer of the last node of the reversed list.
    node.next = None # node now is the last node.
    return res