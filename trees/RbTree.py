import random

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.color = 'red'  
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.NIL_LEAF = TreeNode(None)  
        self.NIL_LEAF.color = 'black'  
        self.root = self.NIL_LEAF  

    def insert(self, key):
        new_node = TreeNode(key)
        new_node.left = self.NIL_LEAF
        new_node.right = self.NIL_LEAF
        parent = None
        current = self.root
        
        while current != self.NIL_LEAF:
            parent = current
            if new_node.key < current.key:
                current = current.left
            else:
                current = current.right
                
        new_node.parent = parent
        
        if parent is None:
            self.root = new_node  
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node
            
        new_node.color = 'red'  
        self.fix_insert(new_node)  

    def fix_insert(self, node):
        while node != self.root and node.parent.color == 'red':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == 'red':  
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:  
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)  
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.right_rotate(node.parent.parent)  
            else:
                uncle = node.parent.parent.left
                if uncle.color == 'red':  
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:  
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)  
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.left_rotate(node.parent.parent)  
                    
        self.root.color = 'black'  

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        
        if y.left != self.NIL_LEAF:
            y.left.parent = x
            
        y.parent = x.parent
        
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
            
        y.left = x
        x.parent = y

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        
        if x.right != self.NIL_LEAF:
            x.right.parent = y
            
        x.parent = y.parent
        
        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
            
        x.right = y
        y.parent = x

    def find(self, key):
        return self._find(self.root, key)

    def _find(self, node, key):
        if node == self.NIL_LEAF or key == node.key:
            return node
        
        if key < node.key:
            return self._find(node.left, key)
        
        return self._find(node.right, key)

    def delete(self, key):
        z = self.find(key)
        
        if z == self.NIL_LEAF:
            print(f"Узел с ключом {key} не найден.")
            return
        
        original_color_y= z.color
        
        if z.left == self.NIL_LEAF:
            x= z.right 
            self.transplant(z, z.right)
        
        elif z.right == self.NIL_LEAF:
            x= z.left 
            self.transplant(z, z.left)
        
        else:
            y= self.min_value_node(z.right)
            original_color_y= y.color 
            x= y.right 
            
            if y.parent == z: 
                x.parent= y 
                
            else: 
                self.transplant(y, y.right) 
                y.right= z.right 
                y.right.parent= y 
                
            self.transplant(z, y) 
            y.left= z.left 
            y.left.parent= y 
            y.color= z.color 
        
        if original_color_y == 'black':
            self.fix_delete(x)

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v 
            
        elif u == u.parent.left:
            u.parent.left= v 
            
        else:
            u.parent.right= v 
        
        v.parent= u.parent 

    def fix_delete(self, x):
       while x !=self.root and x.color =='black':
           if x ==x.parent.left:  
               w=x.parent.right  
               if w.color =='red':  
                   w.color ='black'  
                   x.parent.color ='red'  
                   self.left_rotate(x.parent)  
                   w=x.parent.right  
               if w.left.color=='black' and w.right.color=='black':  
                   w.color ='red'  
                   x=x.parent  
               else:  
                   if w.right.color=='black':  
                       w.left.color='black'  
                       w.color='red'  
                       self.right_rotate(w)  
                       w=x.parent.right  
                   w.color=x.parent.color  
                   x.parent.color ='black'  
                   w.right.color ='black'  
                   self.left_rotate(x.parent)  
                   x=self.root  

           else: 
               w=x.parent.left 
               if w.color =='red': 
                   w.color ='black' 
                   x.parent.color ='red' 
                   self.right_rotate(x.parent) 
                   w=x.parent.left 

               if w.right.color=='black' and w.left.color=='black': 
                   w.color ='red' 
                   x=x.parent 

               else: 
                   if w.left.color=='black': 
                       w.right.color='black' 
                       w.color='red' 
                       self.left_rotate(w) 

                       w=x.parent.left 

                   w.color=x.parent.color 
                   x.parent.color ='black' 
                   w.left.color ='black' 
                   self.right_rotate(x.parent) 

                   x=self.root 

       x.color='black'

    def min_value_node(self, node):
       current=node 
       while current.left!=self.NIL_LEAF: 
           current=current.left 

       return current 

    def print_tree(self, node, level=0, prefix="Root: "):
       if node !=self.NIL_LEAF:
           print(" " * (level * 4) + prefix + str(node.key) + f" ({node.color})")
           if node.right !=self.NIL_LEAF:
               self.print_tree(node.right, level +1 , prefix=" |- R: ")
           if node.left !=self.NIL_LEAF:
               self.print_tree(node.left, level +1 , prefix=" |- L: ")

class RedBlackTreeApp:
    def __init__(self):
       self.tree=RedBlackTree()
       for value in random.sample(range(1, 301), 300): 
           self.tree.insert(value)

    def run(self):
       while True:
           action=input("Выберите действие:\n1. Вставить узел\n2. Удалить узел\n3. Найти узел\n4. Вывести дерево\n5. Выход\n")
           if action=="1":
               key=int(input("Введите значение для вставки: "))
               print(f"Вставлено: {key}")
               self.tree.insert(key)
           elif action=="2":
               key=int(input("Введите значение для удаления: "))
               print(f"Удалено: {key}")
               self.tree.delete(key)
           elif action=="3":
               key=int(input("Введите значение для поиска: "))
               found_node=self.tree.find(key)
               message="Узел найден!"if found_node!=self.tree.NIL_LEAF else"Узел не найден."
               print(message)
           elif action=="4":
               print("Вывод дерева:")
               self.tree.print_tree(self.tree.root)
           elif action=="5":
               break
           else:
               print("Пожалуйста, введите корректное действие.")

if __name__=="__main__":
   app=RedBlackTreeApp()
   app.run()