def calculate_dream_home():

    annual_salary = input("Enter your annual salary:")
    total_cost = input("Enter the cost of your dream home:")
    portion_saved = input("Enter the percent of your salary to save, as a decimal:")

    portion_down_payment = 0.25
    current_savings = 0
    # annual return for savings
    r = 0.04
    monthly_salary = float(annual_salary) / 12
    downpayment = portion_down_payment * total_cost
    savings_per_month =  monthly_salary * portion_saved

    months = 0
    while current_savings < downpayment:
        if current_savings == 0:
            current_savings = savings_per_month
        else:
            current_savings = current_savings + savings_per_month
            current_savings = current_savings + (current_savings * r )/12
        months += 1

    print("Number of months: {}, total savings: {}".format(months, current_savings))


if __name__ == "__main__":
    # print("Hello World")
    calculate_dream_home()
