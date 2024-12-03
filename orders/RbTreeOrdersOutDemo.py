import random
import time
from collections import deque
import matplotlib.pyplot as plt
import numpy as np

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

    def dfs_pre_order(self, node):
         result = []
         
         def traverse(n):
             if n != self.NIL_LEAF:
                 result.append(n.key)
                 traverse(n.left)
                 traverse(n.right)
         
         traverse(node)
         return result

    def dfs_in_order(self, node):
         result = []
         
         def traverse(n):
             if n != self.NIL_LEAF:
                 traverse(n.left)
                 result.append(n.key)
                 traverse(n.right)
         
         traverse(node)
         return result

    def dfs_post_order(self, node):
         result = []
         
         def traverse(n):
             if n != self.NIL_LEAF:
                 traverse(n.left)
                 traverse(n.right)
                 result.append(n.key)
         
         traverse(node)
         return result

    def bfs_traversal(self, root):
         result = []
         
         if not root or root == self.NIL_LEAF:
             return result

         queue = deque([root])
         
         while queue:
             current = queue.popleft()
             result.append(current.key)  
             
             if current.left != self.NIL_LEAF:
                 queue.append(current.left)
             if current.right != self.NIL_LEAF:
                 queue.append(current.right)
         
         return result

class RedBlackTreeApp:
     def __init__(self):
          self.root = None
        
     def measure_traversal_time(self, size):
          values_to_insert = random.sample(range(1, size + 1), size)
          tree = RedBlackTree()
          for value in values_to_insert:
              tree.insert(value)

          times = {}

          start_time_pre_order = time.time()
          pre_order_result = tree.dfs_pre_order(tree.root)  
          times['Pre-order'] = time.time() - start_time_pre_order

          start_time_in_order = time.time()
          in_order_result = tree.dfs_in_order(tree.root)  
          times['In-order'] = time.time() - start_time_in_order

          start_time_post_order = time.time()
          post_order_result = tree.dfs_post_order(tree.root)  
          times['Post-order'] = time.time() - start_time_post_order

          start_time_bfs = time.time()
          bfs_result = tree.bfs_traversal(tree.root)  
          times['BFS'] = time.time() - start_time_bfs

          return times, pre_order_result, in_order_result, post_order_result, bfs_result

     def run(self):
          size = int(input("Введите размер дерева: "))
          
          search_times, pre_order_result, in_order_result, post_order_result, bfs_result= self.measure_traversal_time(size)

          print("\nВыберите метод обхода для вывода узлов:")
          print("1. Прямой обход (Pre-order)")
          print("2. Симметричный обход (In-order)")
          print("3. Обратный обход (Post-order)")
          print("4. Обход в ширину (BFS)")
          
          choice= input("Ваш выбор (введите номер): ")
          
          if choice == "1":
              print("Узлы в порядке Pre-order:", pre_order_result)
          elif choice == "2":
              print("Узлы в порядке In-order:", in_order_result)
          elif choice == "3":
              print("Узлы в порядке Post-order:", post_order_result)
          elif choice == "4":
              print("Узлы в порядке BFS:", bfs_result)
          else:
              print("Неверный выбор.")

if __name__ == "__main__":
     app= RedBlackTreeApp()
     app.run()