from Node import Node

class Binary_tree:

    def __init__(self):
        """
        Initializes a Binary_tree object.
        The root node is set to None and an empty list is created to store the result of traversal methods.
        """
        self.root = None
        self.max_value=None
        
    
    def pre_order(self, root,result_list = None):
        """
        Performs a pre-order traversal on the binary tree and returns the result.
        Args:
            root (Node): The root node of the binary tree.
        Returns:
            list: The result of pre-order traversal as a list of node values.
        """
        if result_list is None:
            result_list = []
        if root is not None:
            result_list.append(root.value)  
        if root.left is not None:
            self.pre_order(root.left,result_list)
        if root.right is not None:
            self.pre_order(root.right,result_list)
        return result_list
    
    def in_order(self, root,result_list = None):
        """
        Performs an in-order traversal on the binary tree and returns the result.
        Args:
            root (Node): The root node of the binary tree.
        Returns:
            list: The result of in-order traversal as a list of node values.
        """
        if result_list is None:
            result_list = []
        if root.left is not None:
            self.in_order(root.left,result_list)
        if root is not None:
            result_list.append(root.value)  
        if root.right is not None:
            self.in_order(root.right,result_list)
        return result_list
    
    def post_order(self, root, result_list =None):
        """
        Performs a post-order traversal on the binary tree and returns the result.
        Args:
            root (Node): The root node of the binary tree.
        Returns:
            list: The result of post-order traversal as a list of node values.
        """
        if result_list is None:
            result_list = []    
        if root.left is not None:
            self.post_order(root.left,result_list)
        if root.right is not None:
            self.post_order(root.right,result_list)
        if root is not None:
            result_list.append(root.value)  
        return result_list
    
    # def maximum_value(self):
    #     """
    #     Returns the maximum value in the binary tree.
    #     Returns:
    #         int or None: The maximum value in the binary tree, or None if the tree is empty.
    #     """
    #     tree = self.in_order(self.root)
    #     if len(tree) > 0:
    #         return tree[-1]
    #     return None
    
    def maximum_value(self):
        if self.root is None:
            return None
        if self.max_value is None:
            self.max_value=self.root.value
        def find_max (root):
              if root.left: find_max(root.left)
              if root.right: find_max(root.right)
              if root.value > self.max_value:
                    self.max_value = root.value      
        find_max(self.root)
        return self.max_value
        

class Binary_Search_Tree(Binary_tree):
    def __init__(self):
        """
        Initializes a Binary_Search_Tree object.
        Inherits from the Binary_tree class.
        """
        super().__init__()

    def add(self, root, value):
        """
        Adds a node with the given value to the binary search tree.
        Args:
            root (Node): The root node of the binary search tree.
            value: The value to be added to the binary search tree.
        """
        if root is None:
            self.root = Node(value)
            return

        if root.value > value:
            if root.left is None:
                root.left = Node(value)
            else:
                self.add(root.left, value)

        elif root.value < value:
            if root.right is None:
                root.right = Node(value)
            else:
                self.add(root.right, value)


    def contain(self, root, value):
        """
        Checks if a value is present in the binary search tree.
        Args:
            root (Node): The root node of the binary search tree.
            value: The value to search for in the binary search tree.
        Returns:
            bool: True if the value is present, False otherwise.
        """
        if root is None:
            return False

        if root.value == value:
            return True

        if root.value > value:
            return self.contain(root.left, value)

        if root.value < value:
            return self.contain(root.right, value)

        return False
    
