def selection_sort(lst):
    n = len(lst)

    for i in range(n-1):
        min_index=i
        for j in range(i+1,n):
            if lst[j]<lst[min_index]:
                min_index=j
        if min_index!=i:
            lst[i],lst[min_index] = lst[min_index],lst[i]




lst = []

while True:
    num = input("Enter num or press q to quit ")
    if num.lower() == 'q':
        break
    lst.append(int(num))

res_lst = selection_sort(lst)

print(lst)
