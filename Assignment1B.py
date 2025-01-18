# Assignment 1B.py

print("[ideal gas law calculator]")

#constants
R = 0.0821 # the ideal gas constant in atm X L/(mol X K)

# input
n = float(input("Enter the number of moles of the gas: "))
celsius = float(input("Enter the temperature of the gas in Celsius: "))
volume = float(input("enter the volume of the gas in Liters: "))

# convert Celsius to Kelvin
kelvin = celsius + 273.15

# calculate the pressure
pressure = (n * R * kelvin / volume)

# output
print(f"\nThe pressure of the gas is {pressure:.2f} atm")
