#!/usr/bin/env python
# coding: utf-8

# ## 1. Write a Python Program to find sum of array?

# In[5]:


A1 = [[1,2],[4,5,5],[3,4]]
sum = 0
for i in A1:
    for j in i:
        sum = sum + j
print("Sum of array is:",sum)    


# ## 2. Write a Python Program to find largest element in an array?

# In[20]:


def largest(A2,n):
    max = A2[0]
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max
  
A2 = [1, 300.24, 95, 0, 98]
n = len(A2)
Ans = largest(A2,n)
print ("Largest element in given array is",Ans)
  


# ## 3. Write a Python Program for array rotation?

# In[32]:


def rotateArray(arr,n, d):
    temp = []
    i = 0
    while (i < d):
        temp.append(arr[i])
        i = i + 1
    i = 0
    while (d < n):
        arr[i] = arr[d]
        i = i + 1
        d = d + 1
    arr[:] = arr[: i] + temp
    return arr

arr = [1, 2, 3, 4, 5, 6, 7]

print("Array after left rotation is: ",rotateArray(arr, len(arr), int(input("Number of elements we want to rotate: "))))


# ## 4. Write a Python Program to Split the array and add the first part to the end?

# In[ ]:


def rotateArray(arr,n, d):
    temp = []
    i = 0
    while (i < d):
        temp.append(arr[i])
        i = i + 1
    i = 0
    while (d < n):
        arr[i] = arr[d]
        i = i + 1
        d = d + 1
    arr[:] = arr[: i] + temp
    return arr

arr = [1, 2, 3, 4, 5, 6, 7]

print("Array after left rotation is: ",rotateArray(arr, len(arr), int(input("Number of elements we want to rotate: "))))


# ## 5. Write a Python Program to check if given array is Monotonic?

# In[36]:


def isMonotonic(A):
  
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1)))
  
A = [6,5,4,3,2,1,1,1]
  
print(isMonotonic(A))
  


# In[ ]:




