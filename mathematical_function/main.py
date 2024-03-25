from mathematical_function.polygons.rectangle import Rectangle
from mathematical_function.polygons.square import Square


def get_input_polygon(polygon):
    base = input("Enter the base length: ")
    if polygon == 'rectangle' or polygon == '1':
        height = input("Enter the height length: ")
        return base, height
    return base


def calculation_for_square(polygon, retry):
    base = get_input_polygon(polygon)
    base = check_input(polygon, base)

    if retry <= 3 and base <= 0:
        retry += 1
        print(f'The length must be a positive number. Retry {retry}!')
        return calculation_for_square(polygon, retry)
    elif base > 0:
        square = Square(base)
        area = square.area()
        print(f'The area of the square is {area}')
        perimeter = square.perimeter()
        print(f'The perimeter of the square is {perimeter}')
        return area, perimeter


def check_input(polygon, base, height=None):
    base = float(base) if base.isdigit() else -1
    if polygon == 'rectangle' or polygon == '1':
        height = float(height) if height.isdigit() else -1
        return base, height
    return base


def calculation_for_rectangle(polygon, retry):
    base, height = get_input_polygon(polygon)
    base, height = check_input(polygon, base, height)

    if retry < 3 and (base <= 0 or height <= 0):
        retry += 1
        print(f'The lengths must be positive numbers. Retry {retry}!')
        return calculation_for_rectangle(polygon, retry)
    elif base > 0 and height > 0:
        rectangle = Rectangle(base, height)
        area = rectangle.area()
        print(f'The area of the rectangle is {area}')
        perimeter = rectangle.perimeter()
        print(f'The perimeter of the rectangle is {perimeter}')
        return area, perimeter


def main():
    polygon = input("Enter a polygon ((1) --> rectangle, (2) --> square): ")
    if polygon.lower() == 'rectangle' or polygon == '1':
        return calculation_for_rectangle(polygon.lower(), 0)
    elif polygon.lower() == 'square' or polygon == '2':
        return calculation_for_square(polygon.lower(), 0)
    else:
        print("Polygon not valid")
        return -1


if __name__ == '__main__':
    main()
