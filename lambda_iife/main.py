celsius_temperature = 23

# The `lambda` function for converting temperature 
# from `celsius_temperature` variable to fahrenheit temperature 
fahrenheit_temperature = (lambda celsius:(9/5)*celsius + 32)(celsius_temperature)

# Testing the result
print(f"{celsius_temperature} degrees Celsius is equal to {fahrenheit_temperature} degrees Fahrenheit")