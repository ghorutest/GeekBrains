income = int(input('Введите выручку:\n'))
cost = int(input('Введите издержки:\n'))

if income > cost:
    profit = income - cost
    profitability = profit/income
    print (f"Прибыль организации: {profit} рентабельность: {profit/income}")
    
    employee_count = int(input('Введите кадровую численность:\n'))
    profit_per_employee = profit/employee_count
    print (f"Прибыль организации на сотрудника: {profit_per_employee:0.2f}")

elif income == cost:
    print ("Организация вышла в ноль")

elif income < cost:
    print (f"Убыток организации = {income - cost}")
