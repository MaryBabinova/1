import cmath
from math import sqrt
def f1():
    print("Программа для поиска корней квадратного уравнения\nВведите коэффициенты:")
    a=float(input("a="))
    b=float(input("b="))
    c=float(input("c="))
    D=b*b-4*a*c
    if D>0:
        print("Уравнение имеет действительные корни")
        x1=round((-b+sqrt(D))/(2*a))
        x2=round((-b-sqrt(D))/(2*a))
        print("X1=",x1,"\nX2=",x2)
    elif D==0:
        x1=(-b)/(2*a)
        print("Уравнение имеет единственный действительный корень")
        print("X1=",x1)
    else:
        print("Уравнение имеет комплексно сопряженные корни")
        x1=(-b+cmath.sqrt(D))/(2*a)
        x2=(-b-cmath.sqrt(D))/(2*a)
        print("X1=",x1,"\nX2=",x2)
def f2():
    temp=[36.6,37.2,34.1,39.3,33.0,32.3,35.3,42.5,45.3,80.1,35.1]
    j=0
    for i in temp:
        if i<33.0 or i>41.9:
            print("Ошибка! Предыдущее значение:",j)
            
            continue
        else:
            j=i
        print(i, end=' ')

def f3():
    N=int(input('Введите правую границу:'))
    if N<5:
        print('Ну уж побольше введи')
    else:
        for i in range(5,N+1):
            print(i,'->',pow(i,3))
def f4():
    i=1
    log=input("Login:")
    pas=input("Password:")
    while i<3:
        if log=='mary' and pas=='kisa':
          print("Good");break
        else:
            print("Wrong login or password")
            print("Осталось {} попыток".format(3-i))
            log=input("Login:")
            pas=input("Password:")
            i+=1
    if i==3:
        print("Мда....\nПопыток не осталось")
def f5():
    import sys
    import turtle
    def border(t, screen_x, screen_y):
        t.penup()
        t.home()
        t.forward(screen_x / 2)
        t.right(90)
        t.forward(screen_y / 2)
        t.setheading(180)
        t.pencolor('red')
        t.pendown()
        t.pensize(10)
        for distance in (screen_x, screen_y, screen_x, screen_y):
            t.forward(distance)
            t.right(90)
        t.penup()
        t.home()
    def square(t, size, color):
        t.pencolor(color)
        t.pendown()
        for i in range(4):
            t.forward(size)
            t.right(90)
    def main():
        screen = turtle.Screen()
        screen.title('Square Demo')
        screen_x, screen_y = screen.screensize()
        t = turtle.Turtle()
        border(t, screen_x, screen_y)
        colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
        t.pensize(3)
        for i, color in enumerate(colors):
            square(t, (screen_y / 2) / 10 * (i+1), color)
        print('Hit any key to exit')
        dummy = input()
    if __name__ == '__main__':
        main()
def f6():
    import turtle
    help(turtle)

