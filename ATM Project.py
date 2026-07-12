# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 20:33:28 2026

@author: PAVILION0.2
"""

#### ATM system.
Balance = 100000
Pin = "1234"

Entered_pin = input("Enter your 4 - digit Pin: ")

if Entered_pin == Pin:
    while True:
        print("\n===== ATM MENU =====")
        print("1.Check Balance ")
        print("2.Deposit Money")
        print("3.Withdrawal Money")
        print("4.Change Pin")
        print("5.Exit")
        
        choice = int(input("Enter your choice (1-5): "))
        
        if choice == 1:
            print("Current Balance is {Balance}")
            
        elif choice == 2:
            Amount = float(input("Enter a deposit Amount: "))
            
            if Amount > 0:
                Balance += Amount
                print("Money deposited successfully")
                print(f"updated balance:{Balance}")
                
            else:
                print("Invalid Amount")
                
        elif choice == 3:
            Amount = float(input("Enter a withdrawal amount: "))
            if Amount <= Balance:
                Balance -= Amount
                
                print("Please collect your cash")
                
                print(f"Remaining balance  {Balance}")
                
            else:
                print("Insufficient Balance")
                
        elif choice == 4:
            new_pin = input("Enter a new 4- digit Pin: ")
            
            if len(new_pin) == 4 and new_pin.isdigit():
                pin = new_pin
                print("Pin changed successfully")
                
            else:
                print("Invalid Pin. Pin must be 4- digit")
                
        elif choice == 5:
            print("Thank you for using our ATM.")
            
            break
        
        else:
            print("Invalid choice.Please try again")
            
        
            
            