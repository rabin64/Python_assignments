# 24. Write a Python program to clone or copy a list.

def clone_list(list_item):
    clonned_list = list.copy(list_item)
    return clonned_list


if __name__ == "__main__":
    main_list = []
    size = int(input("enter the number of a item list: "))
    for i in range(size):
        items = input("enter the list values to be added: ")
        main_list.append(items)
    res = clone_list(main_list)
    print(f'original list: {main_list}\nClonned list: {res}')