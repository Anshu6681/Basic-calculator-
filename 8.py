# -*- coding: utf-8 -*-
"""
Created on Fri May  8 12:04:00 2026

@author: PAVILION0.2
"""

#basic calculator
first_val = input("Enter a first number: ")

if first_val.isdigit() == True:
    first_val = int(first_val)
else:
      result = int(input("Enter a number: "))
      print(f"first value is a {result} come")
    
second_val = input("Enter a  second number: ")

if second_val.isdigit() == True:
    second_val = int(second_val)
else:  
    result = int(input("Enter a number: "))
    print(f"second value is a {result} come")


action = input("Enter a symbol +- for additional,-= subtraction,*- for multiplication,/- division")      
    
if action == "+":
    res = first_val + second_val
    print(f"first additional is {res}")
    
elif action == "-":
      res = first_val - second_val
      print(f"first subtraction is {res}")

elif action == "*":
      res = first_val * second_val
      print(f"first Multiplication is {res}") 
      
elif action == "/":
      res = first_val / second_val
      print(f"first Division is {res}")
      
else:
     print("Enter a valid! Number")      
     
# preparing restaurant food billing system

pizza_price = 400
burger_price = 250
cold_drink_price = 100

food = input("Enter a food name: ")

quantity = int(input("Enter quantity: "))

if food == "pizza_price":
    total = pizza_price * quantity
    print("Total bill is {total}")

elif food == "burger_price":
    total = burger_price * quantity
    print("Total bill is {total}")

elif food == "cold_drink_price":
     total = cold_drink_price * quantity
     print("Total bill is {food}")

else:
    ("Food item is not available")
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
      