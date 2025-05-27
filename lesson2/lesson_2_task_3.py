from math import ceil

def square(part):
    area = part ** 2 
    return ceil(area)

part = int(input("Введите сторону квадрата: "))
area = square(part)
print(f'Площадь квадрата со стороной {part} равна {area}')
