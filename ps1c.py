"""
Author: Raya Yabes
Date: 1/23/22

filename: ps1c.py

Determine best savings rate from monthly salary to save downpayment in 36 months

"""
def calculate_dream_home():

    annual_salary = input("Enter your annual salary:")
    total_cost = 1000000
    portion_down_payment = 0.25
    r = 0.04

    downpayment = total_cost * portion_down_payment

    semi_annual_raise = 0.07
    current_savings = 0

    def calculate_savings_rate(user_salary,temp_savings):
        total_months = 36
        counter_months = 0
        
        low_rate = 0
        high_rate = 1
        savings_rate = float((high_rate + low_rate) / 2)

        epsilon = 100
        bisection_counter = 0

        monthly_salary = float(user_salary) / 12

        while abs(downpayment - temp_savings) >= epsilon:
            savings_per_month =  monthly_salary * savings_rate
            counter_months = 0
            temp_savings = 0

            while counter_months <= total_months:
                if temp_savings == 0:
                    temp_savings = savings_per_month
                else:
                    temp_savings += savings_per_month
                    temp_savings = temp_savings * ( 1 +   r / 12 )
                counter_months += 1

                if counter_months % 6 == 0:
                    user_salary += user_salary * float(semi_annual_raise)
        
            if temp_savings >= downpayment:
                high_rate = savings_rate
            else:
                low_rate = savings_rate

            savings_rate = float((high_rate + low_rate) / 2)

            bisection_counter += 1

        print("Savings rate: {:.4f}\nBisection: {} \nSavings: {}".format(savings_rate, bisection_counter, temp_savings))

    calculate_savings_rate(int(annual_salary), current_savings)   

if __name__ == "__main__":
    calculate_dream_home()