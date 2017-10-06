# we need the math library because it has a really good estimate of pi
import math

# fill in the function called "calculate_pi" that returns a value as close as possible to the real_pi
# level 1: accurate to 2 decimal places (3.14.....)
# level 2: accurate to 10 decimal places (3.1415926535.....)
# level 3: who in the class can get the smallest difference to the real value of pi? (maximum 30 second compute time)

# this is the function you have to fill in
def calculate_pi():
    calculated_value = 3  # you actually have to calculate it here, not just print out a value
    return calculated_value

# call the function I just wrote
my_pi = calculate_pi()

# print out the difference with a "real" value of pi
print (math.pi - my_pi)

