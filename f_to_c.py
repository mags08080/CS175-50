# CS 175
# Maggie Volker

#f_to_c

#converting fahrenheit temperature celsius
degreesFahrenheit = float(input("Enter the temperature in degrees Fahrenheit: "))
#designing formula for conversion
fahrenheitConstant = 32
conversionNumber = 5/9
#forumla
degreesCelsius = (degreesFahrenheit - fahrenheitConstant) * conversionNumber

print(f"The temperature converted to degrees celsius is: {degreesCelsius}")