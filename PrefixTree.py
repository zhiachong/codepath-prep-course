"""
Prefix tree has an empty root.
The root has keys/children, each corresponding to an alphabet.

makeTree constructs the prefix tree, and has a counter (count) for
keeping track of results in the path.


"""

class Node:
    def __init__(self, val=None):
        self.val = val
        self.count = 0
        self.keys = {}
class Solution:
    def makeTree(self, tree, word):
        temp = tree
        for i in word:
            if i not in temp.keys:
                temp.keys[i] = Node(i)

            temp.keys[i].count += 1
            temp = temp.keys[i]


    def prefixTree(self, A):
        tree = Node()
        for word in A:
            self.makeTree(tree, word)

        res = []
        for word in A:
            j = 0
            tempTree = tree
            for i in word:
                if i in tempTree.keys:
                    l = tempTree.keys[i].count
                    if l > 1:
                        tempTree = tempTree.keys[i]
                    elif l == 1:
                        res.append(word[:j+1])
                        break
                j += 1
            if j == len(word):
                res.append(word)
        return res

    def prefix(self, A):
        return self.prefixTree(A)
