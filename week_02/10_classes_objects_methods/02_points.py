'''
Work through the chapter "Classes and Objects" in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2016.html and
build out the Point class example.

'''


class Point:
    """Represents a point in 2-D space."""
    def __init__(self, x = None, y = None):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point({self.x}, {self.y})'

    def print_point(self):
        print((self.x, self.y))

    def clossest_point(self, list_):
        distance_list= []

        for i in range(list_.__len__()):
            x = list_[i].x - self.x
            y = list_[i].y - self.y
            distance = (list_[i], ((x**2 + y**2)**(1/2)))
            distance_list.append(distance)

        return min(distance_list, key=lambda x:x[1])


a = Point(0, 0)
b = Point(1, 2)
c = Point(1, 10)
d = Point(5, 5)

cp, d = d.clossest_point([a, b, c])
print(cp, d)
