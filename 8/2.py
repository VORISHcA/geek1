"""
Задание 2.
Доработайте пример структуры "дерево",
рассмотренный на уроке.
Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).
Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""
class BinaryTreeErr(Exception):
    def __init__(self, error_text):
        self.error_text = error_text

class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    # добавить левого потомка
    def insert_left(self, new_node):
        # Защита от вставки неподходящего элемента в двоичное дерево
        if self.root <= new_node:
            raise BinaryTreeErr('Левый лист не может быть больше родителя')
        # если у узла нет левого потомка
        if self.left_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.left_child = BinaryTree(new_node)
        # если у узла есть левый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj

    # добавить правого потомка
    def insert_right(self, new_node):
        # Защита от вставки неподходящего элемента в двоичное дерево
        if self.root > new_node:
            raise BinaryTreeErr('Правый лист должен быть больше родителя')
        # если у узла нет правого потомка
        if self.right_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right_child = BinaryTree(new_node)
        # если у узла есть правый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.right_child = self.right_child
            self.right_child = tree_obj

    # метод доступа к правому потомку
    def get_right_child(self):
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        return self.left_child

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root


r = BinaryTree(8)
try:
    r.insert_left(40)
except BinaryTreeErr:
    print('Левый лист не может быть больше родителя')

try:
    r.insert_right(1)
except BinaryTreeErr:
    print('Правый лист должен быть больше родителя')

