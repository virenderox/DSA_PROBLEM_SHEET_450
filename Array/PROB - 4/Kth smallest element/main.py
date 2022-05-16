#User function Template for python3

class Solution:
    def kthSmallest(self,arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        #return(self.sortKth(arr))
        
        
        #lst = arr
        #for i in range(k):
           # ans = self.minkth(lst)
            #print(ans)
           # lst.remove(ans)
            
        #return ans
        
        lst = self.arrStore(arr)
        return(lst[0])
        
        
    def arrStore(self,lst):
        l = []
        min = float('inf')
        for i in lst:
            if i < min:
                min = i
                l.append(min)
        return l
        #print(l)
        
    def minkth(self,lst):
        min = float('inf')
        for i in lst:
            if i < min:
                min = i
        return min
        
    def sortKth(self,arr):
        arr.sort()
        return(arr[k-1])

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    import random 
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=list(map(int,input().strip().split()))
        k=int(input())
        ob=Solution()
        print(ob.kthSmallest(arr, 0, n-1, k))
        
# } Driver Code Ends
