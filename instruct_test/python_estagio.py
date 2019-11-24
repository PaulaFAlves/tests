


import math


class Point():
    """
    A two-dimensional Point with an x and an y value

    >>> Point(0.0, 0.0)
    Point(0.0, 0.0)
    >>> Point(1.0, 0.0).x
    1.0
    >>> Point(0.0, 2.0).y
    2.0
    >>> Point(y = 3.0, x = 1.0).y
    3.0
    >>> Point(1, 2)
    Traceback (most recent call last):
        ...
    ValueError: both coordinates value must be float
    >>> a = Point(0.0, 1.0)
    >>> a.x
    0.0
    >>> a.x = 3.0
    >>> a.x
    3.0
    """

    def __init__(self, x, y):
        # self.x = self.define_xy()
        self.x = x
        self.y = y

        n = type(x)
        if n == int:
            raise ValueError('both coordinates value must be float')

    def __repr__(self):
        return f"{self.__class__.__name__}({self.x!r}, {self.y!r})"




def euclidean_distance(a, b):
    """
    Returns the euclidean distance between Point a and Point b

    >>> euclidean_distance(Point(0.0, 0.0), Point(3.0, 4.0))
    5.0
    >>> euclidean_distance((0.0, 0.0), (3.0, 4.0))
    Traceback (most recent call last):
        ...
    ValueError: a must be a Point
    >>> euclidean_distance(Point(0.0, 0.0), (3.0, 4.0))
    Traceback (most recent call last):
        ...
    ValueError: b must be a Point
    """
    if type(a) != Point:
        raise ValueError('a must be a Point')
    elif type(b) != Point:
        raise ValueError('b must be a Point')
    
    r = (a.x + b.x)**2 + (a.y + b.y)**2
    return math.sqrt(r)


    #     num1 = Point(0.0, 0.0)
    #     x1 = num1.x
    #     y1 = num1.y
    #     num2 = Point(3.0, 4.0)
    #     x2 = num2.x
    #     y2 = num2.y

    #     r = ((x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2))
    # return math.sqrt(r)


def manhattan_distance(a, b):
    """
    Returns the manhattan distance between Point a and Point b

    >>> manhattan_distance(Point(0.0, 0.0), Point(3.0, 4.0))
    7.0
    >>> manhattan_distance((0.0, 0.0), (3.0, 4.0))
    Traceback (most recent call last):
        ...
    ValueError: a must be a Point
    >>> manhattan_distance(Point(0.0, 0.0), (3.0, 4.0))
    Traceback (most recent call last):
        ...
    ValueError: b must be a Point
    """

    if type(a) != Point:
        raise ValueError('a must be a Point')
    elif type(b) != Point:
        raise ValueError('b must be a Point')
    
    r = (a.x - b.x) + (a.y - b.y)
    return math.fabs(r)



if __name__ == "__main__":
    import doctest

    doctest.testmod()
