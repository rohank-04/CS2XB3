class RBNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.colour = "R"

    def get_uncle(self):
        return

    def is_leaf(self):
        return self.left == None and self.right == None

    def is_left_child(self):
        return self == self.parent.left

    def is_right_child(self):
        return not self.is_left_child()

    def is_red(self):
        return self.colour == "R"

    def is_black(self):
        return not self.is_red()

    def make_black(self):
        self.colour = "B"

    def make_red(self):
        self.colour = "R"

    def get_brother(self):
        if self.parent.right == self:
            return self.parent.left
        return self.parent.right

    def get_uncle(self):
        return self.parent.get_brother()

    def uncle_is_black(self):
        if self.get_uncle() == None:
            return True
        return self.get_uncle().is_black()

    def __str__(self):
        return "(" + str(self.value) + "," + self.colour + ")"

    def __repr__(self):
        return "(" + str(self.value) + "," + self.colour + ")"

    def rotate_right(self):
        node = self
        y = node.left
        node.left = y.right
        if y.right != None:
            y.right.parent = node
        y.parent = node.parent
        if node.parent == None:
            self.root = y
        elif node == node.parent.right:
            node.parent.right = y
        else:
            node.parent.left = y
        y.right = node
        node.parent = y

    def rotate_left(self):
        node = self
        y = node.right
        node.right = y.left
        if y.left != None:
            y.left.parent = node

        y.parent = node.parent
        if node.parent == None:
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y
        y.left = node
        node.parent = y


class RBTree:

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None

    def get_height(self):
        if self.is_empty():
            return 0
        return self.__get_height(self.root)

    def __get_height(self, node):
        if node == None:
            return 0
        return 1 + max(self.__get_height(node.left), self.__get_height(node.right))

    def insert(self, value):

        if self.is_empty():
            self.root = RBNode(value)
            self.root.make_black()
        else:
            self.__insert(self.root, value)

        while self.root.parent != None:

            self.root = self.root.parent
            self.fix(self.root)
            left = self.root.left
            right = self.root.right
            if right:
                right.make_red()

            if left:
                left.make_red()

    def __insert(self, node, value):

        if value < node.value:
            if node.left == None:
                node.left = RBNode(value)
                node.left.parent = node
                self.fix(node.left)
            else:
                self.__insert(node.left, value)
        else:
            if node.right == None:
                node.right = RBNode(value)
                node.right.parent = node
                self.fix(node.right)
            else:
                self.__insert(node.right, value)

    def fix(self, node):

        # You may alter code in this method if you wish, it's merely a guide.
        if node.parent == None:
            node.make_black()

        while node != None and node.parent != None and node.parent.is_red():
            if node.parent == node.parent.parent.right:
                uncle = node.parent.parent.left
                if uncle != None and uncle.is_red():
                    uncle.make_black()
                    node.parent.make_black()
                    node.parent.parent.make_red()
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        node.rotate_right()
                    node.parent.make_black()
                    node.parent.parent.make_red()
                    node.parent.parent.rotate_left()
            else:
                uncle = node.parent.parent.right

                if uncle != None and uncle.is_red():
                    uncle.make_black()
                    node.parent.make_black()
                    node.parent.parent.make_red()
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        node.rotate_left()
                    node.parent.make_black()
                    node.parent.parent.make_red()
                    node.parent.parent.rotate_right()
            if node == self.root:
                break
            self.root.make_black()

        self.root.make_black()

    def __str__(self):
        if self.is_empty():
            return "[]"
        return "[" + self.__str_helper(self.root) + "]"

    def __str_helper(self, node):
        if node.is_leaf():
            return "[" + str(node) + "]"
        if node.left == None:
            return "[" + str(node) + " -> " + self.__str_helper(node.right) + "]"
        if node.right == None:
            return "[" + self.__str_helper(node.left) + " <- " + str(node) + "]"
        return "[" + self.__str_helper(node.left) + " <- " + str(node) + " -> " + self.__str_helper(node.right) + "]"


# t = RBTree()


# t.insert(31)
# print(t)
# t.insert(11)
# print(t)
# t.insert(50)
# print(t)
# t.insert(7)
# print(t)
# t.insert(26)
# print(t)
# t.insert(83)
# print(t)
# t.insert(9)
# print(t)

# t.insert(110)
# print(t)
# t.insert(42)


# print(t)
