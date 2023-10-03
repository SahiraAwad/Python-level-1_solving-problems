'''*****************************Python  Task level 3**********************************************
1. Make a temperature/measurement converter. Write a script that can convert
Fahrenheit to Celcius and back, or inches to centimeters and back, etc in 3 different
ways
_________________________________________________________________________________________________


'''


# convert Fahrenheit to Celcius
fahrenheit = int(input('Enter the fahrenheit degree to be converted :'))
celsius = (fahrenheit - 32) / 1.8
print('Degree in celsius is :',celsius)

# convert Inches to Centimeter 
Inches=int(input ("Enter the length in Inches:"))
centimeter = round((2.54 * Inches), 2)
print ("The length in centimeter",centimeter)






