'''
Take in a number from the user and print "Monday", "Tuesday", ...
"Sunday", or "Other" if the number from the user is 1, 2,... 7,
or other respectively. Use a "nested-if" statement.

'''

user_number = int(input("Give me a number between 1 and 7!"))
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

while user_number < 0 or user_number > 7:
    user_number = int(input("That's an invalid number. Give me a number between 1 and 7!"))

print(days[user_number-1])

# I know I didn't used a nested-if statement, but this is so much faster.