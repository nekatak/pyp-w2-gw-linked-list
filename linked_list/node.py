class Node(object):
    """
    Node class representing each of the linked nodes in the list.
    """

    def __init__(self, elem, next=None):
        self.elem=elem
        self.next=next

    def __str__(self):
        return "{}".format(self.elem)

    def __eq__(self, other):
        if self.elem==other.elem:
            return True
        return False
        
    def __ne__(self, other):
        if self == other:
            return False
        return True

    def __repr__(self):
        return self
