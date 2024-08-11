def convert_temperature(temperature_list, scale):
    if scale == 'C':
        # Convert Celsius to Fahrenheit
        temperature_list[1] = (temperature_list[0] * 9/5) + 32
    elif scale == 'F':
        # Convert Fahrenheit to Celsius
        temperature_list[0] = (temperature_list[1] - 32) * 5/9
    return temperature_list

# Prompt the user to enter temperature value and scale
temp_entered = float(input("Enter the temperature value: "))
temp_scale = input("Enter the temperature scale (C or F): ").upper()

# Initialize the temperature list with None
temperature_list = [None, None]

# Populate the appropriate list position with the temperature value entered
if temp_scale == 'C':
    temperature_list[0] = temp_entered
elif temp_scale == 'F':
    temperature_list[1] = temp_entered
else:
    print("Invalid temperature scale. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    exit()

# Call the conversion function
temperature_list = convert_temperature(temperature_list, temp_scale)

# Print the results
if temp_scale == 'C':
    print(f"Temperature Entered: {temp_entered}°C")
    print(f"Temperature in Celsius: {temperature_list[0]:.2f}°C")
    print(f"Temperature in Fahrenheit: {temperature_list[1]:.2f}°F")
elif temp_scale == 'F':
    print(f"Temperature Entered: {temp_entered}°F")
    print(f"Temperature in Fahrenheit: {temperature_list[1]:.2f}°F")
    print(f"Temperature in Celsius: {temperature_list[0]:.2f}°C")