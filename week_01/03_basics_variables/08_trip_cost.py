'''
Receive the following arguments from the user:
    - miles to drive
    - MPG of the car
    - Price per gallon of fuel

Display the cost of the trip in the console.

'''

miles = float(input("What distance are you going to drive?"))
rate = float(input("How many miles can the car drive per gallon?"))/10
price = float(input("What is the price per gallon of fuel?"))


def cost_of_ride(distance, usage_rate, fuelprice):
    return distance*usage_rate*fuelprice


print("It will cost you: ", cost_of_ride(miles, rate, price))