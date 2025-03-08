import random #for task 3

#3. If-Else Statement
n = int(input("Number: "))
if n % 2 == 0:
    print("Even!")
else:
    print("Odd!")


#4. For Loop
m = int(input("Multiplication Table: "))
for i in range(1,13):
    print(i*m)


#5. While Loop
s = str(random.randint(1,20))
found = False
while not found:
    if s == input("Pick a number: "):
        print(f"Correct. The number was: {s}")
        found = True
    else:
        print("Incorrect. Try again")
