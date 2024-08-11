class TreeNode:
    def __init__(self, name, desig):
        self.name = name
        self.desig = desig
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        child = f"{self.name} ({self.desig})"
        self.children.append(child)

    def print_tree(self):
        print(self.name)

        #spaces = self.get_level() * " "

        """        
        print(f"{spaces}{self.data}")
                if len(self.children) > 2:
                    for self.child in self.children:
                        self.print_tree()"""



    def get_level(self):
        level = 0

        p = self.parent

        while p:
            level+=1
            p = p.parent

        return level

def build_management_tree():
    root_name = TreeNode("Nilulpul")
    root_desig = TreeNode("CEO")
    return root_name and root_desig

if __name__ == "__main__":
    root_node = build_management_tree()
    root_node.print_tree()


