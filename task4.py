# Задача 4: Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
n = int(input('Введите число N: '))
n_list = [i for i in range(-abs(n), n+1)]
print(n_list)
path = 'file.txt'
data = open(path, 'r')
result = 1
for line in data:
    result *= n_list[int(line) - 1]
print(f'Результат равен {result}')




