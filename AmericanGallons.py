def gallons_to_litres(gallons):
    return gallons * 3.785

def main():
    while True:
        gallons = float(input("Enter gasoline quantity in gallons (negative to quit): "))
        if gallons < 0:
            print("Exiting program. Goodbye!")
            break
        litres = gallons_to_litres(gallons)
        print(f"{gallons} gallons = {litres:.2f} litres")

main()
