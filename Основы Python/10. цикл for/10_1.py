if __name__ == "__main__":
    int_list = [13, 14, 15 , 420, 1337]
    a = 0

    for i in int_list:
        int_list[a] = float(i)
        a += 1

    print(int_list)
    print(type(int_list[0]))   