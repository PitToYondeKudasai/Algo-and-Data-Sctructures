#################
## Left Rotate ##
#################

def reverse(A,s,f):
    while s < f:
        A[s],A[f] = A[f],A[s]
        f -= 1
        s += 1
    return A

# The following function shift all the elements of A by k positions on the left
# the first k elements are attached at the end of A
# This is done in place in O(n)
def left_rotate(A,k):
    n = len(A)
    k = k % n
    A = reverse(A,0,n-1)
    A = reverse(A,0,n-k-1)
    A = reverse(A,n-k,n-1)
    return A
        
A = [1,2,3,4,5,6,7,8,9,10]

A = left_rotate(A,4)

