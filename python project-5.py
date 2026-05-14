balance = 1000

print("1.Check Balance")
print("2.Deposit")
print("3.Withdraw")

choice = int(input("Choose option: "))

if choice == 1:
    print("Balance =", balance)

elif choice == 2:
    amount = int(input("Enter amount: "))
    balance = balance + amount
    print("New Balance =", balance)

elif choice == 3:
    amount = int(input("Enter amount: "))
    balance = balance - amount
    print("Remaining Balance =", balance)

else:
    print("Invalid Option")
