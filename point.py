def autocast_point(fn):
    def wrapper(*args, **kwargs):
        return fn(*(Point(*arg) if type(arg) is tuple else arg for arg in args), **kwargs)
    return wrapper

class Point(tuple):
    def __new__(cls, x, y) -> None:
        return super(Point, cls).__new__(cls, (x,y))

    def __init__(self, x, y):
        self.x=x
        self.y=y

    @classmethod
    def _range(cls, start, stop, step):
        for i in range(start.x, stop.x, step.x):
            for j in range(start.y, stop.y, step.y):
                yield i,j 

    @classmethod
    def range(cls, *args):
        new_args = []
        for arg in args:
            match(arg):
                case Point(): new_args.append(arg)
                case tuple(): new_args.append(Point(*arg))
                case _: raise TypeError(f"{type(arg).__name__} object cannot be interpreted as a Point")

        args = new_args
        match(len(args)):
            case 1: return cls._range(Point(0,0), args[0], Point(1,1))
            case 2: return cls._range(args[0], args[1], Point(1,1))
            case 3: return cls._range(args[0], args[1], args[2])
            case _:
                if len(args) < 1: raise TypeError(f"range expected at least 1 argument, got {len(args)}")
                else: raise TypeError(f"range expected at most 3 arguments, got {len(args)}")


    @autocast_point
    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)

    @autocast_point
    def __sub__(self, other):
        return Point(self.x-other.x, self.y-other.y)

    def __neg__(self):
        return Point(-self.x, -self.y)


    @autocast_point
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    @autocast_point
    def __ne__(self, other):
        return self.x != other.x or self.y != other.y


    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"
