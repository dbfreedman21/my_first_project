# The main script to run the calculator

def parse_input(user_input: str):
    """
    Parse user input and return the numbers and operator.
    Example: "5 + 3" → (5.0, '+', 3.0)
    """
    try:
        parts = user_input.split()
        if len(parts) != 3:
            raise ValueError("Input must be in the format: <number> <operator> <number>")
        num1, operator, num2 = parts
        return float(num1), operator, float(num2)
    except ValueError as e:
        print(f"Error: {e}")
        return None, None, None


def calculate(num1: float, operator: str, num2: float) -> float:
    """
    Perform the calculation based on the operator.
    """
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return num1 / num2
    elif operator == "%":
        return num1 % num2
    elif operator == "//":
        return num1 // num2
    elif operator == "**":
        return num1 ** num2
    else:
        raise ValueError(f"Unsupported operator: {operator}")


def main():
    print("Welcome to the CLI Calculator!")
    print("Supported operators: +, -, *, /, %, //, **")
    print("Type 'exit' to quit.")

    while True:
        user_input = input("Enter operation: ").strip()
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        # Parse and calculate
        num1, operator, num2 = parse_input(user_input)
        if num1 is None:
            continue

        try:
            result = calculate(num1, operator, num2)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
