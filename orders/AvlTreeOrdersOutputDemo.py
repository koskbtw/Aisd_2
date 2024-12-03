import random
import time
from collections import deque
import matplotlib.pyplot as plt
import numpy as np

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    @staticmethod
    def get_height(node):
        return node.height if node else 0

    @staticmethod
    def get_balance(node):
        return AVLTree.get_height(node.left) - AVLTree.get_height(node.right) if node else 0

    @staticmethod
    def right_rotate(y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2

        y.height = 1 + max(AVLTree.get_height(y.left), AVLTree.get_height(y.right))
        x.height = 1 + max(AVLTree.get_height(x.left), AVLTree.get_height(x.right))
        
        return x

    @staticmethod
    def left_rotate(x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2

        x.height = 1 + max(AVLTree.get_height(x.left), AVLTree.get_height(x.right))
        y.height = 1 + max(AVLTree.get_height(y.left), AVLTree.get_height(y.right))
        
        return y

    @staticmethod
    def insert(node, key):
        if not node:
            return TreeNode(key)

        if key < node.key:
            node.left = AVLTree.insert(node.left, key)
        else:
            node.right = AVLTree.insert(node.right, key)

        node.height = 1 + max(AVLTree.get_height(node.left), AVLTree.get_height(node.right))

        balance = AVLTree.get_balance(node)

        if balance > 1 and key < node.left.key:
            return AVLTree.right_rotate(node)

        if balance < -1 and key > node.right.key:
            return AVLTree.left_rotate(node)

        if balance > 1 and key > node.left.key:
            node.left = AVLTree.left_rotate(node.left)
            return AVLTree.right_rotate(node)

        if balance < -1 and key < node.right.key:
            node.right = AVLTree.right_rotate(node.right)
            return AVLTree.left_rotate(node)

        return node

    @staticmethod
    def dfs_pre_order(node):
         result = []
         
         def traverse(n):
             if n:
                 result.append(n.key)
                 traverse(n.left)
                 traverse(n.right)
         
         traverse(node)
         return result

    @staticmethod
    def dfs_in_order(node):
         result = []
         
         def traverse(n):
             if n:
                 traverse(n.left)
                 result.append(n.key)
                 traverse(n.right)
         
         traverse(node)
         return result

    @staticmethod
    def dfs_post_order(node):
         result = []
         
         def traverse(n):
             if n:
                 traverse(n.left)
                 traverse(n.right)
                 result.append(n.key)
         
         traverse(node)
         return result

    @staticmethod
    def bfs_traversal(root):
         result = []
         
         if not root:
             return result

         queue = deque([root])
         
         while queue:
             current = queue.popleft()
             result.append(current.key)  
             
             if current.left:
                 queue.append(current.left)
             if current.right:
                 queue.append(current.right)
         
         return result

class AVLTreeApp:
     def __init__(self):
          self.root = None
        
     def measure_traversal_time(self, size):
          values_to_insert = random.sample(range(1, size + 1), size)
          self.root = None  
          for value in values_to_insert:
              self.root = AVLTree.insert(self.root, value)

          times = {}

          start_time_pre_order = time.time()
          pre_order_result = AVLTree.dfs_pre_order(self.root)  
          times['Pre-order'] = time.time() - start_time_pre_order

          start_time_in_order = time.time()
          in_order_result = AVLTree.dfs_in_order(self.root)  
          times['In-order'] = time.time() - start_time_in_order

          start_time_post_order = time.time()
          post_order_result = AVLTree.dfs_post_order(self.root)  
          times['Post-order'] = time.time() - start_time_post_order

          start_time_bfs = time.time()
          bfs_result = AVLTree.bfs_traversal(self.root)  
          times['BFS'] = time.time() - start_time_bfs

          return times, pre_order_result, in_order_result, post_order_result, bfs_result

     def run(self):
          size = int(input("Введите размер дерева: "))
          
          search_times, pre_order_result, in_order_result, post_order_result, bfs_result = self.measure_traversal_time(size)

          print("\nВыберите метод обхода для вывода узлов:")
          print("1. Прямой обход (Pre-order)")
          print("2. Симметричный обход (In-order)")
          print("3. Обратный обход (Post-order)")
          print("4. Обход в ширину (BFS)")
          
          choice = input("Ваш выбор (введите номер): ")
          
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
     app = AVLTreeApp()
     app.run()