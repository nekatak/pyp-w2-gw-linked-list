from .interface import AbstractLinkedList
from .node import Node
import itertools

class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        self.elements=elements
        self.start=None
        self.end=None
        self.length=0
        self.node=None
        if elements != None:
            for item in elements:
                self.append(item)


    def __str__(self):
        str_list=[]
        #print("TEST!!!!")
        for node in self:
            #print("TEST!!!!")
            element=node.elem
            str_list.append(element)
        return str(str_list)

    def __len__(self):
        pass

    def __iter__(self):
        return self

    def next(self):
        return self.__next__()

    def __next__(self):
        if self.node:
            node=self.node
            self.node=node.next
            return node
        else:
            raise StopIteration()


    def __getitem__(self, index):
        pass

    def __add__(self, other):
        new_list = LinkedList()
        for elem in self:
            new_list.append(elem.elem)
        for node in other:
            new_list.append(node.elem)
        return new_list

    def __iadd__(self, other):
        if not other.start:
            return self
        for node in other:
            self.append(node.elem)
        return self

    def __eq__(self, other):
        for x, y in zip(self, other):
            if x.elem != y.elem and x.next != y.next:
                print (x.elem, y.elem)
                print (type(x.next), type(y.next))
                return False
        return True

    def __ne__(self, other):
        if len(self.elements)!=len (other.elements):
            return True
        return False

    def append(self, elem):
        self.length+=1
        node=Node(elem)
        if self.end != None:
            self.end.next=node
        if self.start is None:
            self.start=node
            self.node=node
        self.end=node

    def count(self):
        return self.length

    def pop(self, index=None):
        if not self.elements:
            raise IndexError()
        if index>=self.length:
            raise IndexError()

        if index == 0:
            self.length=self.length-1
            prev_start = self.start.elem
            self.start = self.start.next
            self.node=self.start
            #print ( self.start)
            return prev_start

        if index == None or index == self.length-1:
            if self.length==1:
                prev_el=self.start.elem
                self.length=0
                self.start=None
                self.end=None
                self.node=None
                return prev_el
            for node in self:
                if node.next.elem == self.end.elem:
                    self.length-=1
                    was_last=self.end.elem
                    self.end=node
                    self.end.next=None
                    print (str(self))
                    return was_last
        ij=0
        ancestor_node=None
        child_node=None
        for node in self:
            if ij==index-1:
                ancestor_node=node
                print(ancestor_node.elem)
            if ij==index:
                forret=node.elem
                child_node=node.next
                print (forret, child_node.elem)
            ij+=1
        self.length-=1
        if not ancestor_node:
            forret=self.start.next
            ancestor_node=self.start
            child_node=self.start.next.next
        ancestor_node.next=child_node
        return forret
