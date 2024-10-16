print(Пример аргументов и параметров функции)
def example(color):
    if color == "green":
        return "This is grass"
    elif color == "blue":
        return "This is water"
    else:
        return "I dont know"
what_is_it = example('blue')
print(what_is_it)

def dog(name, color, age):
    return {'name': name, 'color': color, 'age': age}

my_dog = dog('Lisa', 'Brown', '7')
print(my_dog)

