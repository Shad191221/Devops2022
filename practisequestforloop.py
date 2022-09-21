
# !Write a Python program to find those numbers 
# !which are divisible by 7 and multiple of 5, 
# !between 1500 and 2700 (both included).

# *solution here

p = []
for number in range (1500,2700+1):
    if number % 5 == 0 and number % 7 == 0:
        p.append(number)
print(p)