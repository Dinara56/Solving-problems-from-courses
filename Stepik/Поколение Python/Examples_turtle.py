#!/usr/bin/env python
# coding: utf-8

# # Черепашья графика

# - Для перемещения черепашки вперед на n пикселей применяется команда turtle.forward(n);
# - Для перемещения черепашки назад на n пикселей применяется команда turtle.backward(n);
# - Для перемещения черепашки вправо на angle градусов команда turtle.right(angle);
# - Для перемещения черепашки влево на angle градусов команда turtle.left(angle);
# - Команда turtle.setheading() применяется для установки углового направления черепашки с заданным углом. В качестве аргумента нужно указать желаемый угол;
# - Чтобы получить текущее угловое направление черепашки используется команда turtle.heading();
# - Для изменения внешнего вида используют команду shape(): (square (квадрат), arrow (стрелка), circle (круг), turtle (черепашка), triangle (треугольник), classic (классическая стрелка));

# Напишите программу, которая рисует прямоугольник.
# Программу нужно оформить в виде функции rectangle(width, height), 
# где width, height – ширина и высота прямоугольника.

import turtle

def rectangle(width, height):
  turtle.forward(width)
  turtle.left(90)
  turtle.forward(height)
  turtle.left(90)
  turtle.forward(width)
  turtle.left(90)
  turtle.forward(height)
  
w = int(input('Введити ширину = '))
h = int(input('Введити высоту = '))    
rectangle(w, h)

# Напишите программу, которая рисует правильный треугольник.
# Программу нужно оформить в виде функции triangle(side), где side – длина стороны треугольника в пикселях.

import turtle

def triangle(side):
  turtle.forward(side)
  turtle.left(120)
  turtle.forward(side)
  turtle.left(120)
  turtle.forward(side)
  
s = int(input('Введите длину стороны треугольника в пикселях = '))
triangle(s)

# Напишите программу, которая рисует изображенную фигуру, состоящую из трех квадратов.

import turtle

def square(side):
  turtle.setheading(85)
  for _ in range(3):
      turtle.left(25)
      for _ in range(4):
          turtle.forward(side)
          turtle.right(90)

s = int(input('Введите длину сторону квадрата = '))
square(s)

# Напишите программу, которая рисует изображенную фигуру из восьми квадратов.

import turtle
def square(side):
  for _ in range(4):
    turtle.forward(side)
    turtle.left(90)
    
for _ in range(8):
  turtle.left(45)
  square(120)

# Напишите программу, которая рисует правильный шестиугольник.
# Программу нужно оформить в виде функции hexagon(side), где side – длина стороны в пикселях.

import turtle

def hexagon(side):
  for _ in range(6):
      turtle.forward(side)
      turtle.left(60)
      
s = int(input('Введите длину сторону шестиугольника = '))
hexagon(s)

# Напишите программу, которая рисует соты.
# Убедись, что функция рисования шестиугольника возвращает черепашку в исходную точку.

import turtle

def hexagon(side):
  for _ in '1' * 6:
    turtle.forward(side)
    turtle.right(60)
    
def count(size, num):
  for _ in range(num):
    hexagon(size)
    turtle.right(120)
    turtle.forward(size)
    turtle.left(60)
    
count(60, 6)

# Напишите программу, которая рисует ромб с углами 

import turtle

def romb(length):
  turtle.forward(length)
  turtle.left(120)
  turtle.forward(length)
  turtle.left(60)
  turtle.forward(length)
  turtle.left(120)
  turtle.forward(length)
  
l = int(input('Введити длину = '))
romb(l)


# - Команда turtle.penup() поднимает перо, а команда turtle.pendown() – опускает;
# - Чтобы черепашка нарисовала круг, можно применить команду turtle.circle();
# - Для изменения ширины пера черепашки в пикселях можно применить команду turtle.pensize();
# - Для изменения цвета рисунка можно применить команду turtle.pencolor() (red (красный), green (зеленый), bluе (синий), yellow (желтый), cyan (сине-зелёный));
# - Для изменения фонового цвета графического окна можно применить команду turtle.Screen().bgcolor();
# - Команда turtle.clear() стирает все рисунки в графическом окне;
# - Команда turtle.reset() стирает все рисунки, имеющиеся в графическом окне, задает черный цвет рисунка и возвращает черепашку в исходное положение в центре экрана;
# - Команда turtle.clearscreen() стирает все рисунки в графическом окне, меняет цвет рисунка на черный, а цвет фона на белый, и возвращает черепашку в исходное положение в центре графического окна;

# Напишите программу, которая рисует пунктирную линию

import turtle

turtle.penup()
for _ in range(10):
  turtle.forward(20)
  turtle.dot(10)

# Напишите программу, которая рисует прямоугольник с точкой в каждом углу

import turtle

def rectangle(width, height):
  turtle.forward(width)
  turtle.dot()
  turtle.left(90)
  turtle.forward(height)
  turtle.dot()
  turtle.left(90)
  turtle.forward(width)
  turtle.dot()
  turtle.left(90)
  turtle.forward(height)
  turtle.dot()
  
w = int(input('Введити ширину = '))
h = int(input('Введити высоту = '))    
rectangle(w, h)

# Напишите программу, которая рисует черепашек в соответствии с образцом.

import turtle

import turtle
def turtle_moshpit(turtles):
  turtle.penup()
  turtle.shape('turtle')
  turtle.stamp()
  for _ in range(turtles):
    for i in ['red','yellow','green','orange','blue','purple'] * 2:
      turtle.color(i)
      turtle.forward(50)
      turtle.stamp()
      turtle.backward(50)
      turtle.left(360 / turtles)
    
turtle_moshpit(20)

# Напишите программу, которая рисует узор в соответствии с образцом.

import turtle

colors=['red', 'blue', 'yellow', 'green', 'purple', 'orange']
s=1
n=5
for i in range(8):
  for j in colors:
    turtle.pensize(s)
    turtle.pencolor(j)
    turtle.forward(n)
    turtle.left(45)
    n+=3
  s+=2


# - Для перемещения черепашки в конкретную позицию в графическом окне применяется команда turtle.goto();
# - Команда turtle.pos() возвращает кортеж с x и y координатами черепашки;
# - Для получения только координаты x черепашки служит команда turtle.xcor(), а для получения координаты y – команда turtle.ycor();
# - Для изменения скорости движения черепашки можно применить команду turtle.speed();

# Напишите программу, которая рисует изображение мишки.

import turtle as t
t.circle(-60)
t.penup()
t.goto(0,-35)
t.pendown()
t.circle(10)
t.goto(0,-90)
t.penup()
t.goto(0,-120)
t.pendown()
t.circle(120)
t.penup()
t.goto(90,90)
t.pendown()
t.circle(35)
t.penup()
t.goto(-90,90)
t.pendown()
t.circle(35)
t.penup()
t.goto(55,-5)
t.pendown()
t.dot(23)
t.penup()
t.goto(-55,-5)
t.pendown()
t.dot(23)

