Number = int(input("Please enter a number: "))

print(f"The Table for {Number} is:")

for i in range(1, 11):
    print(f"{Number} X {i} = {Number * i}")
