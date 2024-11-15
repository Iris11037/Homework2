def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for m in numbers:
        try:
           result += m
        except TypeError as exc:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {m}')
    return result, incorrect_data

def calculate_average(numbers):
    try:
        sum8, incorrect = personal_sum(numbers)
        del8 = sum8 / (len(numbers) - incorrect)
        return del8
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None

print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
