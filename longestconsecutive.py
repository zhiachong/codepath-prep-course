class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        N = len(A)
        K = set(A)
        maxCount = 0

        for i in xrange(N):
            left = A[i] - 1
            right = A[i] + 1
            count = 1

            while left in K:
                count += 1
                K.remove(left)
                left -= 1
            while right in K:
                count += 1
                K.remove(right)
                right += 1
            maxCount = max(count, maxCount)
        return 1 if maxCount == 0 else maxCount
