if __name__ == "__main__":
    some_list = ['В лесу родилась елочка', 'В лесу она росла', 'Зимой и летом стройная', 'Зелёная была']

    for i in some_list:
        for j in i:
            print(j, end='-')
        print()    