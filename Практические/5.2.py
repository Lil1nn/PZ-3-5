def ShiftLeft3(A, B, C):
    temp = A
    A = C
    C = B
    B = temp
    return A, B, C

A1 = float(input("Введите значение A1: "))
B1 = float(input("Введите значение B1: "))
C1 = float(input("Введите значение C1: "))

A2 = float(input("Введите значение A2: "))
B2 = float(input("Введите значение B2: "))
C2 = float(input("Введите значение C2: "))

A1, B1, C1 = ShiftLeft3(A1, B1, C1)
A2, B2, C2 = ShiftLeft3(A2, B2, C2)

print("Результат для набора (A1, B1, C1):", A1, B1, C1)
print("Результат для набора (A2, B2, C2):", A2, B2, C2)