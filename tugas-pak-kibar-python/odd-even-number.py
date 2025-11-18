choice = input("odd or even number? (o/e) ").strip().lower()
if choice in ("o", "e"):
    start_number = int(input("Enter starting number: "))
    end_number = int(input("Enter end number: "))
    print("Result:")
    for num in range(start_number, end_number + 1):
        if choice == "o" and num % 2 == 1:
            print(num)
        elif choice == "e" and num % 2 == 0:
            print(num)
else:
    print("Invalid choice. Please enter 'o' for odd or 'e' for even.")

