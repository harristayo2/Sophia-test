# Program: Total and Average Calculator
# Purpose:
# This program allows a user to enter a set of numbers.
# It calculates and displays the total and average of those numbers.
# It also handles the case where the user enters 0

def main():
    """
    Main function that controls the flow of the program.
    It gathers input, performs calculations, and displays results.
    """

    # Create an empty list to store user-entered numbers
    numbers = []

    # Variable to store the running total of all numbers
    total = 0

    # Ask the user how many numbers they want to enter
    count = int(input("How many numbers do you want to enter? "))

    # Check for edge case: no numbers entered
    if count == 0:
        print("No numbers were entered.")
        return  # Exit the program early

    # Loop to collect each number from the user
    for i in range(count):
        # Prompt the user to enter a number
        num = float(input(f"Enter number {i + 1}: "))

        # Add the number to the list
        numbers.append(num)

        # Add the number to the running total
        total += num

    # Calculate the average
    average = total / count

    # Display results to the user
    print("\n--- Results ---")
    print("Numbers entered:", numbers)
    print("Total:", total)
    print("Average:", average)


# This ensures the program runs only when executed directly
if __name__ == "__main__":
    main()
