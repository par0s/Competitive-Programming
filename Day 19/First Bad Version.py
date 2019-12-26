# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self,n):
        """
        :type n: int
        :rtype: int
        """

        low = 0
        high = n
        while(low <= high):
            mid = (low + high)//2
            #print(mid,isBadVersion(mid))
            if isBadVersion(mid) == True:
                if not isBadVersion(mid - 1):
                    return mid
                else:
                    high = mid
            else:
                low = mid + 1
