a = float(input("Введите число A: "))
n = int(input("Введите число N: "))

result = 1

for i in range(abs(n)):
    result *= a

if n < 0:
    result = 1 / result

print("Результат:", result)