import matplotlib.pyplot as plt
import numpy as np
import random

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

def main():
    avl_tree = AVLTree()
    root = None
    
    heights = []
    num_keys = []

    keys = random.sample(range(1, 10001), 10000) 
    
    for i in range(len(keys)): 
        root = AVLTree.insert(root, keys[i])

        if (i + 1) % 600 == 0:
            heights.append(AVLTree.get_height(root))
            num_keys.append(i + 1)

    plt.plot(num_keys, heights, 'o', label='Экспериментальные точки') 

    log_num_keys = np.log(num_keys)
    coefficients = np.polyfit(log_num_keys, heights, 1)
    polynomial = np.poly1d(coefficients)
    
    x_fit = np.linspace(min(log_num_keys), max(log_num_keys), 100)
    y_fit = polynomial(x_fit)

    plt.plot(np.exp(x_fit), y_fit, label='Регрессионная кривая', color='red')  

    upper_bound_heights = [1.44 * np.log2(n) - 1.5 for n in num_keys]
    plt.plot(num_keys, upper_bound_heights, label='Верхняя граница: 1.44 * log(n) - 1.5', color='green', linestyle='--')

    plt.title("Зависимость высоты AVL-дерева от количества ключей")
    plt.xlabel("Количество ключей")
    plt.ylabel("Высота дерева")
    plt.legend()
    plt.grid()
    plt.show()

    print(f"y ≈ {coefficients[0]:.4f} * log(x) + {coefficients[1]:.4f}")

if __name__ == "__main__":
    main()