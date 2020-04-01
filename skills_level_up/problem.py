
def problem(total_sp, skills):

    class Node():
        def __init__(self, id):
            self.id = id
            self.parent = None
            self.children = [ ]
            self.last_children = [ ]
            self.weight = 0

        def find(self, id):

            # check self first
            if self.id == id:
                return self

            # loop through children and find
            for node in self.children:
                n = node.find(id)
                if n:
                    return n

            # not found!
            return None

        def find_create(self, id):

            # find node with id
            node = self.find(id)

            # if node found return
            if node:
                return node

            # node not found, create new Node
            return Node(id)

        def get_last_node(self, root):

            # if no children im last
            if not len(self.children):
                root.last_children.append(self)

            # go through children and get last child
            for child in self.children:
                child.get_last_node(root)

        def bubble_up(self):

            self.weight = sum(self.children)

            if self.parent:
                self.parent.bubble_up()

        def __radd__(self, other):
            return self.weight + other

    # root pointer
    root = None

    # node ids
    node_id_list = []

    # populate tree
    for item in skills:

        # first node setup
        if not root: root = Node(item[0])

        node_a = root.find_create(item[0])
        node_b = root.find_create(item[1])
        node_b.parent = node_a
        node_a.children.append(node_b)

        # save node ids
        if item[0] not in node_id_list:
            node_id_list.append(item[0])

        if item[1] not in node_id_list:
            node_id_list.append(item[1])

    # find all last node
    root.get_last_node(root)

    # weight of nodes
    weight_list = [0] * len(node_id_list)

    while sum(weight_list) != total_sp:

        # incremental increase of last nodes
        for n in root.last_children:
            n.weight = n.weight + 1

        # bubble up tree
        already_bubble_list = []
        for n in root.last_children:
            n.parent.bubble_up()

        # get node for id
        for i in range(1, len(weight_list)+1):
            n = root.find(i)
            weight_list[i-1] = n.weight

    return weight_list

if __name__ == "__main__" :
    testcase = [
        (
            [44, 11, 33, 11, 11, 11],
            121,
            [[1, 2], [1, 3], [3, 6], [3, 4], [3, 5]]
        )
    ]
    for tnum, (result, total_sp, skills) in enumerate(testcase):
        answer = problem(total_sp, skills)
        print("Testcase", tnum)
        print("Expected:", result)
        print("Answer:", answer)
        print("Result:", "Correct" if result == answer else "Failed")
        print()
