import math

def pizza_unit_price(diameter_cm, price_euro):
    radius_m = (diameter_cm / 2) / 100
    area_m2 = math.pi * (radius_m ** 2)
    return price_euro / area_m2

def main():

    d1 = float(input("Enter diameter of pizza 1 (cm): "))
    p1 = float(input("Enter price of pizza 1 (€): "))


    d2 = float(input("Enter diameter of pizza 2 (cm): "))
    p2 = float(input("Enter price of pizza 2 (€): "))


    unit1 = pizza_unit_price(d1, p1)
    unit2 = pizza_unit_price(d2, p2)


    print(f"\nPizza 1 unit price: {unit1:.2f} €/m²")
    print(f"Pizza 2 unit price: {unit2:.2f} €/m²")


    if unit1 < unit2:
        print("👉 Pizza 1 gives better value for money.")
    elif unit2 < unit1:
        print("👉 Pizza 2 gives better value for money.")
    else:
        print("🍕 Both pizzas give the same value for money!")

main()
