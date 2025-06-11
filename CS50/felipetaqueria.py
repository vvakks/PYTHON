def main():
    dictionary = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    total = 0.0
    while True:
        try:
            x = input("Enter item: ").strip().title()  # Clean and titlecase input
        except EOFError:
            print()  # Move to new line before exiting
            break
        else:
            if x in dictionary:
                total += dictionary[x]
                print(f"Total: ${total:.2f}")
            # ignore invalid items silently as per requirement

main()
