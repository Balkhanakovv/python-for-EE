if __name__ == "__main__":
    #Первое задание
    def func1(num):
        n = num * 5
        print(n)

    global_var = 42

    func1(global_var)
    func1(10)
    func1('bla')



    #Второе задание
    def func(n):
        if n < 3:
            n = n * 10

        return n
        