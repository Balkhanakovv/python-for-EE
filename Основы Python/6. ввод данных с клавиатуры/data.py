if __name__ == "__main__":
    try:
        print('What is your name?')
        name = input()

        print('How old are you?')
        age = int(input())

        print('Where are you live?')
        locate = input()

        print('\nThis is ', name, '\n')
        print('It is ', age, '\n')
        print('He/She live in ', locate, '\n')
    except:
        print('Wrong age!!!');