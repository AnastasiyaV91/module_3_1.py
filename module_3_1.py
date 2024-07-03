calls = 0                           # Создаем переменную calls = 0 для счетчика проходов.

def count_calls():                  # Создаем функцию count_calls и изменять в ней значение .
    global calls                    # переменной calls. Эта функция должна вызываться в остальных двух функциях
    calls += 1

def string_info(string):                                              # Создаем функцию string_info с аргументом string
    count_calls()                                                     # Счетчик проходов
    string1 = tuple()                                                 # Создаем пустой кортеж
    string1 = len(string), str(string.upper()), str(string.lower())   # Наполняем кортеж данными
    print(string1)                                                    # Выводим результат в консоль

def is_contains(b,c):                                                 # Создаем функцию is_contains с двумя параметрами b (строка) и c (список)
    count_calls()                                                     # Счетчик проходов
    b1 = b.lower()                                                    # b (строка) переводим в нижний регистр и присваиваем переменной b1
    new_c = [x.lower() for x in c]                                    # c (строка) переводим в нижний регистр и присваиваем переменной new_c
    if b1 in new_c:                                                   # Сравниваем b1 c элементами списка new_c
        index = new_c.index(b1)                                       # Находим индекс найденного элемента
        print("True")                                                 # Выводим результат в консоль
    else:
        print("False")                                                # Если элемент не найден в списке new_c, то выводим в консоль  False

# Вызываем функции

string_info("Capybara")
string_info("Armageddon")
is_contains("Urban", ["ban", "BaNaN", "urBAN"])
is_contains("cycle", ["recycling", "cyclic"])
print(calls)                                            # Выводим результат счетчика проходов