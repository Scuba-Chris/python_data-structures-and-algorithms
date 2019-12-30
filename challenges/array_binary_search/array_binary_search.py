def binary_search(lst, val):
    left = 0
    right = len(lst)
    while left <= right:
        print(left, 'left')
        print(right, 'right')
        mid = (left + right) // 2 
        if left == right:
            return -1
        if lst[mid] == val:
            return mid
        elif lst[mid] < val:
            left = mid + 1
        elif lst[mid] > val:
            right = mid - 1
        
print(binary_search([8, 5 , 52, 15, 150, 81], 15))