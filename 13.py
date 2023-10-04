# Temperature Converter (Celsius to Fahrenheit and vice-versa)

def fahrenheitToCelsius(cTemp):
    print((cTemp-32)*(5/9))

def celsiusToFahrenheit(fTemp):
    print((fTemp*9/5)+32)

while True:
    choiceInp = int(input('(1) Convert Celsius to Fahrenheit\n(2) Convert Fahrenheit to Celsius\n(3) Exit\nEnter here - '))
    if choiceInp == 1:
        cTemp = float(input('Enter temperature in Celsius - '))
        celsiusToFahrenheit(cTemp)
    elif choiceInp == 2:
        fTemp = float(input('Enter temperature in Fahrenheit - '))
        fahrenheitToCelsius(fTemp)
    elif choiceInp == 3:
        break
    else:
        print('Invalid Input')
        break