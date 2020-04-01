if __name__ == "__main__":
    num_fib1 = 3
    num_fib2 = 5
    fib_sum = 0
    i = 5

    while i < 20:
        fib_sum = num_fib1 + num_fib2
        print(fib_sum, " ")
        num_fib1 = num_fib2
        num_fib2 = fib_sum
        i += 1

