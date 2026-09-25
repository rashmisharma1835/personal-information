def print_multiplication_table(number: int, limit: int):
    """Prints the multiplication table of a given number up to a specified limit."""
    print(f"\n--- Multiplication Table for {number} (up to {limit}) ---")
    for i in range(1, limit + 1):
        result = number * i
        # Formatted output for clear visual alignment
        print(f"{number:>3}  x  {i:>3}  =  {result:>5}")
    print("-" * 40)


def main():
    try:
        num = int(input("Enter the number: "))
        limit = int(input("Enter the limit (e.g., 10, 12, 20): "))

        if limit < 1:
            print("Please enter a positive limit greater than 0.")
            return

        print_multiplication_table(num, limit)

    except ValueError:
        print("Invalid input! Please enter valid whole numbers.")


if __name__ == "__main__":
    main()