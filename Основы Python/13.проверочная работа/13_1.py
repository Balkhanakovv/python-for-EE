if __name__ == "__main__":
    try:
        s = ""
        n = 0
        m = 0

        print('Введите число от 1 до 9:')
        x = int(input())

        while x < 0 or x > 10:
            print('Введите число от 1 до 9:')
            x = int(input())

        if x > 0 and x < 4:
            print('Введите строку:')
            s = input(s)
            print('Введите количество повторов:')
            n = int(input())  

            i = 0
            while i < n:
                print(s)
                i += 1 

        if x > 3 and x < 7:
            print('Введите степень:')
            m = int(input())
            i = 0
            res = 1
            while i < m:
                res *= x
                i += 1
            
            print('X в степени m', res)    

        if x > 6 and x < 10:
            i = 0
            while i < 11:
                print(x + i)
                i += 1       

        
    except:
        print('Что-то пошло не так')