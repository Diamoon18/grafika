import turtle
from turtle import Turtle, Screen

ANGLE  = 2
color1 = 'black'
color  = 'blue'
color2 = 'red'
color3 = 'yellow'

def circles(t, size, small):
    for i in range(10):
        t.circle(size)
        size=size-small

def circle_small(t, size, repeat, small):
  for i in range (repeat):
    circles(t, size, small)
    t.right(360/repeat)

def spiral(turtle, radius, color_name):
    for i in range(360 // ANGLE):
        turtle.color(color_name)
        turtle.circle(radius)
        turtle.left(ANGLE)

def main():
    screen = Screen()
    screen.bgcolor('black')

    eye = Turtle(visible=False)
    eye.speed('fastest')

    spiral(eye, 100, color)
    spiral(eye, 50, color2)
    spiral(eye, 25, color1)

    s = turtle.Turtle(visible=False)
    s.speed('fastest')
    s.color('red')
    circle_small(s, 200, 10, 4)

    t1 = turtle.Turtle(visible=False)
    t1.speed(0)
    t1.color('yellow')
    circle_small(t1, 160, 10, 10)

    spiral(eye, 10, color3)

    screen.exitonclick()

if __name__ == "__main__":
    main()

