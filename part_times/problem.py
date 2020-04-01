
def problem(job_list):
    class Node():
        def __init__(self, start, end, pay, parent=None):
            self.start = start
            self.end = end
            self.pay = pay
            self.children = []
            self.parent = parent

        def calculate(self, total_earned = 0):
            node_pointer = self
            while node_pointer :
                # cumulate earned value
                total_earned = total_earned + node_pointer.pay

                # set parent as next node
                node_pointer = node_pointer.parent

            return total_earned

    def popluate(current_node, lst, last_node_list):

        for index, part in enumerate(lst):

            start = part[0]
            end = part[1]
            pay = part[2]

            # check if job starts only after this job ends
            if current_node.end <= start:
                # create job node
                child = Node(start, end, pay, current_node)

                # append job node to this one
                current_node.children.append(child)

                # make a copy and remove current index
                tmp_lst = lst.copy()
                del tmp_lst[index]

                # DFS recursive call this node
                popluate(child, tmp_lst, last_node_list)

        # check if has children, if none than add as last node
        if not len(current_node.children):
            last_node_list.append(current_node)

    # holds a list of last nodes in the tree
    last_node_list = []

    # the startining main root
    root = Node(0, 0, 0)

    # Recursivly create tree
    popluate(root, job_list, last_node_list)

    # loop through all paths and get price
    price_calucated = list(map(lambda n: n.calculate(), last_node_list))

    # get the highest earned value
    return max(price_calucated)

if __name__ == "__main__" :
    testcase = [
        (
            19,
             [
                [3, 6, 3],
                [2, 4, 2],
                [10, 12, 8],
                [11, 15, 5],
                [1, 8, 10],
                [12, 13, 1]
             ]
        ),
        (
            4,
            [
                [1, 2, 1],
                [1, 2, 2],
                [2, 3, 1],
                [3, 4, 1],
                [1, 4, 2]
            ]
        )
    ]
    for tnum, (result, part_times) in enumerate(testcase):
        answer = problem(part_times)
        print("Testcase", tnum)
        print("Expected:", result)
        print("Answer:", answer)
        print("Result:", "Correct" if result == answer else "Failed")
        print()
