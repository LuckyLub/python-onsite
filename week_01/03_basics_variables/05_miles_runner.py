'''
If a runner runs 12 kilometers in 30 minutes and 30 seconds.
What is his/her average speed in miles per hour. (Tip: 1 mile = 1.6 km)

'''

distance = 12
time = 30.5

def convert_miles2km(distance):
    return distance*1.60934


def convert_min2h(time):
    return time/60


def averagespeed(distance, time):
    return distance/time


print(averagespeed(convert_miles2km(distance), convert_min2h(time)))
