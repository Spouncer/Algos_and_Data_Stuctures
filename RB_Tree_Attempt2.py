class Node:
    def __init__(self, item):
        self.item = item
        self.right = None
        self.left = None
        self.parent = None
        self.col = 1 # 1 is red, 0 is black
        
    def recolour(self, col):
        self.col = col
        
    def gp(self):
        if self.parent != None:
            return self.parent.parent
        else:
            return None

    def p(self):
        return self.parent

class RBTree:
    def __init__(self):
        self.root = None

    def RR_Violation(self):
        n = self.root
        
        def check_RR(n):
            if n == None:
                return False
            elif n.right == None and n.left == None:
                return False

            elif n.col == 1:

                if n.right != None and n.right.col == 1:
                    return True
                if n.left != None and n.left.col == 1:
                    return True
                else:
                    if check_RR(n.right) or check_RR(n.left):
                        return True
            else:
                if check_RR(n.right) or check_RR(n.left):
                    return True
                
                else:
                    return False
        
        return check_RR(n)

    def RB_depth_viol(self):
        n = self.root
        
        def count(n, depth):
            if n == None:
                return False, depth
            elif n.col == 0:
                depth += 1
                violr, depth_r = count(n.right, depth)
                violl, depth_l = count(n.left, depth)
                
                if violr == True or violl == True:
                    return True, 0
                elif depth_r == depth_l:
                    return False, depth_r
                else:
                    return True, 0

            else:
                violr, depth_r = count(n.right, depth)
                violl, depth_l = count(n.left, depth)
                if violr == True or violl == True:
                    return True, 0
                elif depth_r == depth_l:
                    return False, depth_r
                else:
                    return True, 0

        viol, depth = count(n, 0)
        return viol

    def isBinaryTree(self):
        pass

    def isRBTree(self):

        
        if self.root.col == 0:
            if self.RR_Violation() == False:
                if self.RB_depth_viol() == False:
                    return True
                else:
                    print('black depth prop violated')
                    return False
            else:
                print('RR prop violated')
                return False
        else:
            print('root prop violated')
            return False
    

    def right_rotate(node):
        pass

    def RB_insert(self, node):
        pass

    def left_rotate(self, node):
        x = node
        if node == self.root:
            if node != None:   
 
                y = x.right
                if y != None:
                    b = y.left 
                    y.parent = None
                    if b != None:
                        b.parent = x
                    x.right = b 
                    y.left = x
                    self.root = y
                    x.parent = y
                    

    
                    
        else:
        
            if node != None:    
                y = x.right
                if y != None:
                    b = y.left 
                    if node.parent.left == node:
                        x.parent.left = y
                        
                    elif node.parent.right == node:
                        x.parent.right = y

                    y.parent = x.parent
                    x.parent = y
                    if b != None:
                        b.parent = x
                    y.left = x
                    x.right = b
        
    def right_rotate(self, node):
        x = node
        if node == self.root:
            if node != None:    
                y = x.left
                if y != None:
                    b = y.right 
                    self.root = y

                    y.parent = x.parent
                    x.parent = y
                    if b != None:
                        b.parent = x
                    y.right = x
                    x.left = b 
        else:
            
            if node != None: 
                y = x.left
                if y != None:
                    b = y.right 
                
                    if node.parent.left == node:
                        x.parent.left = y
                        
                    elif node.parent.right == node:
                        x.parent.right = y

                    y.parent = x.parent
                    x.parent = y
                    if b != None:
                        b.parent = x

                    y.right = x
                    x.left = b

'''# Violates root property
test1 = RBTree()

en = Node(1)
en.col = 1
test1.root = en
print('root')
print(test1.isRBTree() == False)

# Simplest RB tree
test2 = RBTree()

to = Node(2)
to.col = 0
test2.root = to
print('simple true tree')
print(test2.isRBTree() == True)

# violates RR property
tre = Node(3)
fire = Node(4)
fem = Node(5)
nul = Node(0)
nul.col = 1
tre.col = 1
fire.col = 1
fem.col = 1

test3 = RBTree()
test3.root = to
to.right = fire
fire.right = fem
to.left = nul
print('RR Violation')
print(test3.isRBTree() == False)


# Violates black depth property
tre.col = 0
fire.col = 0 
fire.left = tre
print('black depth')
print(test3.isRBTree() == False)

# Fixed
nul.col = 0
fire.col = 1
fem.col = 0
print('fixed tree')
print(test3.isRBTree() == True)

# Black depth test
tuve = Node(20)
tred = Node(30)
nul = Node(0)
m_ti = Node(-10)
m_fem = Node(-5)
fem = Node(5)
ti = Node(10)
fyrre = Node(40)
halvf = Node(50)
femfem = Node(55)
firefem = Node(45)
trefem = Node(35)
tofem = Node(25)
femten = Node(15)
m_femten = Node(-15)

test4 = RBTree()
test4.root = tuve
tuve.col = 0

tuve.right = fyrre
fyrre.col = 1
tuve.left = nul
nul.col = 1 

fyrre.right = halvf
halvf.col = 0
fyrre.left = tred
tred.col = 0

nul.right = ti
ti.col = 0
nul.left = m_ti
m_ti.col = 0

m_ti.right = m_fem
m_fem.col = 0
m_ti.left = m_femten
m_femten.col = 0

ti.right = femten
femten.col = 0
ti.left = fem
fem.col = 0

tred.right = trefem
trefem.col = 1
tred.left = tofem
tofem.col = 1

halvf.right = femfem
femfem.col = 1
halvf.left = firefem
firefem.col = 1

print(test4.isRBTree() == False)
'''
# Left rotate test
t = RBTree()

p = Node('p')
x = Node('x')
y = Node('y')
a = Node('alpha')
b = Node('beta')
g = Node('gamma')

t.root = x
# p.left = x
# x.parent = p

x.left = a
a.parent = x

x.right = y
y.parent = x

y.right = g
g.parent = y

y.left = b
b.parent = y

t.left_rotate(x)

print(x.left.item,
a.parent.item,

x.right.item,
x.parent.item,
y.parent,

y.right.item,
g.parent.item,

y.left.item,
b.parent.item)

t.right_rotate(y)

# p.left.item,
# x.parent.item,
print(
x.left.item,
a.parent.item,

x.right.item,
y.parent.item,

y.right.item,
g.parent.item,

y.left.item,
b.parent.item)







