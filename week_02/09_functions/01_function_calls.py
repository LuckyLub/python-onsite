'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''


def volume_circle(r):
    from math import pi
    return pi * (r ** 2)


def volume_column(r, h):
    return volume_circle(r) * h


def cost_column(r, h, costs):
    return round(volume_column(r, h) * costs, 2)


radius = 1
height = 3
costs_per_cubic_m = 120

print(f'The costs of a_column with a radius of {radius}, height of {height} and costs per cubic meter of '
      f'{costs_per_cubic_m} is : {cost_column(radius, height, costs_per_cubic_m)}.')

