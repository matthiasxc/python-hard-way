# describe what we're about to do
print("I will now count my chickens:")

# 25 + (30 / 6) = 30.0
print("Hens", 25 + 30 / 6)
# 100 - ((25 * 3) % 4) = 100 - (75 % 4) = 100 - 3
print("Roosters", 100 - 25 * 3 % 4)

print("Now I will count the eggs:")

# I'm kind of assuming that the below code runs like this:
# 3 + 2 + 1 - 5 + (4 % 2) - (1 / 4) + 6
# 6 - 5 + (0) - (0.25) + 6
# 1 - 0.25 + 6 = 5.75
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

print("Is it true that 3 + 2 < 5 - 7?")
# 5 < -2? no
print(3 + 2 < 5 - 7)

print("What is 3 + 2?", 3 + 2)
print("What is 5 - 7?", 5 - 7)

print("Oh, that's why it's False.")

print("How about some more.")

# intersting... pylint tells me that I should be putting -2 on the
# other side of that equation
print("Is it greater?", 5 > -2)
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)
