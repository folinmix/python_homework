# Exercise №3 - Input number 'n' by user - display variable 'sum' calculated by sum = n + nn + nnn
print("---------------------------Start of program---------------------------")

# Input number 'n' by user
input_data = input("Задайте число 'n':\n")

# Calculate terms and sum of terms
term_1 = int(input_data)
term_2 = int(input_data * 2)
term_3 = int(input_data * 3)
sum_of_terms = term_1 + term_2 + term_3

# Display sum of terms
sys_message = "Сумма трёх слогаемых5 равна sum = {sum}".format(sum=sum_of_terms)
print(sys_message)

print("---------------------------End of program---------------------------")
