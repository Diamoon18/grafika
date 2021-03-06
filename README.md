
# Python 2d picture - burning flower

## These functions are for drawing circles. 
Function ``` circles ``` draw circles with a smaller radius on each iteration.
```python
def circles(t, size, small):
    for i in range(10):
        t.circle(size)
        size=size-small
```
Function ``` circle_direction ``` 
```python
def circle_direction(t, size, repeat, small):
  for i in range (repeat):
    circles(t,size,small)
    t.right(360/repeat)

```
## This function 
```python
def spiral(turtle, radius, color_name):
    for i in range(360 // ANGLE):
        turtle.color(color_name)
        turtle.circle(radius)
        turtle.left(ANGLE)
```


### Result:
![burning_flower](https://user-images.githubusercontent.com/72127610/110212868-b82f3980-7e9d-11eb-8745-d4d379ff2bff.jpg)
