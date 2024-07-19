def decimal_to_binary(decimal_number):
    if decimal_number == 0:
        return "0"
    
    binary_number = ""
    while decimal_number > 0:
        remainder = decimal_number % 2
        binary_number = str(remainder) + binary_number
        decimal_number = decimal_number // 2
    
    return binary_number

def main():
    try:
        decimal_number = int(input("input: "))
        if decimal_number < 0:
            print("Please enter a positive number.")
            return
        
        binary_equivalent = decimal_to_binary(decimal_number)
        print(f"output: {binary_equivalent}")
    except ValueError:
        print("Invalid input. Please enter a valid positive decimal number.")

if __name__ == "__main__":
    main()
