def Solve (N, A):
    # Write your code here
    closest = A[0]
    for i in range(len(A)):
        if A[i] == 0:
            return 0
        if A[i]*A[i] < closest*closest:
            closest = A[i]
        elif A[i]*A[i] == closest*closest and A[i] > closest:
            closest = A[i]
    return closest
    
N = input()
A = list(map(int, input().split()))
out_ = Solve(N, A)
print (out_)
