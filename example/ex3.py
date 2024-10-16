print(Пример внутренней функции без замыкания)

def outer(out_param):
    def inner(in_param):
        return f'Outer def have value: {in_param}'
    return inner(out_param)

print(outer('TEST'))

print(Пример с замыканием)
    def outer2(out_param):
        def inner2():
            return f'Outer def have value: {out_param}'
    return inner2

value = outer2('TEST')
print(value())

