class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
    
    def add_child(self,data):
        
        if data == self.data:
            return
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
            
    
    def in_order_traversal(self):
        elements = []
        
        if self.left:
            elements += self.left.in_order_traversal()
            
        elements.append(self.data)
        
        if self.right:
            elements += self.right.in_order_traversal()
            
            
        return elements
    
    def search(self,val):
        if self.data == val:
            return True
            
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
    
    def find_minimum_element(self):
       if self.left is None:
           return self.data
        
       return self.left.find_minimum_element()
      
    
    def find_max_element(self):
       if self.right is None:
           return self.data
        
       return self.right.find_max_element()
        


def build_tree(numbers):
    root = BinarySearchTreeNode(numbers[0])
    
    for i in range(1,len(numbers)):
        root.add_child(numbers[i])
        
    return root
if __name__ == "__main__":
    numbers = [17,4,1,20,9,23,18,34,34]
    tree = build_tree(numbers)
    
    print(tree.find_minimum_element())
    print(tree.find_max_element())
