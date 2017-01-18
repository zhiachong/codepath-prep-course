class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextGreater(self, A):
        res = []
        default = -1

        for i in xrange(len(A)):
            curMax = float('inf')
            com = A[i]
            for j in xrange(i, len(A)):
                cur = A[j]
                if cur <= curMax and cur > com:
                    curMax = cur
                    break
            if curMax == float('inf'):
                curMax = default
            res.append(curMax)
        return res
