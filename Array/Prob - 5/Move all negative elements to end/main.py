#User function Template for python3

class Solution:
    def segregateElements(self, arr, n):
        l_pos = []
        l_neg = []
        
        for val in arr:
            if val >= 0:
                l_pos.append(val)
            else:
                l_neg.append(val)
        ln_pos = len(l_pos)
        ln_neg = n - ln_pos
                
        for i in range(ln_pos):
            arr[i] = l_pos[i]
        #print(arr)
        for j in range(ln_pos,n):
            arr[j] = l_neg[j - ln_pos]
            
        return
            
            
        # Your code goes here

#{ 
#  Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        ob.segregateElements(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends
