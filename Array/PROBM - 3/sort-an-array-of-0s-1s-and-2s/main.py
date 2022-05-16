#User function Template for python3

class Solution:
    def sort012( self,a, arr_size):
        lo = 0
        hi = arr_size - 1
        mid = 0
        while mid <= hi:
            if a[mid] == 0:
                a[lo], a[mid] = a[mid], a[lo]
                lo = lo + 1
                mid = mid + 1
            elif a[mid] == 1:
                mid = mid + 1
            else:
                a[mid], a[hi] = a[hi], a[mid] 
                hi = hi - 1
        return a
        
    def sortDic(self,arr,n):
        dic = {0:0,1:0,2:0}
        for value in arr:
            dic[value] += 1
        count = 0   
        for key in dic:
            val = dic[key]
            while val != 0:
                arr[count] = key
                val -= 1
                count  += 1
        return 
                
            


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends
