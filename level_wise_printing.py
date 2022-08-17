class TreeNode:
    def __init__(self, name,designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self,level):
        if self.get_level() > level:
            return
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        
        print(prefix + self.name)
            
        if self.children:
            for child in self.children:
                child.print_tree(level)    

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_product_tree():
    nilupul = TreeNode("Nilupul","CEO")

    chinmay = TreeNode("Chinmay","CTO")
    
    vishwa = TreeNode("Vishwa","Infrastructure Head")
    vishwa.add_child(TreeNode("Dhawal","Cloud Manager"))
    vishwa.add_child(TreeNode("Abhijeet","App Manager"))
    
    amir = TreeNode("Amir","Application Head")
    
    chinmay.add_child(vishwa)
    chinmay.add_child(amir)
    
    
    gells = TreeNode("Gells","HR Head")
    gells.add_child(TreeNode("Peter","Recruitement Manager"))
    gells.add_child(TreeNode("Waqas","Policy Manager"))
    

    

    nilupul.add_child(chinmay)
    nilupul.add_child(gells)

    nilupul.print_tree(2)

if __name__ == '__main__':
    build_product_tree()
