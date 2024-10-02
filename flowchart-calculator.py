def calculator():
    while True:
        print("Please enter another number")
        y = float(input("Enter a number: "))
        
        print("Select operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        operation = input("Enter operation number (1-4): ")
        
        x = float(input("Enter another number: "))
        
        if operation == '1':
            result = x + y
        elif operation == '2':
            result = x - y
        elif operation == '3':
            result = x * y
        elif operation == '4':
            if y != 0:
                result = x / y
            else:
                print("Error: Division by zero!")
                continue
        else:
            print("Invalid operation selected.")
            continue
        
        print(f"Result: {result}")
        
        choice = input("Do you want to perform another calculation? (yes/no): ")
        if choice.lower() != 'yes':
            break

if __name__ == "__main__":
    calculator()
