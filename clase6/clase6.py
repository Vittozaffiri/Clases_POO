from math import pi

def circle_area(radius):

    if not isinstance(radius, int):

        raise TypeError("el radio debe ser un número")

    if radius < 0:

        raise ValueError("El radio debe ser mayor que 0")


    else:

        return pi*radius ** 2

try:

    print(circle_area(5))
    print(circle_area(-1))
    print(circle_area(4))

except ValueError as ex:
    print("hubo un error")
    print(ex)

except TypeError as te:

    print("Hubo un error")
    print(te)

## exeptions
## custom exeptions 
