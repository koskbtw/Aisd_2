import random
import matplotlib.pyplot as plt
import numpy as np

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def insert(self, node, key):

        if node is None:
            return TreeNode(key)

        if key < node.key:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)

        return node

    def find(self, node, key):

        if node is None or node.key == key:
            return node
        
        if key < node.key:
            return self.find(node.left, key)
        
        return self.find(node.right)

    def delete(self, root, key):

        if root is None:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else: 
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self.min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        return root

    def min_value_node(self, node):

        current = node
        while current.left is not None:
            current = current.left
        return current

    def height(self, node):

        if node is None:
            return 0
        else:
            left_height = self.height(node.left)
            right_height = self.height(node.right)
            return max(left_height, right_height) + 1


class BinarySearchTreeApp:
    def __init__(self):
        self.tree = BinarySearchTree()
        self.root = None
        
    def run(self):
         heights = []
         num_keys = []
         
         for i in range(1, 5001): 
             key = random.randint(1, 10000) 
             self.root = self.tree.insert(self.root, key)

             if i % 300 == 0:
                 heights.append(self.tree.height(self.root))
                 num_keys.append(i)

         plt.plot(num_keys, heights, 'o', label='Экспериментальные точки', color = "red")

         log_num_keys = np.log(num_keys)  
         coefficients = np.polyfit(log_num_keys, heights, 1) 
         polynomial = np.poly1d(coefficients)
         x_fit = np.linspace(min(log_num_keys), max(log_num_keys), 100)  
         y_fit = polynomial(x_fit)

         plt.plot(np.exp(x_fit), y_fit, label='Регрессионная кривая', color='purple')  
         plt.title("Зависимость высоты бинарного дерева поиска от количества ключей")
         plt.xlabel("Количество ключей(n)")
         plt.ylabel("Высота дерева(h)")
         plt.legend()
         plt.grid()
         plt.show()

         print("Уравнение регрессионной кривой:")
         print(f"y ≈ {coefficients[0]:.4f} * log(x) + {coefficients[1]:.4f}")

if __name__ == "__main__":
    app = BinarySearchTreeApp()
    app.run()