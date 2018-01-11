# Josephus problem
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
def createLinkList(length):
    i=1
    head = Node(1)
    a = head 
    while i <= length:
        if i == length:
            a.next = head
        else:
            a.next = Node(i+1)
            a = a.next
        i += 1
    return head
    
def showLinkList(node):
    result=[]
    head = node
    while node.next != head:
        result.append(node.value)
        node = node.next
    result.append(node.value)
    print result

def getLength(node):
    head = node
    count = 1
    while node.next != head:
        node = node.next
        count += 1
    return count
    
def killNode(node,step):
    head = node
    count = 1
    while head.next.next != head:
        #showLinkList(head)
        #print 'node:',node.value
        if count == (step - 1 ) :
            #print 'kill:',node.next.value
            node.next = node.next.next
            node = node.next
            head = node
            count = 1
        else:
            count += 1
            node = node.next
    return head

# main
node = createLinkList(41)
showLinkList(node)
print 'length:',getLength(node)
surviver = killNode(node,3)
showLinkList(surviver)

'''
output:

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41]
length: 41
[16, 31]

'''
