class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        array = []
        temp = self
        while temp:
            array.append(temp.val)
            temp = temp.next

        return str(array)
    
def listNode(array = []):
    if (len(array) == 0):
        return ListNode()
    else:
        val = array[0]
        if len(array) > 1:
            next = listNode(array[1:])
        else:
            next = None

        return ListNode(val, next)

def swap(parent1, parent2):
    node1 = parent1.next
    node2 = parent2.next
    if not node1 or not node2:
        return
    
    tail2 = node2.next

    if parent1.next == parent2:
        parent2.next = node1
        node1.next = tail2
        parent1.next = node2
    else:
        node1 = parent1.next
        node2 = parent2.next
        if not node1 or not node2:
            return
        
        tail2 = node2.next

        parent2.next = None
        node2.next = node1.next
        node1.next = tail2

        parent1.next = node2
        parent2.next = node1