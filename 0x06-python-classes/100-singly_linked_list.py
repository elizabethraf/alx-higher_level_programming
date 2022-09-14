#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Node that defines a node of a singly linked list
Attributes:
    data (int): data stored in the node
    dat (int): next node in the linked list
"""


class Node:
    """Defines a node in a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a node.
        Args:
            data (int): The data stored in the node.
            next_node (node): next not linked  list
        return: None
        """
        self._data = data
        self.next_node = next_node

    @data.setter
    def data(self, data):
        """setter of _data.

        Args:
            value (int): the data stored in the node.

        return: None
        """
         if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def data(self):
        """getter of _data

        return (self.__data)

    @size.setter
    def size(self, value):
        """property setter of __size
        Args:
            vaue (int): The size of the new square
        return: None
        """
        self.__size = value

        if type(value) != int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")

    def my_print(self):
        """prints the square
        return: None
        """


   @property
    def next_node(self):
        """getter of __next_node.

        return: next node in the linked list
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter of __next_node.

        Args:
            value (Node): next node in the linked list
        return: None
        """
        if value != None and type(value) != Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """Define a single linked list

    Attributes:
        __head (Node): head of the linked list
    """

    def __init__(self):
        """Initializes the linked list
        return: None
        """
        self.__head = None
