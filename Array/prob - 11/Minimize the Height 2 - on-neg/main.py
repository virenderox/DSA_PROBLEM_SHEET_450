#User function Template for python3

class Solution:
    def getMinDiff(self, arr, n, k):
        arr.sort()
        #print(arr)
        ans = arr[n-1] - arr[0]
        small = arr[0] + k
        large = arr[n-1] - k
        
        for i in range(1,n):
            
            if arr[i] - k < 0:
                continue
            #print(arr[i-1])
            min_ = min(small, arr[i] - k)
            max_ = max(large, arr[i-1] + k )
            ans = min(ans, max_ - min_)
        #print(max_,min_)
        
        
        
        
        return ans
        
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends
