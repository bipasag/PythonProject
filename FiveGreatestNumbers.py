numbers = []

while True:
    entry = input("Enter a number (empty to quit): ")
    if entry == "":
        break
    numbers.append(float(entry))

if numbers:
    numbers.sort(reverse=True)  # sort descending
    print("Five greatest numbers:", numbers[:5])
else:
    print("No numbers were entered.")
