def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

while True:
    temp = input("Enter a temperature in Fahrenheit: ")

    try:
        fahrenheit_temp = float(temp)
        celsius_temp = fahrenheit_to_celsius(fahrenheit_temp)
        print(f"{fahrenheit_temp}°F is equal to {celsius_temp:.2f}°C.")
        break
    except ValueError:
        print("That's not a valid temperature. Please enter a number.")