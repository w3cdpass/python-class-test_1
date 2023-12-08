
# Setting variables
Basic_Salary = 175000
month_pay = Basic_Salary // 12
print(month_pay)

# Employee Name 
Employee_name = input("Enter name here: ")
print(f"Welcome {Employee_name}!")

# PF is 12% of Basic salary
Pro_fund = Basic_Salary * 12 / 100
print(F"{Employee_name} 12% of PF is {Pro_fund}.")


#  hra is 20% of bp but maximum can be 2000 only
hra = Basic_Salary * 20 / 100  # but maximum can be 2000 only kaise kare 
print(f"{Employee_name} your HRA is {hra}.")

Dearness_Allowance = Basic_Salary * 20 /100
print(f"{Employee_name} your Da is {Dearness_Allowance}.")




# Gross pay = bp + da + hra - pf
Gross_pay = Basic_Salary + Dearness_Allowance + hra - Pro_fund
print(f"{Employee_name} your gross pay is {Gross_pay}.")

# Net pay = gross - pf
Net_pay = Gross_pay - Pro_fund
print(f"{Employee_name} your net pay is {Net_pay}.")



# Dearness_Allowance = 9

'''
    (hra is 20% of bp but maximum can be 2000 only) ~~ isme function ya method konsa use hoga 
    (da is 20% of bp for bp < 3 lac
    otherwise                                       ~~ mujhe ye question smaj nhi aya sir ji  
    da is 30% of bp )
'''