'''1. Реализуйте рекурсивную функцию нарезания прямоугольника с заданными пользователем сторонами a и b
на квадраты с наибольшей возможной на каждом этапе стороной.
Выведите длины ребер получаемых квадратов и кол-во полученных квадратов.'''


def squares(a, b, i=0):
    if a > b:
        i+=1
        print(b)
        squares(a-b, b, i)
    elif a<b:
        i+=1
        print(a)
        squares(a, b-a, i)
    else:
        print(a)
        i+=1
        print("Number of squares is "+str(i))

a = int(input("Input 1st dimension of a rectangle \n"))
b = int(input("Input 2nd dimension of a rectangle \n"))

print('\n')
squares(a, b)
