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

    @staticmethod
    def delete(root, key):
        if not root:
            return root

        if key < root.key:
            root.left = AVLTree.delete(root.left, key)
        elif key > root.key:
            root.right = AVLTree.delete(root.right, key)
        else:  
            if not root.left:  
                return root.right
            elif not root.right:
                return root.left
            
            temp = AVLTree.min_value_node(root.right)  
            root.key = temp.key  
            root.right = AVLTree.delete(root.right, temp.key)  

        root.height = 1 + max(AVLTree.get_height(root.left), AVLTree.get_height(root.right))
        
        balance = AVLTree.get_balance(root)

        if balance > 1 and AVLTree.get_balance(root.left) >= 0:
            return AVLTree.right_rotate(root)

        if balance < -1 and AVLTree.get_balance(root.right) <= 0:
            return AVLTree.left_rotate(root)

        if balance > 1 and AVLTree.get_balance(root.left) < 0:
            root.left = AVLTree.left_rotate(root.left)
            return AVLTree.right_rotate(root)

        if balance < -1 and AVLTree.get_balance(root.right) > 0:
            root.right = AVLTree.right_rotate(root.right)
            return AVLTree.left_rotate(root)

        return root

    @staticmethod
    def min_value_node(node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    @staticmethod
    def find(node, key):
        if not node or node.key == key:
            return node
        
        if key < node.key:
            return AVLTree.find(node.left, key)
        
        return AVLTree.find(node.right, key)

    @staticmethod
    def print_tree(node, level=0, prefix="Root: "):
        
        if node is not None:
            print(" " * (level * 4) + prefix + str(node.key))
            
            if node.right is not None: 
                AVLTree.print_tree(node.right, level + 1, prefix=" |- R: ")
            
            if node.left is not None: 
                AVLTree.print_tree(node.left, level + 1, prefix=" |- L: ")

class AVLTreeApp:
    def __init__(self):
        self.tree = AVLTree()
        self.root = None
        
    def run(self):
         for value in random.sample(range(1, 301), 100): 
             self.root = AVLTree.insert(self.root, value)
         
         while True:
             action = input("Выберите действие:\n1. Вставить узел\n2. Удалить узел\n3. Найти узел\n4. Вывести дерево\n5. Выход\n")
             
             if action == "1":
                 key = int(input("Введите значение для вставки: "))
                 self.root = AVLTree.insert(self.root, key)
                 print(f"Вставлено: {key}")
                 
             elif action == "2":
                 key = int(input("Введите значение для удаления: "))
                 self.root = AVLTree.delete(self.root, key)
                 print(f"Удалено: {key}")
                 
             elif action == "3":
                 key = int(input("Введите значение для поиска: "))
                 found_node = AVLTree.find(self.root, key)
                 
                 message = "Узел найден!" if found_node else "Узел не найден."
                 print(message)
                 
             elif action == "4":
                 print("Вывод дерева:")
                 self.tree.print_tree(self.root)
                 
             elif action == "5":
                 break
                
             else:
                 print("Пожалуйста, введите корректное действие.")

if __name__ == "__main__":
    app = AVLTreeApp()
    app.run()