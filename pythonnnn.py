import random

print("Enter a number:")
num = input(">> ")
num2 = random.randint(1, 30)
answer = int(num2) - int(num)
print(f"{num2} minus {num} is: " + str(answer))
print("Now, enter your favorite food:")
food = input(">> ")
print("Heres " + str(answer) + f" {food}(s)!")

for i in range(1, answer):
 print(f"{food} " + str(i)) 

