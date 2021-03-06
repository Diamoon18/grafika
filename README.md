
# Python 2d picture - burning flower
I found an amazing library ```turtle```, that helps me to draw a flower.
It is quite easy to use and allows you to draw interisting things.

## Using functions from the ```turtle``` library 
```python
from turtle import Turtle, Screen
```
## These functions are for drawing circles. 
Function ``` circles ``` make circles with a smaller radius on each iteration.
```python
def circles(t, size, small):
    for i in range(10):
        t.circle(size)
        size=size-small
```
Function ``` circle_direction ``` uses the ``` circles ``` function and draws circles-crescents in circular direction.
```python
def circle_direction(t, size, repeat, small):
  for i in range (repeat):
    circles(t, size, small)
    t.right(360/repeat)

```
## This function draw circles in spiral direction
```python
def spiral(turtle, radius, color_name):
    for i in range(360 // ANGLE):
        turtle.color(color_name)
        turtle.circle(radius)
        turtle.left(ANGLE)
```
## Main function
A window for the picture, black background and the name of the window.
```python
    screen = Screen()
    screen.bgcolor('black')
    screen.title('Burning flower')
```
Create an object turtle.
```python
    eye = Turtle(visible=False)
    eye.speed('fastest')
```
Call the ```spiral``` function and draw something that looks like an eye.
```python
    spiral(eye, 100, color)
    spiral(eye, 50, color2)
    spiral(eye, 25, color1)
```
![etap1](https://user-images.githubusercontent.com/72127610/110216250-562b0000-7eae-11eb-88f1-e61142ed177e.jpg)

Create new object turtle and call the ```circle_direction``` the function of drawing large red circles in the form of a crescent.
```python
    s = Turtle(visible=False)
    s.speed('fastest')
    s.color('red')
    circle_direction(s, 200, 10, 4)
```
![etap2](https://user-images.githubusercontent.com/72127610/110216438-7c9d6b00-7eaf-11eb-9501-cc036567fb2b.jpg)

Create new object turtle and call the ```circle_direction``` the function of drawing large, smaller than red, yellow circles in the form of a crescent.
```python
    t1 = Turtle(visible=False)
    t1.speed(0)
    t1.color('yellow')
    circle_direction(t1, 160, 10, 10)
```
![etap3](https://user-images.githubusercontent.com/72127610/110216638-7491fb00-7eb0-11eb-9b67-c762ac47424e.jpg)

And the last draw the core of the flower. Call the ```spiral``` function.
To prevent the window from closing immediately, call the ```exitonclick``` function.
```python
spiral(eye, 10, color3)
screen.exitonclick()
```

## Result:
![burning_flower](https://user-images.githubusercontent.com/72127610/110212868-b82f3980-7e9d-11eb-8745-d4d379ff2bff.jpg)
