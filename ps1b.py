"""
Author: Raya Yabes
Date: 1/23/22

filename: ps1b.py

Determine months to save downpayment give user saves portion from monthly salary
Include raise in calcuation

"""

def calculate_dream_home():

    annual_salary = input("Enter your annual salary:")
    total_cost = input("Enter the cost of your dream home:")
    portion_saved = input("Enter the percent of your salary to save, as a decimal:")
    semi_annual_raise = input("Enter the semi-annual raise, as a decimal: ")

    portion_down_payment = 0.25
    current_savings = 0
    # annual return for savings
    r = 0.04
    downpayment = portion_down_payment * total_cost

    months = 0
    while current_savings < downpayment:
        monthly_salary = float(annual_salary) / 12
        savings_per_month =  monthly_salary * portion_saved
        if current_savings == 0:
            current_savings = savings_per_month
        else:
            current_savings += savings_per_month
            current_savings = current_savings * ( 1 +   r / 12 )
        months += 1

        if months % 6 == 0:
            annual_salary += annual_salary * float(semi_annual_raise)

    print("Number of months: {}, total savings: {}".format(months, current_savings))   

if __name__ == "__main__":
    calculate_dream_home()
