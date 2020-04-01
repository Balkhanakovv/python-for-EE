if __name__ == "__main__":
    list1 = ['ab', 'ra', 'ka', 'da', 'bruh']
    list2 = ['kreks', 'peks', 'shreks']

    print('Второй элемент из первого списка:\t', list1[1])

    list2[-1] = 'feks'
    print('Второй список:\t', list2)

    new_list = list1 + list2
    print('Соединенный список:\t', new_list)

    center_of_new_list = new_list[len(new_list) // 2 - 2 : len(new_list) // 2 + 2]
    print('Срез нового списка:\t', center_of_new_list)

    center_of_new_list.append('new')
    center_of_new_list.append('elements')

    print('Новый список:\t', center_of_new_list)

