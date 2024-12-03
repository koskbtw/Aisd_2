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

    def height(self, node):
        """Возвращает высоту дерева."""
        if node == self.NIL_LEAF:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

class RedBlackTreeApp:
    def __init__(self):
        self.tree=RedBlackTree()

    def run(self):
         heights = []
         num_keys = []
         
         for i in range(1, 10001):  
             key = i  
             self.tree.insert(key)

             if i % 600 == 0:  
                 heights.append(self.tree.height(self.tree.root))
                 num_keys.append(i)

         plt.plot(num_keys, heights, 'o', label='Экспериментальные точки', color = 'red')  

         log_num_keys = np.log(num_keys)  
         coefficients = np.polyfit(log_num_keys, heights, 1)  
         polynomial_func = np.poly1d(coefficients)
         x_fit = np.linspace(min(log_num_keys), max(log_num_keys), 100)  
         y_fit = polynomial_func(x_fit)

         plt.plot(np.exp(x_fit), y_fit, label='Регрессионная кривая', color='purple')  

         upper_bound_heights = [2 * np.log2(n + 1) for n in num_keys]
         plt.plot(num_keys, upper_bound_heights, label='Верхняя граница: 2 * log2(n + 1)', color='#f5c1c1', linestyle='--')

         plt.title("Зависимость высоты красно-черного дерева от количества ключей")
         plt.xlabel("Количество ключей")
         plt.ylabel("Высота дерева")
         plt.legend()
         plt.grid()
         plt.show()

         print("Уравнение регрессионной кривой:")
         print(f"y ≈ {coefficients[0]:.4f} * log(x) + {coefficients[1]:.4f}")

if __name__ == "__main__":
    app=RedBlackTreeApp()
    app.run()