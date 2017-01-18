class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
        size = self.findSize(A)
        # create a 2-D array

        result = [[0 for i in xrange(size)] for j in xrange(size)]
        last = size - 1
        for i in xrange(A):
            for j in xrange(i, size):
                result[i][j] = A # first row
                result[last][j] = A #last row

                result[j][i] = A # first column
                result[j][last] = A # last column
            size = size - 1
            A = A - 1
            last = last - 1
        return result

    def findSize(self, A):
        if A == 1:
            return 1
        elif A == 2:
            return 3
        return 2 + self.findSize(A - 1)