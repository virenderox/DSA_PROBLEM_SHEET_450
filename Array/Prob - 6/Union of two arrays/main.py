#User function Template for python3

class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m):
        
        ln_set_a = 0
        dic_a = {}
        
        for val in a:
            if not dic_a.get(val):
                ln_set_a += 1
                dic_a[val] = True
                
    
        count = 0
        b_set = set(b)
        for val in b_set:
            if not dic_a.get(val):
                count += 1
                
        return ln_set_a + count 
                
        
        #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n,m=[int(x) for x in input().strip().split()]
        
        a=[int(x) for x in input().strip().split()]
        b=[int(x) for x in input().strip().split()]
        ob=Solution()
        
        print(ob.doUnion(a,n,b,m))
# } Driver Code Ends
