def find_even_index(arr):
    #your code here
    sum1 = 0
    sum2 = 0
    for i in range(len(arr)):
        sum2 = sum(arr[i+1:])
        if sum1 == sum2:
            return i
        sum1 = sum(arr[:i+1])
    return -1