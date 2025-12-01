def merge_k_lists(lst):
    res = []
    for i in lst:
        res.extend(i)
    return res.sort()


lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)