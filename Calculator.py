print("Simple Calculator")
print()
print("""1. Addition
2. Subtraction
3. Multiplication
4. Division""")

#Take user input
user_input = input("What is your choice (1, 2, 3, 4): ")

if user_input in ['1', '2', '3', '4']:
    num_1 = float(input("Please tell us the first number: "))
    num_2 = float(input("Please tell us the second number: "))

    if user_input == '1':
        print(f"The result would be {num_1 + num_2}")
    elif user_input == '2':
        print(f"The result would be {num_1 - num_2}")
    elif user_input == '3':
        print(f"The result would be {num_1 * num_2}")
    elif user_input == '4':
        if num_2 == 0:
            print("The result would be infinite or not possible")
        else:
            print(f"The result would be {num_1 / num_2}")
else:
    print("Invalid Operation, give us a valid operation to perform")