age = int(input("Enter the age to evaluate :"))
print(f"you're {age}")
if age >= 1 and age <= 5 :
    print("You're an infant !")
elif age >= 6 and age <= 13:
    print("you're a child !")
elif age >=14 and age<= 18:
    print("you're a teen !")
elif age >=19 and age <= 35:
    print("you're young !")
elif age >= 36 and age == 60 :
    print("you're an adult !")
else :
    print("you're a senior citizen")