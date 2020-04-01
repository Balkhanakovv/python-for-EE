if __name__ == "__main__":
    try:
        print('Введите число: ')
        a = int(input())

        while (a != 0):
            print(a % 10)
            a = a // 10
    except:
        print('Ведено неправильное число\n')