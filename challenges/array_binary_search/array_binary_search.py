def binary_search(lst, val):
    left = lst[0]
    right = len(lst)
    while len(lst) > 0:
        print(left, 'left')
        print(right, 'right')
        mid = len(lst) // 2 
        if left == right:
            return -1
        if lst[mid] == val:
            return mid
        elif lst[mid] < val:
            left = mid
        elif lst[mid] > val:
            right = mid
    return -1
        
print(binary_search([8, 5 , 52, 15, 150, 81], 15))