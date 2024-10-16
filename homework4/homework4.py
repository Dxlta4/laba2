def find_multiples():
    X = int(input("Введите цифру X: "))

    numbers = [(i * 37) % 201 for i in range(10)]

    multiples = list(filter(lambda n: n % X == 0, numbers))

    print("Сгенерированные числа:", numbers)
    print("Числа, кратные", X, ":", multiples)

find_multiples()
