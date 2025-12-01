from timeit import timeit
from random import randint


# merge sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
            
    while left_index < len(left):
        result.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        result.append(right[right_index])
        right_index += 1

    return result

# insertion sort
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key
    return lst

# builtin sort
def built_in(lst):
    return sorted(lst)


def main():
    sizes = [100,1000,10000,100000]
    print(f"{'Size':<10} | {'Merge Sort':>12} | {'Insertion Sort':>15} | {'Built-in Sorted':>10}")
    print('='*61)
    for size in sizes:
        data = [randint(0,10000) for _ in range(size)]
        merge_sort_time = timeit(lambda:merge_sort(data[:]),number=1)
        insertion_sort_time = timeit(lambda:insertion_sort(data[:]),number=1)
        built_in_sort_time = timeit(lambda:built_in(data[:]),number=1)

        print(f'{size:<10} | {merge_sort_time:>12.6f} | {insertion_sort_time:>15.6f} | {built_in_sort_time:>10.6f}')


if __name__ == '__main__':
    main()