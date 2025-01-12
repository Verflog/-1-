def is_prime(number):
    if number <= 1:
        print(number, "не является простым")
    else:
        k = 0
        for i in range(2, number):
            if number % i == 0:
                k += 1
            if k != 0:
                print(number, "не является простым")
                break
        else:
            print(number, "является простым")
