<h1>1207<h1>


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


        
