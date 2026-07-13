def house_hunting (annual_salary, portion_saved,total_cost,semi_annual_raise):
    portion_down_payment = total_cost * 0.25
    current_savings = 0
    months_needed = 0
    r=(0.04 / 12)
    

    while current_savings < portion_down_payment:
        if months_needed > 0  and months_needed % 6 == 0 :
            annual_salary = annual_salary + annual_salary * semi_annual_raise
        current_savings += current_savings * r + ((annual_salary/12) * portion_saved)
        months_needed += 1
    
    return months_needed

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

result_months = house_hunting(annual_salary,portion_saved,total_cost,semi_annual_raise)
print(f"Number of months: {result_months}")
