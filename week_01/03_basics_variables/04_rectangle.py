'''
Write the necessary code to display the area and perimeter of a rectangle
that has a width of 2.4 and a height of 6.4

'''

width = 2.4
height = 6.4

def rect_area(width, height):
    return width * height

def rect_peri(width, height):
    return width*2+height*2

print(rect_area(width,height), rect_peri(width,height))