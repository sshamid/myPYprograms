
# coding: utf-8

# In[ ]:

# insertion sort

def insertion(A):
    """Insertion sort list"""
    for i in range(1,len(A)):
        insert(A, i, A[i])

def insert(A, idx, value):
    """insert value into proper location A[:idx]"""

    i = idx-1
    while i>=0 and A[i] > value:
        A[i+1] = A[i]
        i = i-1
        
    A[i+1] = value


# In[27]:

def copymergesort(A):
    """Mergesort of A and return a new collection"""
    if len(A) < 2:
        return A

    mid = len(A)/2
    left = copymergesort(A[:mid])
    right = copymergesort(A[mid:])

    i = j = 0
    B = []

    while len(B) < len(A):
        if j >= len(right) or (i < mid and left[i] < right[j]):
            B.append(left[i])
            i += 1
        else:
            B.append(right[j])
            j += 1

    return B

import random

list = [random.randint(1,90) for x in range(20)]

print copymergesort(list)


# In[ ]:




# In[1]:

import copy
def mergesort(A):
    ''' merge sort in place'''
    copyA = list(A)
    mergesort_array(copyA, A, 0, len(A))
    
def mergesort_array(A, result, start, end):
    if end - start < 2:
        return
    if end - start == 2:
        if result[start] > result[start+1]:
            result[start], result[start+1] = result[start+1], result[start]
        return
    mid = (start + end)/2
    mergesort_array(result, A, start, mid)
    mergesort_array(result, A, mid, end)
    
    i = start
    j = mid
    idx = start
    
    while idx < end:
        if j >= end  or (i < mid and A[i] < A[j]):
            result[idx] = A[i]
            i += 1
        else:
            result[idx] = A[j]
            j +=1
        
        idx += 1

import random   
listA = [random.randint(1,90) for x in range(20)]
listB = [1,2,4,1,49]
mergesort(listB)
print listB


# In[51]:

listA


# In[55]:

import copy
def mergeSort(A):
    """merge sort A in place"""
    copyA = copy.copy(A)

    mergesort_array(copyA, A, 0, len(A))


def mergesort_array(A, result, start, end):
    """Mergesort array in memory with given range"""
    if end - start < 2:
        return
    if end - start == 2:
        if result[start] > result[start+1]:
            result[start],result[start+1] = result[start+1],result[start]
        return

    mid = (end + start)/2
    mergesort_array(result, A, start, mid)
    mergesort_array(result, A, mid, end)
    
    # merge is now ready. Merge from A back into result
    i = start
    j = mid
    idx = start
    while idx < end:
        if j >= end or (i < mid and A[i] < A[j]):
            result[idx] = A[i]
            i += 1
        else:
            result[idx] = A[j]
            j += 1
            
        idx += 1

import random   
listA = [random.randint(1,90) for x in range(20)]
listB = [1,2,4,1,49]
mergesort(listA)
print listA


# In[29]:

# counting sort
def counting_sort(array):
    """in-place counting sort"""
    maxval = 0
    for i in array:
        if maxval < i:
            maxval = i
    m = maxval + 1
    count = [0] * m               # init with zeros
    for a in array:
        count[a] += 1             # count occurences
    i = 0
    for a in range(m):            # emit
        for c in range(count[a]): # - emit 'count[a]' copies of 'a'
            array[i] = a
            i += 1
    return (array,count)
 
print counting_sort( [7, 4, 7, 2, 1, 3, 2, 1, 4, 2, 3, 2, 1])


# In[5]:

# quick sort
def quicksort(seq):
    if len(seq) <= 1: 
        return seq
    lo, pivot, hi = partition(seq)
    return quicksort(lo) + [pivot] + quicksort(hi)

def partition(seq):
    pi, seq = seq[0], seq[1:]
    lo = [x for x in seq if x <= pi]
    hi = [x for x in seq if x > pi]
    return lo, pi, hi
x = range(20, -1, -1)
print quicksort(x)


# In[27]:

# Bucket sort
# Parameters: array to be sorted, values in [0,1]
# Result: values sorted into increasing order
def bucketSort(unsorted):
    n = len(unsorted)
    buckets = [list() for i in range(n)] # empty buckets

    # place the values to be sorted in the buckets
    for i in range(n):
        buckets[int(n*unsorted[i])].append(unsorted[i])

    # sort each bucket and concatenate to the result
    result = []
    for i in range(n):
        sortedBucket = sorted(buckets[i])
        result.extend(sortedBucket)

    return result
import random
x = [random.random() for i in range(10)]
print bucketSort(x)


# In[ ]:



