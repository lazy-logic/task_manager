# # AVERAGE program to calculate the average of two numbers

# # take the two numbers as input
# # declare the average variable
# # declare average = (num1 + num2) / 2
# # display the average

# # num1 = float(input("enter number 1")) 
# # num2 = float(input("enter number 2"))
# # average =(num1 + num2) / 2
# # print(f"The average of {num1} and {num2} is: {average}")

# # AVERAGE program to calculate the average of two numbers
   
# # accept an age input from user and a full name 
# age = int(input("Enter your age: "))
# name = str(input("Enter your full name: "))
# print(f"{name}, Your age is: {age}")
# # if the age is less than 18 and the average is equal to 20,
# if age < 18 and int(average) == 20:
#     print(f"{name}, you are not eligible to vote.")
# # if the age is greater than or equal to 18 and the average is greater than orequal to 20,
# if age >= 18 and average >= 20:
#     # print {name}, you are eligible to vote.
#     print(f"{name}, you are eligible to vote since you are {age} years old and your average is {average}")

   
   
   
   
   
   
   
   
   
   
   
   
   
    # ask user to input their purchase a,ount as float
    # if the purchase amount is 100 cedis or more apply a disocunt of 20% and print amount to pay
    # if the purchase amamount is 50gh or more apply a discount of 10% and print the amount to pay
    #  if the purchase is less than 50gh apply no discount and print the amount to pay

amount = float(input("Enter your purchase amount in cedis: "))

if amount >= 100:
    discount = 0.2
elif amount >= 50:
    discount = 0.1
else:
    discount = 0.5
final_price = amount - (amount * discount)
print(f"The final price after a {discount * 100}% discount is: {final_price}")


######################################################

price = float(input("enter amount\n"))

if price >= 500:
    discount = 0.5
if price >= 200:
    discount = 0.2
elif discount : 0.1
final_price = price - (price * 0.5)
print (f"{final_price} we gave you a discount of {discount}")

