def add_everything_up(a, b):
    if type(a) == (int) and type(a) == float and type(b) == (int) and type(b) == float:
        print(a + b)

    elif type(a) == type(b):
        print(a + b)

    else:
        try:
            print (a + b)

        except TypeError:
            print(str(a) + str(b))
            print(f"Ошибка ввода типа данных:\n a = {a} тип данных - {type(a)}\n b = {b} тип данных - {type(b)}")

        finally:
            print("Задание выполнено")






# add_everything_up(1, "1")
add_everything_up(123.456, 'строка')
add_everything_up('яблоко', 4215)
add_everything_up(123.456, 7)