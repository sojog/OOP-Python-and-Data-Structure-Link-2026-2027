class Point:
    def __init__(self, x:int, y:int):
        self.__x = x
        self.__y = y
        
    def __str__(self):
        return f"({self.__x}, {self.__y})"

    def __bool__(self):
        return (self.__x != 0) or (self.__y != 0)

    def set_to_origin(self):
        self.__x = 0
        self.__y = 0

    def __iadd__(self, other):
        if isinstance(other, Point):
            self.__x += other._x
            self.__y += other._y
        elif isinstance(other, tuple):
            dx, dy = other
            self.__x += dx
            self.__y += dy
        return self