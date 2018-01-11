class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
    
    # Binary Search Tree    
    def insert(self,value):
        if value < self.val:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
            return True
        elif value > self.val:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)
            return True
        else:
            print "Node exists:",value
            return False
        
    # Perorder Traversal (root -> left -> right)
    def preorder(self,node):
        if node is None:
            return []
        else:
            leftList = self.preorder(node.left)
            rightList = self.preorder(node.right)
            result = [node.val] + leftList + rightList
            return result
    
    # Inorder Traversal (left -> root -> right)
    # this method will get a order list from small to big
    def inorder(self,node):
        if node is None:
            return []
        else:
            leftList = self.inorder(node.left)
            rightList = self.inorder(node.right)
            result = leftList + [node.val] + rightList
            return result
        
    # Postorder Traversal (left -> right -> root)
    def postorder(self,node):
        if node is None:
            return []
        else:
            leftList = self.postorder(node.left)
            rightList = self.postorder(node.right)
            result = leftList + rightList + [node.val]
            return result
        
    # Level Traverse (level one -> level two -> ...)
    def levelorder(self,node):
        if node is None:
            return []
        else:
            nodeList = []
            result = []
            nodeList.append(node)
            while nodeList:
                treeNode = nodeList.pop(0)
                result.append(treeNode.val)
                if treeNode.left is not None:
                    nodeList.append(treeNode.left)
                if treeNode.right is not None:
                    nodeList.append(treeNode.right)
            return result
        
    # search a target value in tree or not
    def isContain(self,target):  
        if target > self.val:
            if self.right == None:
                return False
            else:
                return self.right.isContain(target)
        elif target < self.val:
            if self.left == None:
                return False
            else:
                return self.left.isContain(target)
        else:
            return True

# Main
root = TreeNode(5)
inputList = [5,3,6,2,4,7]

for i in inputList:
    flag = root.insert(i)for i in inputList:
    flag = root.insert(i)
    if flag:
        print "insert",i

print 'preorder:',root.preorder(root)
print 'inorder:',root.inorder(root)
print 'postorder:',root.postorder(root)
print 'levelorder:',root.levelorder(root)

for i in range(1,10):
    print 'i',i,root.isContain(i)


# output:

'''
Node exists: 5
insert 3
insert 6
insert 2
insert 4
insert 7

preorder: [5, 3, 2, 4, 6, 7]
inorder: [2, 3, 4, 5, 6, 7]
postorder: [2, 4, 3, 7, 6, 5]
levelorder: [5, 3, 6, 2, 4, 7]

i 1 False
i 2 True
i 3 True
i 4 True
i 5 True
i 6 True
i 7 True
i 8 False
i 9 False

'''