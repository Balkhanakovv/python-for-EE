if __name__ == "__main__":
    try:
        print('Введите положительное целое число:   ')
        num = int(input())

        if num % 2 == 0 and num > 0:
            print('Четное\n')
        elif num % 2 != 0 and num > 0:
            print('Нечетное\n') 
        else:  
            print('Отрицательное')  


    except:
        print('Error: You input wrong number.\n')    
