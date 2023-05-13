class Node:
    def __init__(self, p=[0, 0], id=0, id_parent=0):
        self.p = p                  # node XY-position
        self.id = id                # node id
        self.id_parent = id_parent  # node parent's id