[1207. Unique Number of Occurrences](https://leetcode.com/problems/unique-number-of-occurrences)

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        a ={}
        for i in arr:
            if i in a:
                a[i] += 1
            else:
                a[i]= 1 
        
        occ  = set()

        for i in a.values():
            if i in occ:
                return False
            else:
                occ.add(i)

    #   return len(set(a.values()))== len(a)


        
