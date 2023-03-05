from figures.circle import circle_area, circle_perimeter
from figures.triangle import triangle_perimeter, triangle_area
from figures.square import square_perimeter, square_area

tests = (
    (circle_area, ()),
    (circle_area, (5,)),
    (circle_perimeter, ()),
    (circle_perimeter, (5,)),
    (triangle_area, ()),
    (triangle_area, (2, 3, 4,)),
    (triangle_perimeter, ()),
    (triangle_perimeter, (2, 3, 4,)),
    (square_area, ()),
    (square_area, (10,)),
    (square_perimeter, ()),
    (square_perimeter, (10,)),
)

for f, args in tests:
    print(f'{f.__name__}{args} -> {f(*args)}')
