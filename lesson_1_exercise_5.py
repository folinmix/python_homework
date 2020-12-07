# Exercise №5 - Firm revenue and costs
print("---------------------------Start of program---------------------------")

# Input revenue and costs by user and define variables
firm_revenue = float(input("Введите выручку фирмы:\n"))
firm_costs = float(input("Введите издержки фирмы:\n"))

firm_profit = firm_revenue - firm_costs
employees_quantity = 0
revenue_profitability = 0.0
employees_profit = 0.0
sys_message = ""

# Calculate and display financial results
if firm_profit > 0:
    sys_message = "Фирма работает с прибылью в {:.2f}".format(firm_profit)
    print(sys_message)
    revenue_profitability = firm_profit / firm_revenue
    sys_message = "Рентабельность выручки составляет {:.2f}%".format(revenue_profitability)
    print(sys_message)
    employees_quantity = int(input("Введите количество сотрудников в фирме:\n"))
    employees_profit = firm_profit / employees_quantity
    sys_message = f"При общем штате в {employees_quantity} сотрудник(a,ов), прибыль фирмы в расчёте"
    sys_message += "на одного сотрудника составляет {:.2f}".format(employees_profit)
    print(sys_message)

print("---------------------------End of program---------------------------")
