#zadacha2-1
length=float(input("Введите длину прямоугольника: "))
width=float(input("Введите ширину прямоугольника: "))
person=int(input("введите количество"))
area=(length*width)*person
perimeter=((length+width)*2)*person
print(f"Периметр = {perimeter} см Площадь = {area} см")
