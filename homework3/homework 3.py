def input_date(prompt):
    while True:
        try:
            day, month, year = map(int, input(prompt).split('/'))
            if 1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2100:
                return year, month, day
            else:
                print("Пожалуйста, введите корректную дату.")
        except ValueError:
            print("Пожалуйста, введите дату в формате день/месяц/год.")

def calculate_age(birth_year, birth_month, birth_day):
    today = get_current_date()
    
    if (today[1], today[2]) < (birth_month, birth_day):
        return today[0] - birth_year - 1
    else:
        return today[0] - birth_year

def get_current_date():
    month_days = [31, 28, 28, 31, 30, 31, 31, 31, 30, 31, 30, 31]
    current_month = int(input("Введите текущий месяц: "))
    current_day = int(input(f"Введите количество дней в {current_month}-м месяце: "))
    current_year = int(input("Введите текущий год: "))
    return current_year, current_month, current_day

print("Введите вашу дату рождения в формате день/месяц/год:")
year, month, day = input_date("Ваша дата рождения: ")
age = calculate_age(year, month, day)
print(f"Ваш возраст: {age} лет")
