def sum_of_natural_numbers(n):
    """
    Function to calculate the sum of the first n natural numbers.
    :param n: int - The number of terms
    :return: int - The sum of the first n natural numbers
    """
    if n < 1:
        return 0  # Return 0 if n is less than 1
    return n * (n + 1) // 2  # Using the formula for sum of natural numbers

# Example usage
n = int(input("Enter a positive integer: "))
result = sum_of_natural_numbers(n)
print(f"The sum of the first {n} natural numbers is: {result}")