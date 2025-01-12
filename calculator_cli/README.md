# Project description and instructions

1.
Define the Features of Your Calculator

Before diving into coding, define the functionality:

Basic Operations:
Addition (+), subtraction (-), multiplication (*), division (/).

## Features
- Basic operations: `+`, `-`, `*`, `/`
- Advanced operations: `%` (modulus), `//` (floor division), `**` (exponentiation)
- Error handling for invalid input and division by zero
- View calculation history

Input and Output:
Accept user input in the form: 5 + 3.
Display the result: 8.

## Usage Examples
- `5 % 2` → `1`
- `10 // 3` → `3`
- `2 ** 3` → `8`

Error Handling:
Invalid input: "5 & 3" → Show an error message.
Division by zero: "10 / 0" → Show an error message.

2.
Build Incrementally

Start Simple:
Focus on a single operation (e.g., addition).
Parse user input and calculate the result.

Expand Features:
Add support for subtraction, multiplication, and division.
Use a loop to repeatedly accept user input until they choose to exit.

Refactor for Scalability:
Organize functions into a separate utils.py module if the code grows.

Features Check
1 Input Parsing (parse_input)
✅ Splits input into numbers and operator.
✅ Handles invalid inputs (e.g., wrong format).
✅ Returns None for invalid input, so the program can handle it gracefully.
2 Calculation Logic (calculate)
✅ Supports all required operators: +, -, *, /, %, //, **.
✅ Handles division by zero with a ZeroDivisionError.
✅ Raises an error for unsupported operators.
3 Main Loop (main)
✅ Greets the user and displays instructions.
✅ Includes a history feature.
✅ Allows users to quit with exit.
4 History Tracking
✅ Maintains a list of past calculations.
✅ Displays history when the user enters history.
✅ Handles cases where no calculations have been performed.