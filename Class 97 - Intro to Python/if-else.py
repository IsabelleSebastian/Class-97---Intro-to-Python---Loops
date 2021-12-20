
# int() --> integer; makes sure the input is a number, not a string

age = int(input("Enter Age "))

print("Your Age Is: " , age)

if (age >= 18): 
    print("Eligible to Vote.")
elif(age >=10 and age < 18):
    print("Juvenile Delinqent; Uneligible to Vote.")
else: 
    print("You Are a Child. Go Back to Mom.")



