'''
In the U.S., if there is:
    - One person who is born every 6 seconds
    - One person who dies every 12 seconds
    - One person who immigrates every 40 seconds

Write the necessary code to display the total population
for the next 3 years (without a leap year).
Let's say the current population is 380,123,456.

'''

born_interval = 1/6
death_interval = 1/12
imigrate_interval = 1/40
current_population = 380123456

def future_population(born, death, current, year):
    import datetime
    year_delta_sec= ((year-2019)*365*24*60*60)
    return current+ year_delta_sec * (born_interval-death_interval-imigrate_interval)

print("population 2020: ", future_population(born_interval, death_interval,current_population,2020))
print("population 2021: ", future_population(born_interval, death_interval,current_population,2021))
print("population 2022: ", future_population(born_interval, death_interval,current_population,2022))
