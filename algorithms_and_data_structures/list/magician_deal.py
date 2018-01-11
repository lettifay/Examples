class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

def createLinkList(length):
    node = Node(0)
    head = node
    for i in range(length - 1):
        node.next = Node(0)
        node = node.next
    node.next = head
    return head

def showLinkList(node):
    result = []
    head = node
    while node.next != head :
        result.append(node.value)
        node = node.next
    result.append(node.value)
    print result
    
def deal(node,length):
    head = node
    count = 1
    while count <= length:
        for i in range(1,count):
            while node.next.value != 0:
                node = node.next
            node = node.next
        
        node.value = count
        while (node.next.value != 0) and (count != length):
            node = node.next
        node = node.next
        count += 1
    return head

# Main
head = createLinkList(13)
showLinkList(head)
dealled = deal(head,13)
showLinkList(dealled)

'''
output:

[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[1, 8, 2, 5, 10, 3, 12, 11, 9, 4, 7, 6, 13]

'''
