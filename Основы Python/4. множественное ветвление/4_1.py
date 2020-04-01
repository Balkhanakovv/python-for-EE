if __name__ == "__main__":
    try:
        print('Введите целое число:')
        a = int(input())
        print('Введите целое число:')
        b = int(input())

        if a % 2 == 0 and b % 2 == 0:
            print('Оба четные\n')
        elif a % 2 == 0 and b % 2 != 0:
            print('"a" четное\n')
        elif a % 2 != 0 and b % 2 == 0:
            print('"b" четное\n')
        else:
            print('Оба нечетные\n')            

    except:
        print('Введите корректные данные\n')