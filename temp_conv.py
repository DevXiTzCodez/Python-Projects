unit = input("Enter the unit in Temperature or Fahrenheit (Type C or F): ").upper()
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = (temp * 9) / 5 + 32
    print(f"The temperature in Fahrenheit is: {round(temp,2)}°F")
elif unit == "F":
    temp = (temp - 32) * 5 /9
    print(f"The temperature in Celsius is: {round(temp,2)}°C")
else:
    print(f"{unit} is an invalid unit.")    