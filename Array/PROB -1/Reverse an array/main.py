#code
def reverse(n,lst):
    i = n
    while i != 0:
        print(lst[i-1], end = ' ')
        i = i - 1
    print()
    
def rev(n,lst):
    start = 0
    end = n - 1
    while start < end:
        lst[start],lst[end] = lst[end], lst[start]
        start += 1
        end -= 1
    for i in lst:
        print(i, end = " ")
        
    print()
t = int(input())
for i in range(t):
    n = int(input())
    lst = list(map(int,input().split()))
    #reverse(n,lst)
    rev(n,lst)


    
    
