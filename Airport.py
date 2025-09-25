menu_options = ("Enter a new airport", "Fetch airport information", "Quit")

airports = {}

icao_codes = set()

while True:
    # Print the menu using the tuple
    print("\nChoose an option:")
    print(f"1 = {menu_options[0]}")
    print(f"2 = {menu_options[1]}")
    print(f"3 = {menu_options[2]}")

    choice = input("Your choice: ").strip()

    if choice == "1":
        icao = input("Enter the ICAO code of the airport: ").upper()
        if icao in icao_codes:
            print("This ICAO code already exists!")
        else:
            name = input("Enter the name of the airport: ")
            airports[icao] = name
            icao_codes.add(icao)
            print(f"Airport '{name}' with ICAO code '{icao}' added successfully.")

    elif choice == "2":
        icao = input("Enter the ICAO code of the airport: ").upper()
        if icao in airports:
            print(f"The airport name is: {airports[icao]}")
        else:
            print("No airport found with that ICAO code.")

    elif choice == "3":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please select 1, 2, or 3.")