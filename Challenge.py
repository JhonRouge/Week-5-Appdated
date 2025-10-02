

print(" ===== ATM ===== ")
print("1) Balance Check")
print("2) Withraw")
print("3) Deposit")
print("4) Exit")

option = int(input("Enter your choice: "))

balance = 1000
attempts = 3
while attempts > 0:
    if option == 1:
        print(f"Your balance is{balance}")
    elif option == 2:
        deduct = int(input("How much money do you want to Withraw? "))
        print(f"you have withrawed{deduct}")
        deduct -= balance
    elif option == 3:
        add = int(input("How much money do you want to deposit? "))
        print(f"you have deposit {add} to your account")
        add += balance
    elif option == 4:
        print("Goodbye!")
        break