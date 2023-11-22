#!/usr/bin/python3
"""Write a class Node that defines a node of a singly linked list by:"""


class Node:
    """class Node that defines a node of a singly linked list"""
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class SinglyLinkedList:
    """class SinglyLinkedList that defines a singly linked list"""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        newNode = Node(value)
        if not self.__head or self.__head.data >= value:
            newNode.next_node = self.__head
            self.__head = newNode
            return
        temp = self.__head
        while temp.next_node and temp.next_node.data < value:
            temp = temp.next_node
        newNode.next_node = temp.next_node
        temp.next_node = newNode

    def __str__(self):
        sll = ""
        temp = self.__head
        while temp:
            sll += str(temp.data)
            if temp.next_node:
                sll += "\n"
            temp = temp.next_node
        return sll
