a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = int(input("Choose option: "))

if choice == 1:
    print("Answer =", a + b)

elif choice == 2:
    print("Answer =", a - b)

elif choice == 3:
    print("Answer =", a * b)

elif choice == 4:
    print("Answer =", a / b)

else:
    print("Invalid Option")
