
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
Function ``` circle_direction ``` uses the ``` circles ``` function and draw circles in round direction (0-360 digrees)
```python
def circle_direction(t, size, repeat, small):
  for i in range (repeat):
    circles(t,size,small)
    t.right(360/repeat)

```
## This function draw circles in spiral direction // po krugu
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
    screen.bgcolor("black")
    screen.title('Burning flower')
```
Create an object
```python
    eye = Turtle(visible=False)
    eye.speed("fastest")

    spiral(eye, 100, color)
    spiral(eye, 50, color2)
    spiral(eye, 25, color1)
```

### Result:
![burning_flower](https://user-images.githubusercontent.com/72127610/110212868-b82f3980-7e9d-11eb-8745-d4d379ff2bff.jpg)
