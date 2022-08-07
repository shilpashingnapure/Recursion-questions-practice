'''
Question Link -: https://www.geeksforgeeks.org/sum-triangle-from-array/
level : Easy
'''
#code
arr = [1,2,3,4,5]

def sumOfarray(arr):
    if len(arr) < 1:
        return
    temp = []
    for i in range(1 , len(arr)):
        s = arr[i-1] + arr[i]
        temp.append(s)

    sumOfarray(temp)
    print(arr)

sumOfarray(arr)
