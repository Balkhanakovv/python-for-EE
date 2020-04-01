if __name__ == "__main__":
    num1 = 42
    num2 = 33

    print('\twith "and"\n')
    print(num1 > 0 and num2 > 0, '\n')
    print(num1 == 42 and num2 == 33, '\n')
    print(num1 < 0 and num2 > 0, '\n')
    print(num1 != 42 and num2 == 33, '\n')

    print('\n\twith "or"\n')
    print(num1 > 0 or num2 > 0, '\n')
    print(num1 == 42 or num2 == 33, '\n')
    print(num1 < 0 or num2 == 0, '\n')
    print(num1 != 42 or num2 != 33, '\n')


    str1 = 'a'
    str2 = 'z'

    print('\n\twith strings\n')
    print(str1 == 'a' and str2 > str1, '\n')
