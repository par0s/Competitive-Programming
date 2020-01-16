class Solution:
    def commonChars(self,A):
        dicts = {}
        words = []
        commons = []

        #print(A)

        for k in A[0]:
            if k not in dicts:
                dicts[k] = 1
            else:
                dicts[k] += 1

        for i in A[1:]:
            #print(i)
            new = {}
            for j in i:
                if j in new:
                    new[j] += 1
                else:
                    new[j] = 1

            l = not dicts

            for k in dicts:
                if k not in new:
                    dicts[k] = 0
                else:
                    if new[k] < dicts[k]:
                        dicts[k] = new[k]

            #print(dicts,new)

        for i in dicts:
            if dicts[i] > 0:
                for j in range(dicts[i]):
                    commons.append(i)

        return commons
    

