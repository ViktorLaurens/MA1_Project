class Tree:
    def __init__(self, start_node, tree_id=0, tree_list=[]):
        self.start_node = start_node
        self.tree_id = tree_id
        self.tree_list = tree_list
        self.trees_connected = 0
        self.tree_length = 0
        self.tree_priority = 0
        self.extension_d = 0.2
