from Node import Node
class ListaMultiple:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def search_by_attr(self, attr, value):
        current = self.head
        while current:
            if getattr(current, attr) == value:
                return current
            current = current.next
        return None
    
    def update_value(self, search_value, **attrs):
        node = self.search_id(search_value)
        if node:
            for k, v in attrs.items():
                setattr(node, k, v)
            return True
        return False
    
    def delete_value(self, search_value):
        current = self.head
        while current:
            if current.id == search_value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return True
            current = current.next
        return False
    
    def print_multilinked_list(self, level=0):
        if self.head is None:
            print("Empty list"); return
        current = self.head
        while current:
            print("  " * level + str(current))
            if current.sub_list:
                current.sub_list.print_multilinked_list(level + 1)
            current = current.next

    def add_child(self, parent:Node, child:Node):
        if parent.sub_list is None:
            sublist = ListaMultiple()
            sublist.head = child
            sublist.tail = child
            parent.sub_list = sublist
        else:
            current = parent.sub_list.tail
            current.next = child
            child.prev = current
            parent.sub_list.tail = child
        return parent.sub_list
    
    def str__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return " <-> ".join(nodes)