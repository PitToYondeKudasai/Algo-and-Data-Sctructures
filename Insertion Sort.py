####################
## Insertion Sort ##
####################
# The following algorithm implements the insertion sort
# and prints at every iteration of the outer loop
# the array so far

def Insertion_sort(A):
    for i in range(1,len(A)):
        while A[i] < A[i-1]:
            tmp = A[i]
            A[i] = A[i-1]
            A[i-1] = tmp
            i -= 1
        print(A)


# Example
A = [7,17,89,74,21,7,43,9,26,10]

Insertion_sort(A)

