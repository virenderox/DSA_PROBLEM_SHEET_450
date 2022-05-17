#User function Template for python3

def rotate( arr, n):
    lst = arr[:]
    arr[0] = lst[n-1]
    for ind in range(1,n):
        arr[ind] = lst[ind-1]
    
    


#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        rotate(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends
