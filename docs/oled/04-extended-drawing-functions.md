# Extending Drawing Functions

## Circle

If we assume we have a 64x128 display we can call two circle functions to draw eyes

display.fill(0)  # Clear the display.
display.circle(32, 32, 10, 1) # draw the left eye

Here are the parameters for circle functions

1. X position of the circle center
2. Y position of the circle center
3. Radius of the circle in pixels
4. The color of the drawing, 1 for on and 0 for off.

## Fill Circle

This similar to the circle, but pixels internal to the circle are filled.

## Sample Code

For each pixel in the "square" bounding box that surrounds the circle, we need to do a little math to see if the pixel is inside or outside of the circle.

```py
def fill_circle(framebuffer, x, y, radius, fill):
    for x in range(left-edge, right-edge):
        for y in range(top-edge, bottom-edge):
            if in_circle(x, y, r):
                set(framebuffer(x, y, 1)
```

Now all we need to do is write a function called in_circle() to turn the pixel on.  We can use some basic geometry to see if a point at x,y is within the radius by using the distance function.

distance = sqrt(x*x + y*y)

```py
def in_circle(x, y, radis):
    point_distance = sqrt(x*x + y*y)
    if point_distance < radis:
        return 1
    elif:
         return 0
```