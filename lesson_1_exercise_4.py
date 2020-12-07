# Exercise №4 - Input positive number by user and finding the maximum value in characters
print("---------------------------Start of program---------------------------")

# Input positive number by user
input_data = input("Введите положительное число:\n")

length_of_data = len(input_data)
max_number = int(input_data[0])
length_count = 1

# Check length of input number and finding the maximum value in characters in loop
if length_of_data > 1:
    while length_count < length_of_data:
        if int(input_data[length_count]) > max_number:
            max_number = int(input_data[length_count])
        length_count += 1

# Display the maximum value in characters
sys_message = "Маскимальная цифра в введённом числе: {max}".format(max=max_number)
print(sys_message)

print("---------------------------End of program---------------------------")
