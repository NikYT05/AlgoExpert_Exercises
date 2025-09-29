class FileSystem:
    def __init__(self):
        self.root = Directory("/")

    def create_directory(self, path):
        path = list(filter(None, path.split("/")))
        # print(path)
        if len(path) == 1:
            self.root.add_node(Directory(path[0]))
            return

        node = self.root
        for i in path:
            if i in node.children:
                node = node.children[i]
                continue

            if i not in node.children and path[-1] == i:
                node.add_node(Directory(i))
            else:
                raise ValueError

    def create_file(self, path, contents):
        path = list(filter(None, path.split("/")))
        if len(path) == 1:
            self.root.add_node(File(path[0]))
            self.root.children[path[0]].write_contents(contents)
            return
        
        node = self.root
        for i in path:
            if i in node.children:
                node = node.children[i]
                continue

            if i not in node.children and i == path[-1]:
                node.add_node(File(i))
                node.children[i].write_contents(contents)
            else:
                raise ValueError

    def read_file(self, path):
        path = list(filter(None, path.split("/")))
        node = self.root
        for i in path:
            if i in node.children and i == path[-1]:
                return node.children[i].contents
            elif i not in node.children:
                break
            else:
                node = node.children[i]
        raise ValueError

    def delete_directory_or_file(self, path):
        path = list(filter(None, path.split("/")))
        if isinstance(path[-1], File):
            node = self.root
            for i in path:
                if i not in node.children:
                    raise ValueError
                
                if i in node.children and path[-1] == i:
                    del node.children[i]
                else:
                    node = node.children[i]

        
        node = self.root
        for i in path:
            if i not in node.children:
                raise ValueError
            
            if i in node.children and path[-1] == i:
                node.delete_node(i)
                return
            else:
                node = node.children[i]

    def size(self):
        files = []
        
        def dfs(node):
            # print(files)
            if isinstance(node, File):
                files.append(node)
                return

            if node.children == {}:
                return
            
            for i in node.children.values():
                dfs(i)
        
        dfs(self.root)
        
        size = 0
        for i in files:
            size += i.contents.__len__()

        return size


    def __str__(self):
        return f"*** FileSystem ***\n" + self.root.__str__() + "\n***"
    
    @staticmethod
    def _validate_path(path):
        if not path.startswith("/"):
            raise ValueError("Path should start with `/`.")


    def _find_bottom_node(self, node_names):
        current = self.root.children
        for i in node_names:
            print(current)
            for j in current:
                if i == j and i == node_names[-1]:
                    current = current[j]
                    break
                elif i == j and not i == node_names[-1]:
                    current = current[j].children
                    break
                else:
                    continue
        return current


class Node:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name} ({type(self).__name__})"


class Directory(Node):
    def __init__(self, name):
        super().__init__(name)
        self.children = {}

    def add_node(self, node):
        self.children[node.name] = node

    def delete_node(self, name):
        del self.children[name]

    def __str__(self):
        string = super().__str__()

        children_strings = []
        for child in list(self.children.values()):
            child_string = child.__str__().rstrip()
            children_strings.append(child_string)

        children_combined_string = indent("\n".join(children_strings), 2)
        string += "\n" + children_combined_string.rstrip()
        return string


class File(Node):
    def __init__(self, name):
        super().__init__(name)
        self.contents = ""

    def write_contents(self, contents):
        self.contents = contents

    def __len__(self):
        return len(self.contents)

    def __str__(self):
        return super().__str__() + f" | {len(self)} characters"


def indent(string, number_of_spaces):
    spaces = " " * number_of_spaces
    lines = string.split("\n")
    indented_lines = [spaces + line for line in lines]
    return "\n".join(indented_lines)

fs = FileSystem()
fs.create_directory("/dir1")
fs.create_directory("/dir1/dir2")
fs.create_file("/dir1/dir2/dile1.html", "Hello World")
print(fs)
fs.delete_directory_or_file("/dir1")
print(fs)
fs.read_file("/dir1/dir2/dile1.html")