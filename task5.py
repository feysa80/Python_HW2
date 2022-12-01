# Задача 5: Реализуйте алгоритм нахождения(генерации) рандомного(случайного) числа.
# (Не используя библиотеки связанные с рандомом)
import time


def rand_number():
    result = time.localtime().tm_sec * 359 // 26
    return result


print(rand_number())
