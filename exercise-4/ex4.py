# number of cars
cars = 100
# number of seats in a car
space_in_a_car = 4
# number of available drivers
drivers = 30
# total number of passengers (including drivers)
passengers = 90
# number of cars we cannot drive due to lack of drivers
cars_not_driven = cars - drivers
# only 1 driver per car
cars_driven = drivers
# the total passenger capacity of these cars
carpool_capacity = cars_driven * space_in_a_car
# the number of passengers we can have in each car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available")
print("There are only", drivers, "drivers available")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car")
