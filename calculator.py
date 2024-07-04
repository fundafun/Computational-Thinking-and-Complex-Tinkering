
def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Division by zero"
    else:
        return "Invalid operator"

def main():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operator = input("Enter the operation (+, -, *, /): ")

            result = calculate(num1, num2, operator)
            print(f"Result: {result}")

            choice = input("Do you want to make another calculation? (yes/no): ")
            if choice.lower() != 'yes':
                break
        except ValueError:
            print("Invalid input. Please enter numeric values.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()

