# merge sort
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
n = 10
if n <= 0:
    print("Plese enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(n):
        print(fibonacci(i))

#armstrong
def armstrong(n):
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if n == sum:
        return True
    else:
        return False    
n = 2671
print(armstrong(n))

#sum of two numbers is equal to third number in array
def sum_of_two(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            for k in range(j+1,len(arr)):
                if arr[i]+arr[j]==arr[k]:
                    return True
    return False
arr=[1,2,3,4,5,6,7,8,9,10]
print(sum_of_two(arr))

#reverse a string
def reverse_string(string):
    return string[::-1]
string="Geeksforgeeks"
print(reverse_string(string))

#anagram
def anagram(string1,string2):
    if sorted(string1)==sorted(string2):
        return True
    else:
        return False
string1="listen"
string2="hello"
print(anagram(string1,string2))

