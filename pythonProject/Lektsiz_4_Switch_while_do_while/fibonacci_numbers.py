n = int(input("Введите целое число: "))
n_1 = 1
n_2 = 0
print(n_2, end=' ')

for i in range(n):
    n_2 = n_1 + n_2
    n_1 = n_2 - n_1
    print(n_2, end=' ')
