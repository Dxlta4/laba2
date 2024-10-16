def get_number():
    for num in range(30):
        if num % 2 != 0:
            yield num

gen = get_number()

first = None
fifth = None
last = None

for i, val in enumerate(gen, start=1):
    if i == 1:
        first = val
    if i == 5:
        fifth = val
    last = val  

print("Первое нечетное число:", first)
print("Пятое нечетное число:", fifth)
print("Последнее нечетное число:", last)
