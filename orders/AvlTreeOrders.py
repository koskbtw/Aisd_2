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
        if not node:
            return 0
        return node.height

    @staticmethod
    def get_balance(node):
        if not node:
            return 0
        return AVLTree.get_height(node.left) - AVLTree.get_height(node.right)

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
          AVLTree.dfs_pre_order(self.root)
          times['Pre-order'] = time.time() - start_time_pre_order

          start_time_in_order = time.time()
          AVLTree.dfs_in_order(self.root)
          times['In-order'] = time.time() - start_time_in_order

          start_time_post_order = time.time()
          AVLTree.dfs_post_order(self.root)
          times['Post-order'] = time.time() - start_time_post_order
          start_time_bfs = time.time()
          AVLTree.bfs_traversal(self.root)
          times['BFS'] = time.time() - start_time_bfs
          return times

     def run(self):
          sizes = [1000, 5000, 10000, 20000, 50000]  
          results = {size: self.measure_traversal_time(size) for size in sizes}

          pre_order_times = [results[size]['Pre-order'] for size in sizes]
          in_order_times = [results[size]['In-order'] for size in sizes]
          post_order_times = [results[size]['Post-order'] for size in sizes]
          bfs_times = [results[size]['BFS'] for size in sizes]

          plt.figure(figsize=(12, 6))

          for times, label in zip([pre_order_times, in_order_times, post_order_times, bfs_times], 
                                   ['Pre-order', 'In-order', 'Post-order', 'BFS']):
              log_sizes = np.log(sizes)  
              coeffs = np.polyfit(log_sizes, times, deg=1)  
              regression_line = np.exp(coeffs[0] * log_sizes + coeffs[1])  
              plt.plot(sizes, regression_line, linestyle='--', label=f'{label} Regression')

              print(f"{label} Regression: y ≈ {coeffs[0]:.6f} * ln(x) + {coeffs[1]:.6f}")

          plt.title('Логарифмическая регрессия времени выполнения обходов в зависимости от размера дерева')
          plt.xlabel('Размер дерева')
          plt.ylabel('Время (секунды)')
          plt.legend()
          plt.grid(True)
          plt.savefig('tree_traversal_regression.png')  
          plt.show()  

if __name__ == "__main__":
     app = AVLTreeApp()
     app.run()