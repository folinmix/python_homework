# Exercise 2 - Input time by user in seconds and display time in next format hh:mm:ss
print("---------------------------Start of program---------------------------")

# Input time by user in seconds
time_in_seconds = int(input("Введите время в секундах:\n"))

# Calculate hours, minutes and seconds
time_in_hours = int(time_in_seconds / 3600)
time_in_seconds = (time_in_seconds % 3600)
time_in_minutes = int(time_in_seconds / 60)
time_in_seconds = (time_in_seconds % 60)

# Correction variables for 2-symbols format
if time_in_hours < 10:
    time_in_hours = "0" + str(time_in_hours)

if time_in_minutes < 10:
    time_in_minutes = "0" + str(time_in_minutes)

if time_in_seconds < 10:
    time_in_seconds = "0" + str(time_in_seconds)


# Display calculated and corrected variables
sys_message = "Введённое время в формате чч:мм:сс = {hours}:{minutes}:{seconds}".format(hours=time_in_hours, minutes=time_in_minutes, seconds=time_in_seconds)
print(sys_message)

print("---------------------------End of program---------------------------")
