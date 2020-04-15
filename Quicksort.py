###############
## QUICKSORT ##
###############
import random

# This function returns an array sorted by using quicksort

def swap(A, i,j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp

def quicksort(A,begin, end):
    if begin == end:
        pass
    else:
        q = begin
        for i in range(begin,end):
            if A[i] <= A[end-1]:
                swap(A,i,q)
                q += 1
        quicksort(A,begin, q-1)
        quicksort(A, q ,end)
    
A = [random.randint(0,100) for i in range(100)]
quicksort(A,0, len(A))
