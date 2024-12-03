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

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = TreeNode(key)
        else:
            self._insert_recursively(self.root, key)

    def _insert_recursively(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_recursively(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_recursively(node.right, key)

    def dfs_pre_order(self, node):
         result = []
         
         def traverse(n):
             if n:
                 result.append(n.key)
                 traverse(n.left)
                 traverse(n.right)
         
         traverse(node)
         return result

    def dfs_in_order(self, node):
         result = []
         
         def traverse(n):
             if n:
                 traverse(n.left)
                 result.append(n.key)
                 traverse(n.right)
         
         traverse(node)
         return result

    def dfs_post_order(self, node):
         result = []
         
         def traverse(n):
             if n:
                 traverse(n.left)
                 traverse(n.right)
                 result.append(n.key)
         
         traverse(node)
         return result

    def bfs_traversal(self, root):
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

class BinaryTreeApp:
     def __init__(self):
          self.tree = BinaryTree()
        
     def measure_traversal_time(self, size):
          values_to_insert = random.sample(range(1, size + 1), size)
          for value in values_to_insert:
              self.tree.insert(value)

          times = {}

          start_time_pre_order = time.time()
          pre_order_result = self.tree.dfs_pre_order(self.tree.root)  
          times['Pre-order'] = time.time() - start_time_pre_order

          start_time_in_order = time.time()
          in_order_result = self.tree.dfs_in_order(self.tree.root)  
          times['In-order'] = time.time() - start_time_in_order

          start_time_post_order = time.time()
          post_order_result = self.tree.dfs_post_order(self.tree.root)  
          times['Post-order'] = time.time() - start_time_post_order

          start_time_bfs = time.time()
          bfs_result = self.tree.bfs_traversal(self.tree.root)  
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
     app= BinaryTreeApp()
     app.run()