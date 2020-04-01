if __name__ == "__main__":
    try:
        print('Введите свою строку(10-15 символов): ')
        a = input()
        STR_SIZE = len(a)
        i = 0
        res = ""

        print('Первые 8 символов:\t\t', a[0:7])  
        print('4 Символа из центра:\t\t', a[STR_SIZE // 2 - 2:STR_SIZE // 2 + 2])

        while i < STR_SIZE:
            if i % 3 == 0:
                res = res + a[i]
            i += 1

        print('Каждый третий символ:', res)   

    except:
        print('Что-то пошло не так :(')
