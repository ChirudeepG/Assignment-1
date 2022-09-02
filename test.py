#merge sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr
arr=[1,2,3,4,5,6,7,8,27,272,9,10]
print(merge_sort(arr))

#binary search
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1
arr=[1,2,3,4,5,6,7,8,9,10]
x = 10
result = binary_search(arr, x)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")

#fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))
n = 5
if n <= 0:
    print("Plese enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(n):
        print(fibonacci(i))

#amstrong
def amstrong(n):
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if n == sum:
        print(n,"is an Armstrong number")
    else:
        print(n,"is not an Armstrong number")
n = 1654
amstrong(n)

#sum of two numbers is equal to third number in array
def sum_of_two(arr, n):
    for i in range(0, n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if (arr[i] + arr[j] == arr[k]):
                    print("Triplet is", arr[i],
                          ", ", arr[j], ", ", arr[k])
                    return True
    return False
arr = [1, 2, 3, 4, 5]
n = len(arr)
sum_of_two(arr, n)

#reverse a string
def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
s = "Geeksforgeeks"
print ("The original string  is : ",end="")
print (s)
print ("The reversed string(using loops) is : ",end="")
print (reverse(s))

#anaagram
def areAnagram(str1, str2):
    n1 = len(str1)
    n2 = len(str2)
    if n1 != n2:
        return 0
    str1 = sorted(str1)
    str2 = sorted(str2)
    for i in range(0, n1):
        if str1[i] != str2[i]:
            return 0
    return 1
str1 = "listen"
str2 = "silent"
if areAnagram(str1, str2):
    print("The two strings are anagram of each other")
else:
    print("The two strings are not anagram of each other")

