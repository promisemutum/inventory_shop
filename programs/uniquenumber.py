def uniqueNum(my_list, i):
    new_list = []
    for j in range(0,i):
        if my_list[j] in new_list:
            pass
        else:
            new_list.append(my_list[j])
    print(new_list)

my_list = []
i = int(input("Number of elements:"))
for _ in range(i):
    my_list.append(input())
uniqueNum(my_list, i)