def is_prime(number):
    """Check if a number is a prime number."""
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def find_next_prime(current_prime):
    """Find the next prime number after the current_prime."""
    next_number = current_prime + 1
    while not is_prime(next_number):
        next_number += 1
    return next_number


def main():
    current_prime = 1  # Start before the first prime number
    while True:
        user_input = input("Do you want to find the next prime number? (y/n): ").strip().lower()
        if user_input == 'y':
            current_prime = find_next_prime(current_prime)
            print(f"The next prime number is: {current_prime}")
        elif user_input == 'n':
            print("Program ended.")
            break
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")


if __name__ == "__main__":
    main()
