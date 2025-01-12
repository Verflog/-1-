def greet(name):
    print("Привет,", name, "!")

def square(number):
    return number * number

def max_of_two(x, y):
    if x > y:
        return x
    elif y > x:
        return y
    else:
        return "equal"

def describe_person(name, age=30):
    print("Имя:", name, "/ Возраст:", age)

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

greet("Всеволод")
print(square(7))
print(max_of_two(-9, 8))
describe_person("Олеся")
is_prime(101)