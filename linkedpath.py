from cell import Cell

class LinkedPath:
    # Singly linked list to store the robot's memory (visited cells)
    class Node:
        def __init__(self, cell, next = None):
            self.cell = cell
            self.next = next
    
    def __init__(self):
        self.head = None
        self.size = 0
        
    def add_cell(self, cell):
        if not isinstance(cell, Cell):
            raise ValueError("must be a Cell")
        node = self.Node(cell, self.head)
        self.head = node
        self.size += 1

    def remove_last(self):
        if self.head is None:
            return None
        
        node = self.head
        self.head = node.next
        self.size -= 1
        return node.cell

    def show_path(self):
        path_detail = []
        curr = self.head

        while curr is not None:
            c = curr.cell
            show = str(c)
            path_detail.append(show)
            curr = curr.next

        return path_detail
