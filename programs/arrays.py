import numpy as np

def list_imp():
    def enter(amt):
        my_list = []
        for _ in range(amt):
            my_list.append(input('Enter elements: '))
        arr_ori = np.array(my_list)
        return arr_ori

    def option1(arr_ori, amt):
        sorted_list = sorted(arr_ori)
        for i in range(0,amt):
            print(sorted_list[i] , end=" ")
        return sorted_list

    def option2(arr_ori, amt):
        sorted_list = sorted(arr_ori)
        reverse = sorted_list[::-1]
        for i in range(0,amt):
            print(reverse[i] , end=" ")
    
    print("Start array program")
    i = input("Press 1 for using list\n-")
    if i == '1':
        list_imp()
    start = input("Do you want to start the program?(y/n):")
    con = 'y'
    if start == 'y':
        amt = int(input("Enter number of elements: "))
        arr_ori = []
        arr_ori = enter(amt)
        print("The original array: "+ str(arr_ori))
        while con == 'y':
            options = input("Press 1 for sorting\nPress 2 for reverse sorting\n-")
            if options == '1':
                option1(arr_ori, amt)
            elif options == '2':
                option2(arr_ori, amt)
            con = input("\nContinue operations?y:")
        print("Bye")
    elif start == 'n':
        print("Bye")