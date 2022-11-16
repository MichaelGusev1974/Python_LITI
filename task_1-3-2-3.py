# Прочитайте список с клавиатуры (элементы, целые числа, разделены пробелом). Составьте список пар:
# (индекс, значение списка). Выведите получившийся список на экран.

L = [int(i) for i in input().split()]

L1 = [(inx, item) for inx, item in enumerate(L)]
print(L1)

# print([(inx, item) for inx, item in enumerate([int(i) for i in input().split()])])
