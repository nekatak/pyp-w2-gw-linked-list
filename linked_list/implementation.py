from .interface import AbstractLinkedList
from .node import Node

class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """
    
    def __init__(self, elements=None):
        self.start = None
        self.end = None
        self.elements = elements
        if self.elements is not None:
            for elem in self.elements:
                self.append(elem)
            
    
    def __str__(self):
        if not self.start:
            return "[]"
        str_list='['
        for node in self:
            str_list+=str(node)
            if node != self.end.elem:
                str_list +=', '
        str_list+=']'
        return str_list

    def __len__(self):
        return self.count()


    def __iter__(self):
        if self.start is None:
            yield None
            raise StopIteration
        node = None
        while True:
            if node is None:
                node = self.start
            yield node.elem
            node = node.next
            if node is None:
                raise StopIteration
        
    def __getitem__(self, index):
        counter = 0
        for node in self:
            if counter == index:
                return node
            counter += 1

    def __add__(self, other):
        for node in other:
            self.append(node)
        return self
        

    def __iadd__(self, other):
        for node in other:
            self.append(node)
        return self


    def __ne__(self, other):
        if self.count() != other.count():
            return True
        for x, y in zip(self, other):
            if x!=y:
                return True
        return False

    def __eq__(self, other):
        if not self.start and not other.start:
            return True
        if self.count() != other.count():
            return False
        for x, y in zip(self, other):
            if x!=y:
                return False
        return True


    def append(self, elem):
        node = Node(elem)
        if self.start is None:
            self.start = node
        if self.end is None:
            self.end = node
            return
        
        self.end.next = node
        self.end = node

        
    def count(self):
        i = 0
        for x in self:
            if x is None:
                return 0
            i += 1
        return i


    def pop(self, index=None):
        if self.start is None:
            raise IndexError
        if index > self.count() -1:
            raise IndexError
        if index is None or index == self.count() - 1:
            prev_end = self.end.elem
            prev_start = self.start.elem
            for x in self:
                if x == prev_end and x == prev_start:
                    self.end = None
                    self.start = None
                    return prev_end
                if x == prev_end:
                    return prev_end
                node = Node(x)
                if x == prev_start:
                    self.start = node
                self.end.next = node
                self.end = node
        if index == 0:
            prev_start = self.start.elem
            self.start = self.start.next
            return prev_start
        counter = 0
        prev_node = None
        for x in self:
            if counter == index:
                return_val = prev_node.next.elem
                prev_node.next = prev_node.next.next
                return return_val
            counter +=1
            if not prev_node:
                prev_node = self.start
                continue
            prev_node = prev_node.next