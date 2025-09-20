import random

class Node:
    def __init__(self, value: int) -> None:
        self.left = None
        self.right = None
        self.value = value

def insert(root: Node, value: int) -> Node:
    '''
    insert value into the BST (duplicates go to the right)
        Arg:
            root: Node - the root of the BST
            value: int - the value to be inserted
        Returns:
            Node - the root of the modified BST
    '''
    if root is None:
        return Node(value)
    else:
        if value < root.value:
            root.left = insert(root.left, value)
        else:
            root.right = insert(root.right, value)
    return root


def find_minimum(root: Node) -> int:
    '''
    Find the minimum value in a binary search tree.
        Arg:
            root: Node - the root of the BST
        Returns:
            int - the minimum value in the BST
    '''
    if root is None:
        raise ValueError("The tree is empty")
    current = root
    while current.left is not None:
        current = current.left
    return current.value

def print_tree(node: Node, prefix: str = "", is_left: bool = True):
    '''
    Print the binary tree in a structured way.
        Arg:
            node: Node - the root of the tree
            prefix: str - the prefix for the current node
            is_left: bool - whether the current node is a left child
    '''
    BLUE = "\033[34m"
    RESET = "\033[0m"
    if node is not None:
        #print the current node
        value_str = f"{BLUE}{node.value}{RESET}"
        print(prefix + ("├── " if is_left else "└── ") + value_str)
        # recur on the left and right children
        if node.left or node.right:
            if node.left:
                print_tree(node.left, prefix + ("│   " if is_left else "    "), True)
            if node.right:
                print_tree(node.right, prefix + ("│   " if is_left else "    "), False)
                
# Example usage:
if __name__ == "__main__":
    root = None
    for _ in range(10):
        value = random.randint(1, 100)
        root = insert(root, value)
    print()
    print("Binary Search Tree:")
    print_tree(root)
    print(f"\033[32mMinimum value in the tree: {find_minimum(root)}\033[0m")