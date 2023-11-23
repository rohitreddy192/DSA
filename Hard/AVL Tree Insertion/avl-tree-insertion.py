#User function Template for python3

''' structure of tree node:

class Node:
    def __init__(self,x):
        self.data=x
        self.left=None
        self.right=None
        self.height=1

'''
class Solution:
    def height(self, node):
        if not node:
            return 0
        return node.height

    def getBalance(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def rightRotate(self, y):
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))

        return x

    def leftRotate(self, x):
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def insertToAVL(self, node, key):
        # Step 1 - Perform the normal BST insertion
        if not node:
            return Node(key)
        
        if key < node.data:
            node.left = self.insertToAVL(node.left, key)
        elif key > node.data:
            node.right = self.insertToAVL(node.right, key)
        else:  # Duplicate keys not allowed
            return node

        # Step 2 - Update the height of the current node
        node.height = 1 + max(self.height(node.left), self.height(node.right))

        # Step 3 - Get the balance factor
        balance = self.getBalance(node)

        # Step 4 - Balance the tree if needed
        # Left Left Case
        if balance > 1 and key < node.left.data:
            return self.rightRotate(node)

        # Right Right Case
        if balance < -1 and key > node.right.data:
            return self.leftRotate(node)

        # Left Right Case
        if balance > 1 and key > node.left.data:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)

        # Right Left Case
        if balance < -1 and key < node.right.data:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)

        return node



#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self,x):
        self.data=x
        self.left=None
        self.right=None
        self.height=1

def isBST(n, lower, upper):
    if not n:
        return True
    
    if n.data <= lower or n.data >= upper:
        return False
    
    return isBST(n.left, lower, n.data) and isBST(n.right, n.data, upper)

def isBalanced(n):
    if not n:
        return (0,True)
    
    lHeight, l = isBalanced(n.left)
    rHeight, r = isBalanced(n.right)
    
    if abs( lHeight - rHeight ) > 1:
        return (0, False)
    
    return ( 1 + max( lHeight,rHeight  ) , l and r )

def isBalancedBST(root):
    if not isBST(root, -1000000000, 1000000000):
        print("BST voilated, inorder traversal :", end=' ')
    
    elif not isBalanced(root)[1]:
        print("Unbalanced BST, inorder traversal :", end=' ')
    
    else:
        return True
    
    return False

def printInorder(n):
    if not n:
        return
    printInorder(n.left)
    print(n.data, end=' ')
    printInorder(n.right)

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        ip = [ int(x) for x in input().strip().split() ]
        
        root = None
        
        for i in range(n):
            root = Solution().insertToAVL( root, ip[i] )
            
            if not isBalancedBST( root ):
                break
        
        printInorder(root)
        print()

# } Driver Code Ends