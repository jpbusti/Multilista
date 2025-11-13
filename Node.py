class Node:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.next = None
        self.prev = None
        self.sub_list = None   # apunta a otra LinkedList

    def __repr__(self):
        return f"Node({self.name!r})"