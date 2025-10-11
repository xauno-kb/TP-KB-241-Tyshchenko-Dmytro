def find_insert_position(sorted_list, value):
    left, right = 0, len(sorted_list)
    while left < right:
        mid = (left + right) // 2
        if sorted_list[mid] < value:
            left = mid + 1
        else:
            right = mid
    return left

lst = [1, 3, 5, 7]
pos = find_insert_position(lst, 4)
print("Insert position for 4:", pos)
