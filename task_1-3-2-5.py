# На вход программе подается некоторое количество предложений, разделенных символом табуляции ('\t').
# С помощью метода строк strip() уберите пробельные символы в начале и конце каждого предложения. Далее подсчитайте,
# какое предложение встречается в тексте наибольшее число раз, и выведите это число повторений на экран.

L = input().strip().split('\\t')
print(L)
# Ls = []
# for i in range(len(L)):
#     num = L.count(L[i])
#     Ls.append(num)
# print(max(Ls))

print(max([L.count(L[i]) for i in range(len(L))]))

# вывод: aa\tbb\tcc\taa\tbb\tcc\taa\tbb\tcc\taa\taa\tbb\tcc\taa\taa\tbb\tcc\taa
# ['aa', 'bb', 'cc', 'aa', 'bb', 'cc', 'aa', 'bb', 'cc', 'aa', 'aa', 'bb', 'cc', 'aa', 'aa', 'bb', 'cc', 'aa']
# 8




