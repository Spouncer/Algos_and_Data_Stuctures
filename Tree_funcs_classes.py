from sympy import N


class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.item = item

    def isleaf(self):
        return self.left == None and self.right == None
        
class RB_Node(Node):
    def __init__(self, item):
        super().__init__(item)
        self.colour = None
        self.parent = None

    def get_parent_value(self):
        if self.parent == None:
            print('this is the root')
        else:
            return self.parent.item
    
    def recolour(self):
        if self.colour == 'R':
            self.colour = 'B'
        elif self.colour == 'B':
            self.colour = 'R'

    def isshape(self):
        p = self.parent
        gp = p.parent
        if p.left == self and gp.right == p:
            return 'T', 'r'
        elif p.right == self and gp.left == p:
            return 'T', 'l'

        elif p.left == self and gp.left == p:
            return 'L', 'l'

        elif p.right == self and gp.right == p:
            return 'L', 'r'
         
class Tree:
    def __init__(self, name, root):
        self.root = root
        self.name = name

    def DFS_search(self, value):
        ''' In-order traversal.'''
        node = self.root
        print("sim is cool")
        found = 0

        # Switch around the order to do pre-order or post-order traversal
        if found == 0:    
            if node.left != None:
                t_left = Tree("t1", node.left)
                f1 = t_left.DFS_search(value)
                found += f1

        if found == 0:   
            print(node.item)
            if value == node.item:
                found += 1

        if found == 0:  
            if node.right != None:
                t_right = Tree("t2", node.right)
                f2 = t_right.DFS_search(value)
                
                found += f2
            
        return found

    def BFS_Search(self, value, d):
        found = 0
        node = self.root
        layer = [node]
        
        if node == None:
            return found
        else:
            values = [node.item]
            print(values)
            if value == node.item:
                
                found += 1 

            while found == 0:
                d += 1
                next_layer = []
                next_values = []
                for i in layer:
                    
                    if i.left != None:
                        next_values.append(i.left.item)
                        if value == i.left.item:
                            found +=1 
                            print(f'The node {value} is in the tree, at depth {d}.')
                            break
                        else:
                            next_layer.append(i.left)
                            
                        
                    if i.right != None:
                        next_values.append(i.right.item)
                        if value == i.right.item:
                            found += 1
                            print(f'The node {value} is in the tree, at depth {d}.')
                            break
                        else:
                            next_layer.append(i.right)
                            
                
                values = next_values
                layer = next_layer

                if len(layer) == 0:
                    break
                print(values)

                
        return found
            
class BinaryTree(Tree):
    def __init__ (self, name, root):
        super().__init__(name, root)
    

    def add_node(self, obj):
        node = self.root
        if node == None:
            self.root = obj
            
        else:
            while True:
                if obj.item == node.item:
                    print(f'The node {obj.item} is already in the tree.')
                    break
                elif obj.item > node.item:
                    
                    if node.right == None:
                        node.right = obj
                        
                        break
                    else:
                        node = node.right

                else:
                    
                    if node.left == None:
                        node.left = obj
                        
                        break
                    else:
                        node = node.left
        return node

    def min_node(self, root):
        node = root
        if node != None:
            node = root
            while node.left != None:
                node = node.left
            return node
        else:
            return None

    def max_node(self, root):
        if root != None:
            node = root
            while node.right != None:
                node = node.right
            return node
        else:
            return None


    def binary_search(self, value):
        node = self.root
        found = 0
        if node == None:
            print('This tree is empty.')
        else:
            while found == 0:
                print(node.item)
                if value == node.item:
                    print(f'The node {value} is in the tree.')
                    found += 1
                    break
                    
                elif value > node.item:
                    
                    if node.right == None:
                        print(f'The tree {self.name} does not have node {value}.')
                        break
                    else:
                        node = node.right

                else:
                    
                    if node.left == None:
                        print(f'The tree {self.name} does not have node {value}.')
                        
                        break
                    else:
                        node = node.left
            return bool(found)

    def print_children(self, node):
        print(node.item, node.colour)
        if node.left != None and node.right != None:
            print([node.left.item, node.right.item])
        elif node.left != None:
            print([node.left.item])
        elif node.right != None:
            print([node.right.item])
        else:
            print([])


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
                
