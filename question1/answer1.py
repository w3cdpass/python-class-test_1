'''1) If a year is evenly divisible by 4 means having no remainder then go to next step.
If it is not divisible by 4.
It is not a leap year. For example:  is not a leap year.'''

print("Questions part1")
print("Let's find leap year using % method.")
# create a variable called leap_year
leap_year = int(input("Enter a Year: "))

if leap_year%4 == 0:
    print(f"Yes! {leap_year} it's a leap year.")
else:
    print(f"Nop, {leap_year} itn't a leap year.")
# done

'''2)If a year is divisible by 4, but not by 100. For example: 2012, it is a leap year.
If a year is divisible by both 4 and 100, go to next step.'''

print("Questions part2")
# create a variable called find_lpyear
give_me_lpyear = int(input("Enter a leap year: "))
div_lpyear = int(input("Enter a number to divide: "))
print(f"Leap year is {give_me_lpyear}, Divided by {div_lpyear}.")
if give_me_lpyear  %  div_lpyear == 0:
    print(f"{give_me_lpyear} It is a leap year")
else:
    print(f"{give_me_lpyear} It is not a leap year")
    
'''3) If a year is divisible by 100, but not by 400. 
For example: 1900, then it is not a leap year. 
If a year is divisible by both, then it is a leap year. So 2000 is a leap year.'''