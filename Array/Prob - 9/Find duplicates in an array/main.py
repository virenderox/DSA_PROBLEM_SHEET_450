class Solution:
    def duplicates(self, arr, n): 
        dic = {}
        flag = 0
        for val in arr:
            #print(val, dic.get(val))
            if val in dic:
                #print("hi")
                flag = 1
                dic[val] += 1
            else:
                dic[val] = 0
        #print(dic)
        l = []
        for key in dic:
            if dic[key] > 0:
                l.append(key)
        l.sort()
        #print(flag)
        if flag == 0:
            return [-1]
        else:
            return l
               
                
         
                
            

#{ 
#  Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends
