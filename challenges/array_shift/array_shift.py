def insert_shift_array(lst, num):
  new_lst = []
  middle = (len(lst) + 1) // 2
  for i in range(len(lst) + 1):
    if i < middle:
      new_lst.append(lst[i])
    elif i == middle:
      new_lst.append(num)
    elif i > middle:
      new_lst.append(lst[i - 1])
  print(new_lst)
insert_shift_array([2,4,6,8], 5)