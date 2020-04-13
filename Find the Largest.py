##################
## Find Largest ##
##################

# This code implement a merge sort algorithm to sort a generic array
# and return the largest element
import math

# Function to merge two already sorted arrays
def merge_sorted(A_l,A_r):
    a_l = 0
    a_r = 0
    A = []
    while a_l < len(A_l) and a_r < len(A_r):
        if A_l[a_l] < A_r[a_r]:
            A.append(A_l[a_l])
            a_l +=1
        else:
            A.append(A_r[a_r])
            a_r += 1
    if a_l < len(A_l):
        A.extend(A_l[a_l:len(A_l)])
    elif a_r < len(A_r):
        A.extend(A_r[a_r:len(A_r)])
    return A

# Function that implements the merge sort
def merge_sort(A):
    if len(A) <= 1:
        return A
    else:
        n = math.floor(len(A)/2)
        A_l = A[0:n]
        A_r = A[n:len(A)]
        return(merge_sorted(merge_sort(A_l), merge_sort(A_r)))

# Function that returns the largest element of an array
def Find_Largest(A):
    return merge_sort(A)[-1]


# Example     
A = [1,2,4,5,6,2,7,0,10, 11,29, 0,-1]

print(Find_Largest(A))
    
    
