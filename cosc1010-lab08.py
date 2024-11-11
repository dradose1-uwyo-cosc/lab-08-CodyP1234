# Cody Phillips
# UWYO COSC 1010
# Due 11/10/2024
# Lab 08
# Lab Section:
# Sources, people worked with, help given to:
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 


print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null

import math

def convert_string(s):
    try:
        if '.' in s:
            return float(s) if s.count('.') == 1 else False
        else:
            return int(s)
    except ValueError:
        return False

def slope_intercept(m, b_slope, x_lower, x_upper):
    if not (isinstance(x_lower, int) and isinstance(x_upper, int)):
        return False
    if x_lower > x_upper:
        return False
    
    y_values = []
    for x in range(x_lower, x_upper + 1):
        y = m * x + b_slope
        y_values.append(y)
    
    return y_values

def quadratic_formula(a, b_quad, c):
    discriminant = b_quad**2 - 4*a*c
    if discriminant < 0:
        return None  
    
    sqrt_discriminant = math.sqrt(discriminant)
    x1 = (-b_quad + sqrt_discriminant) / (2 * a)
    x2 = (-b_quad - sqrt_discriminant) / (2 * a)
    
    return (x1, x2)

def sqrt_help(number):
    if number < 0:
        return None
    return math.sqrt(number)

def main():
    while True:
        print("Enter 'exit' to quit.")
        
        m = input("Enter the slope (m): ")
        b_slope = input("Enter the y-intercept (b): ")
        x_lower = input("Enter the lower x bound: ")
        x_upper = input("Enter the upper x bound: ")
        
        if m == "exit" or b_slope == "exit" or x_lower == "exit" or x_upper == "exit":
            break
        
        m = convert_string(m)
        b_slope = convert_string(b_slope)
        x_lower = convert_string(x_lower)
        x_upper = convert_string(x_upper)
        
        if m is False or b_slope is False or x_lower is False or x_upper is False:
            print("Invalid input. Please enter valid numbers.")
            continue
        
        result = slope_intercept(m, b_slope, x_lower, x_upper)
        if result is False:
            print("Invalid x bounds or range.")
            continue
        print("Slope-Intercept Results:", result)
        
        a = input("Enter coefficient a for quadratic equation: ")
        b_quad = input("Enter coefficient b for quadratic equation: ")
        c = input("Enter coefficient c for quadratic equation: ")
        
        if a == "exit" or b_quad == "exit" or c == "exit":
            break
        
        a = convert_string(a)
        b_quad = convert_string(b_quad)
        c = convert_string(c)
        
        if a is False or b_quad is False or c is False:
            print("Invalid input for quadratic equation. Please enter valid numbers.")
            continue
        
        roots = quadratic_formula(a, b_quad, c)
        if roots is None:
            print("No real roots exist for the given quadratic equation.")
        else:
            print("Quadratic Roots:", roots)
        
        num = input("Enter a number to find its square root: ")
        if num == "exit":
            break
        
        num = convert_string(num)
        if num is False:
            print("Invalid input for square root calculation.")
            continue
        
        root_result = sqrt_help(num)
        if root_result is None:
            print("Cannot compute the square root of a negative number.")
        else:
            print("Square Root:", root_result)

main()