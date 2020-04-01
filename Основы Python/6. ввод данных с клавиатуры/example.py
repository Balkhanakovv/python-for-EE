if __name__ == "__main__":
    try:
        print('Решите Следующий пример: 4 * 100 - 54')
        result = int(input())

        while result != 346:
            print('Попробуй снова (4 * 100 - 54)')
            result = int(input())
            

        print('Молодец!!!')
    except:
        print('Не правильно!!!')
