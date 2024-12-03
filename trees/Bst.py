import random

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
                                    
        return self.find(node.right, key)

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

    def print_tree(self, node, level=0, prefix="Root: "):
        if node is not None:
            print(" " * (level * 4) + prefix + str(node.key))

            if node.right is not None: 
                self.print_tree(node.right, level + 1, prefix=" |- R: ")

            if node.left is not None: 
                self.print_tree(node.left, level + 1, prefix=" |- L: ")

class BinarySearchTreeApp:
    def __init__(self):
        self.tree = BinarySearchTree()
        self.root = None
        
    def run(self):
         for value in random.sample(range(1, 301), 100):
             self.root = self.tree.insert(self.root, value)
         
         while True:
             action = input("Выберите действие:\n1. Вставить узел\n2. Удалить узел\n3. Найти узел\n4. Вывести дерево\n5. Выход\n")
             
             if action == "1":
                 key = int(input("Введите значение для вставки: "))
                 self.root = self.tree.insert(self.root, key)
                 print(f"Вставлено: {key}")
                 
             elif action == "2":
                 key = int(input("Введите значение для удаления: "))
                 self.root = self.tree.delete(self.root, key)
                 print(f"Удалено: {key}")
                 
             elif action == "3":
                 key = int(input("Введите значение для поиска: "))
                 found_node = self.tree.find(self.root, key)
                 
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
    app = BinarySearchTreeApp()
    app.run()