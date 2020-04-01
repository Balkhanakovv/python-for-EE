if __name__ == "__main__":
    try:
        print('enter int number:   ')
        num = int(input())

        if num > 0:
            print('1\n')
        else:
            print('-1\n')    

    except:
        print('Error: You input wrong number.\n')    

