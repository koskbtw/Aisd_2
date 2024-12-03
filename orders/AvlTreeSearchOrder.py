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
        
     def measure_search_time(self, size):
          values_to_insert = random.sample(range(1, size + 1), size)
          self.root = None  
          for value in values_to_insert:
              self.root = AVLTree.insert(self.root, value)

          search_key = random.choice(values_to_insert)

          times = {}

          start_time_pre_order = time.time()
          found_node_pre_order = AVLTree.dfs_pre_order(self.root)  
          times['Pre-order'] = time.time() - start_time_pre_order

          start_time_in_order = time.time()
          found_node_in_order = AVLTree.dfs_in_order(self.root)  
          times['In-order'] = time.time() - start_time_in_order

          start_time_post_order = time.time()
          found_node_post_order = AVLTree.dfs_post_order(self.root)  
          times['Post-order'] = time.time() - start_time_post_order

          start_time_bfs = time.time()
          found_node_bfs = AVLTree.bfs_traversal(self.root)  
          times['BFS'] = time.time() - start_time_bfs

          return times

     def run(self):
          sizes = [1000, 5000, 10000, 20000, 50000]  
          
          results_preorder, results_inorder, results_postorder, results_bfs= [], [], [], []

          for size in sizes:
              search_times = self.measure_search_time(size)
              results_preorder.append(search_times['Pre-order'])
              results_inorder.append(search_times['In-order'])
              results_postorder.append(search_times['Post-order'])
              results_bfs.append(search_times['BFS'])

          plt.figure(figsize=(14, 8))

          for times, label in zip(
              [results_preorder, results_inorder, results_postorder, results_bfs],
              ['Pre-order', 'In-order', 'Post-order', 'BFS']):
              
              log_sizes = np.log(sizes)  
              coeffs = np.polyfit(log_sizes[1:], times[1:], deg=1)  
              regression_line_x_values = np.linspace(min(sizes), max(sizes), num=100) 
              regression_line_y_values = np.exp(coeffs[0] * np.log(regression_line_x_values) + coeffs[1])  

              plt.plot(regression_line_x_values, regression_line_y_values, linestyle='--', label=f'{label} Regression')

              print(f"{label} Regression: y ≈ {coeffs[0]:.6f} * ln(x) + {coeffs[1]:.6f}")

          plt.title('Логарифмическая регрессия времени выполнения поиска по методам обхода')
          plt.xlabel('Размер дерева')
          plt.ylabel('Время (секунды)')
          plt.legend()
          plt.grid(True)

          plt.savefig('search_time_regression.png')  
          plt.show()  

if __name__ == "__main__":
     app = AVLTreeApp()
     app.run()