import random


def binarySearch(data,target,low,high):
    if low > high:
        return False
    
    mid = (low + high) // 2

    if target == data [mid]:
        return True
    elif target < data[mid]:
        return binarySearch(data,target,low,mid - 1)
    else:
        return binarySearch(data,target,mid + 1,high) 
    


if __name__ == '__main__':
    data = [random.randint(0,100) for i in range(10)]
    
    data.sort()

    print(data) 
    target = int(input('What number would you like to find? '))
    found = binarySearch(data, target, 0, len(data)-1)
    
    print(found)
