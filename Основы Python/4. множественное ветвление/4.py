if __name__ == "__main__":
    try:
        print('Введите целое число:')
        a = int(input())
        print('Введите целое число:')
        b = int(input())

        if a > b:
            c = a - b
        elif a < b:
            c = a + b
        else:
            c = a

        print(c, '\n')    

    except:
        print('Введите корректные данные\n')