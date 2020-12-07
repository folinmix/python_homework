# Exercise 6 - daily workouts
print("---------------------------Start of program---------------------------")

# Input first and last value of daily running in kilometers
start_distance = float(input("Введите начальную дистанцию в км (допускаются дробные значения):\n"))
finish_distance = float(input("Введите необходимую дистанцию в км (допускаются дробные значения):\n"))

# Define variables
day_distance = start_distance
day_of_workout = 1
sys_message = ""
increasing_distance = 0.1

# Calculate results
while day_distance < finish_distance:
    sys_message = f"{day_of_workout}-й день: " + "{:.2f} км".format(day_distance)
    print(sys_message)
    day_of_workout += 1
    day_distance += day_distance * increasing_distance

sys_message = f"{day_of_workout}-й день: " + "{:.2f} км".format(day_distance)
print(sys_message)

# Display exercise answer
sys_message = f"\nОтвет: на {day_of_workout}-й день спортсмен достиг результата - не менее "
sys_message += "{:.2f} км".format(finish_distance)
print(sys_message)

print("---------------------------End of program---------------------------")
