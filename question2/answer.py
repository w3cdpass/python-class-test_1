
# Setting variables
Basic_Salary = 17500
Dearness_Allowance = 9

Employee_name = input("Enter name here: ")
print(f"Welcome {Employee_name}!")

# PF is 12% of Basic salary
Pro_fund = Basic_Salary * 12 / 100
print(F"{Employee_name} 12% of PF is {Pro_fund}.")


#  hra is 20% of bp but maximum can be 2000 only
hra = Basic_Salary * 20 / 100 
print(f"{Employee_name} your HRA is {hra}.")
# Gross pay = bp + da + hra - pf
Gross_pay = Basic_Salary + Dearness_Allowance + hra - Pro_fund
print(f"{Employee_name} your gross pay is {Gross_pay}.")

# Net pay = gross - pf
Net_pay = Gross_pay - Pro_fund
print(f"{Employee_name} your net pay is {Net_pay}.")