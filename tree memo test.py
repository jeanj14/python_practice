class TreeClass:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self):
        spaces = " "* self.get_level()
        print(f"{spaces}{self.data}")
        for x in self.children:             #if self.children:
            if self.children:                  #for child in children:
                print(self.print_tree())            #self.print_tree()

    def get_level(self):
        p = self.parent
        level = 0
        for x in self.children: #while p:
            if p:                   #p = p.parent
                level += 1
        return level