class RB_Tree(BinaryTree):
    def __init__(self, name, root):
        super().__init__(name, root)

    def RR_Violation(self):
        n = self.root
        
        def check_RR(n):
            if n == None:
                return False
            elif n.right == None and n.left == None:
                return False

            elif n.colour == 'R':

                if n.right != None and n.right.colour == 'R':
                    return True
                if n.left != None and n.left.colour == 'R':
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
            elif n.colour == 'B':
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

    def isRBTree(self):

        if self.root.colour == 'B':
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

    # def fix_node(self, node):
    #     if self.root != node:

    #             while node.parent != None and node.parent.colour != 'R': 
    #                 print(1)
    #                 if node.parent.parent != None:
    #                     grandparent = node.parent.parent

    #                     if grandparent.left == node.parent:
    #                         uncle = grandparent.right
    #                     elif grandparent.right == node.parent:
    #                         uncle = grandparent.left

    #                     if uncle == None:
    #                         col = 'B'
    #                     elif uncle.colour == 'B':
    #                         col = 'B'
    #                     elif uncle.colour == 'R':
    #                         col = 'R'

    #                     if col == 'B':    
    #                         tf, lr = node.isshape()
    #                         if tf == 'T':
    #                             if lr == 'l':
    #                                 node.parent.left_rotate()
    #                             elif lr == 'r':
    #                                 node.parent.right_rotate()

    #                         elif tf == 'L':
    #                             if lr == 'r':
    #                                 grandparent.left_rotate()
    #                             elif lr == 'l':
    #                                 grandparent.right_rotate()
    #                             grandparent.recolour()
    #                             node.parent.recolour()
                            

    #                     elif col == 'R':
    #                         node.parent.recolour()
    #                         grandparent.recolour()
    #                         if uncle != None:
    #                             uncle.recolour()
    #                         node = grandparent

                                    
    #     elif node.colour == 'R':
    #         node.recolour()

    def fix_node(self, node):
        print('new')
        p = node.parent
        
        while p != None and p.parent != None and p.colour == 'R':
            
            if p == p.parent.left:
                print('A')
                u = p.parent.right
                if p.parent != None and u != None and u.colour == 'R':
                    print('B')
                    u.colour = 'B'
                    p.colour = 'B'
                    p.parent.colour = 'R'
                    node = p.parent
                    p = node.parent
                else:
                    if node == p.right:
                        print('C')
                        node = p
                        self.left_rotate(node)
                        
                
                    print('D')
                    p.colour = 'B'
                    p.parent.colour = 'R'
                    self.right_rotate(p.parent)

                
            elif p == p.parent.right:
                print('E')
                u = p.parent.left
                if u != None and p.parent.left.colour == 'R':
                    print('F')
                    p.colour = 'B'
                    u.colour = 'B'
                    p.parent.colour = 'R'
                    node = p.parent
                    p = node.parent

                else:
                    if p.left == node:
                        print('G')
                        node = p
                        self.right_rotate(node)
                    p.colour = 'B'
                    p.parent.colour = 'R'
                    
                    self.left_rotate(p.parent)
            if node == self.root:
                break
                
        self.root.colour = 'B'
        

    '''def fix_node(self, node):
        print('new')
        count = 0
        while node.parent != None and node.parent.colour == 'R' and node != self.root and count < 6:
            count += 1
            print('A')
            if node.parent != None and node.parent.parent != None:
                grandparent = node.parent.parent     
                if grandparent.left == node.parent:
                    uncle = grandparent.right
                elif grandparent.right == node.parent:
                    uncle = grandparent.left

                if uncle == None:
                    col = 'B'
                elif uncle.colour == 'B':
                    col = 'B'
                elif uncle.colour == 'R':
                    col = 'R'

                if col == 'R':
                    print('B')
                    uncle.colour = 'B'
                    node.parent.colour = 'B'
                    grandparent.colour = 'R'
                    node = grandparent
                    if grandparent == None:
                        break

                elif col == 'B':
                    print('C')
                    if grandparent.parent != None:
                        print('D')
                        
                    tl, lr = node.isshape()
                    if tl == 'L':
                        if lr == 'l':
                            print('E')
                            self.right_rotate(grandparent)
                            
                        else:
                            print('F')
                            self.left_rotate(grandparent)
                        node.parent.recolour()
                        grandparent.recolour()
                        break
                    elif tl == 'T':
                        if lr == 'l':
                            print('G')
                            p = node.parent
                            self.left_rotate(node.parent)
                            node = p
                            self.left_rotate(grandparent)
                            node.parent.recolour()
                            grandparent.recolour()
                            break
                        else:
                            print('H')
                            p = node.parent
                            self.right_rotate(node.parent)
                            node = p
                            self.right_rotate(grandparent)
                            node.parent.recolour()
                            grandparent.recolour()
                            break 

        if node == self.root:
            node.colour = 'B'    '''  

    def transplant(self, node1, node2):
        x = node1
        y = node2
        if y == None and x == None:
            pass
        elif y == None:
            if x.parent.left == y:
                x.parent.left = None
                
            else:
                x.parent.right = None
            x.parent = None

        elif x == None:
            if y.parent.left == y:
                y.parent.left = None
                
            else:
                y.parent.right = None
            y.parent = None
            
        else:
            xp = x.parent
            yp = y.parent
            xrc = x.right
            xlc = x.left
            yrc = y.right
            ylc = y.left

            node1.parent = yp
            node2.parent = xp
            node1.right = yrc
            node1.left = ylc
            node2.right = xrc
            node2.left = xlc

                        

    def RB_insert_node(self, node):
        parent = self.add_node(node)
        node.parent = parent
        node.colour = 'R'
        self.fix_node(node)

    def RB_delete_fix(self, x):
        
        while self.root.item != x.item and x.colour == 'B':
            if x.parent.left == x:
                w = x.parent.right
                if w != None and w.colour == 'R':
                    print('CASE I')
                    w.recolour()
                    x.parent.colour = 'R'
                    
                    self.left_rotate(x.parent)
                    w = x.parent.right

                if w != None:
                    if w.left != None and w.right != None:
                        if w.left.colour == 'B' and w.right.colour == 'B':
                            v = True
                        else:
                            v = False
                    else:
                        if w.left != None and w.left.colour == 'B' and w.right == None:
                                v = True

                        elif w.left == None and w.right != None and w.right.colour == 'B':
                            v = True
                        else:
                            v = False
        
                if w != None and v == True:
                        print('CASE II')
                        if w != None:
                
                            w.colour = 'R'
                        x = x.parent
        
                else:
                    if w != None and w.right == None:
                        print('CASE III')
                        w.left.colour = 'B'
                        w.colour = 'R'
                        
                        self.right_rotate(w)
                        w = x.parent.right
                    elif w != None and w.right.colour == 'B':
                        print('CASE III')
                        w.left.colour = 'B'
                        w.colour = 'R'
                        
                        self.right_rotate(w)
                        w = x.parent.right
                    
                    
                    if w != None:
                        w.colour = x.parent.colour
                        w.right.colour = 'B'
                    x.parent.colour = 'B'
                
                    self.left_rotate(x.parent)
                    print('CASE IV')
                    if x.item == None:
                        if x.parent.left == x:
                            x.parent.left = None

                        if x.parent.right == x:
                            x.parent.right = None

                    x = self.root
                    break

            else:
                w = x.parent.left
                if w.colour == 'R':
                    print('Case I')
                    w.recolour()
                    x.parent.colour = 'R'
                    
                    self.right_rotate(x.parent)
                    w = x.parent.left

                if (w.right == None or w.right.colour == 'B'): 
                    if ( w.left == None or w.left.colour == 'B'):
                        print('Case II')
                        w.colour = 'R'
                        x = x.parent
                else:
                    if  w.left == 'B':
                        print('Case III')
                        w.right.colour = 'B'
                        w.colour = 'R'
                        
                        self.left_rotate(w)
                        w = x.parent.left
                
                    print('Case IV')
                    if x.parent != None:
                        w.colour = x.parent.colour
                        x.parent.colour = 'B'
                        if x.parent.parent != None:
                            x.parent.parent.colour = 'B'
                    if w.left != None:
                        w.left.colour = 'B'
                    
                    if x.parent != None:
                        self.right_rotate(x.parent)

                    if x.item == None:
                        if x.parent.left == x:
                            x.parent.left = None

                        if x.parent.right == x:
                            x.parent.right = None
                            
                    x = self.root
                    break

        x.colour = 'B'       

              
    def RB_delete_node(self, node):
        origicol = node.colour
        print(node.left.item)
        if node.left == None:
            print('A')
            x = node.right
            if x != None:
                x.parent = node.parent

            node.right = None
            if node.parent.left == node:
                node.parent.left = x
                child = 'l'
            elif node.parent.right == node:
                node.parent.right = x
                child = 'r'

            if node.parent != None:
                xp = node.parent
                
            
        elif node.right == None:
            print('B')
            x = node.left
            if x != None:
                x.parent = node.parent
            node.left = None
            if node.parent.left == node:
                node.parent.left = x
                child = 'l'
            elif node.parent.right == node:
                node.parent.right = x
                child = 'r'

            if node.parent != None:
                xp = node.parent

        else:
            print('C')
            y = self.min_node(node.right)
            origicol = y.colour
            x = y.right
            self.print_children(y) 
            print('a')
            if y.parent == node:
                print('D')
                if x != None:
                    print('E')
                    x.parent = y

                else:
                    print('F')
                    y.parent = node.parent
                xp = y
                child = 'r'
    
            else:
                print('G')
                if y.right == None:
                    n = Node(None)
                    n.colour = 'B'
                    n.parent = y
                    y.right = n

                if y.parent != None:
                    if y == y.parent.left:
                        y.parent.left = y.right
                    else:
                        y.parent.right = y.right
                
                    y.right.parent = y.parent
                    y.parent = y.right
                    
                self.print_children(y) 
                print('b')
                y.right = node.right
                y.parent.parent = y
            self.print_children(y) 
            print('c')
            
            y.left = node.left
            node.left.parent = y
            print(f'find None?, {y.right.item}')
            if y.right.left.item == None:
                y.right.left = None
            y.right = node.right
            node.left = None
            node.right = None
            if node.parent.left == node:
                node.parent.left = y
            if node.parent.right == node:
                node.parent.right = y

            node.parent = None
            self.print_children(y) 
            print('d')

            if y.left != None:
                print('H')
                y.left.parent = y
            y.colour = node.colour
            self.print_children(y) 
            print('e')
        if origicol == 'B' and x != None:
            print('I')
            print(f'x = {x.item}')
            self.RB_delete_fix(x)

        if origicol == 'B' and x == None:
            print('J')
            x = Node(None)
            x.parent = xp
            x.colour = 'B'
            if child == 'l':
                xp.left = x
            if child == 'r':
                xp.right = x
            print(f'x = {x.item}, xp = {xp.item}')
            self.RB_delete_fix(x)
            

nul, en, to, tre, fire, fem, seks = RB_Node(0), RB_Node(1), RB_Node(2), RB_Node(3), RB_Node(4), RB_Node(5), RB_Node(6)
syv, otte, ni, ti, elleve, tolve =  RB_Node(7), RB_Node(8), RB_Node(9), RB_Node(10), RB_Node(11), RB_Node(12)
nifem = RB_Node(9.5)



