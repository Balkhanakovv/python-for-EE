if __name__ == "__main__":
    try:
        print('\t\tОбщество XXI века')
        print('Введите свой возраст: ')
        age = int(input())

        if age > -1 and age < 7:
            print('Вам в детский сад')
        elif age > 6 and age < 18:
            print('Вам в школу')
        elif age > 17 and age < 25:
            print('Вам в профессиональное учебное заведение')
        elif age > 24 and age < 60:
            print('Вам на работу')
        elif age > 59 and age < 120:
            print('Вам предоставляется выбор')
        else:
            for i in range(5):
                print('Ошибка! Это программа для людей')

    except:
        print('Что-то не то :(')