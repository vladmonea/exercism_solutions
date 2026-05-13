def is_triangle(func):
    def check_sides(sides):
        if any([side <= 0 for side in sides]):
            return False
        elif sides[0] + sides[1] < sides[2] or sides[1] + sides[2] < sides[0] or sides[2] + sides[0] < sides[1]:
            return False
        else:
            return func(sides)
    return check_sides


@is_triangle
def is_equilateral(sides):
    return sides[0] == sides[1] == sides[2]


@is_triangle
def is_isosceles(sides):
    two_sides_equal = sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]
    return two_sides_equal


@is_triangle
def is_scalene(sides):
    return sides[0] != sides[1] != sides[2]


def is_degenerate(sides):
    return sides[0] + sides[1] == sides[2] or sides[1] + sides[2] == sides[0] or sides[2] + sides[0] == sides[1]
