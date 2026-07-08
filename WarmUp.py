def kLargestNumber(numbers:list,k:int):
    sorted_numbers=sorted(numbers,reverse=True)
    k_largest_numbers=[]
    for i in range(0,k):
        k_largest_numbers.append(sorted_numbers[i])
        print(k_largest_numbers)
    return k_largest_numbers

numbers= [9,6,5,4]
print(kLargestNumber(numbers,3))

def binarySearch(list:tuple,target:int):
    sorted_list=sorted(list)
    low=0
    high=len(list)-1
    for i in range(0,len(list)):
        mid=(low+high)//2
        if list[mid]==target:
            return mid
        elif list[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1
array=(1, 3, 5, 7, 9, 11, 13)
print(binarySearch(array,6))

print("Flatten test")
def flatten(nested_list:list):
    flat_list=[]
    for item in nested_list:
        if isinstance(item,list):
            flat_list.extend(item)
        else:flat_list.append(item)
    return flat_list

flat = [3,[1, 4] , [1, 5, 9, 2], 6]
print(flatten(flat))

def bubble_sort(array:list):
    for i in range(0,len(array)):
        for j in range(i+1,len(array)):
            if(array[i]>array[j]):
                temp=array[i]
                array[i]=array[j]
                array[j]=temp
    return array
array = [3,5,1,7,2,9,13,11]
print(bubble_sort(array))

def insertion_sort(array:list):
    for i in range(1,len(array)):
        key=array[i]
        j = i-1
        while j>=0 and key<array[j]:
            array[j+1]=array[j]
            j-=1

    return array

print(insertion_sort(array))



