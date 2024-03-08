while True:
    n = input("Want some calculations? Type 'yes' to continue, 'no' to exit: ")

    if n.lower() == "yes":
        a = float(input("ValueOne: "))
        b = float(input("ValueTwo: "))
        choice = int(input("Choose operation:\n1. Addition\n2. Subtraction\n3. Division\n4. Multiplication\n"))

        if choice == 1:
            print("\nYou chose addition............\n")
            print("Answer: %f + %f = %f" % (a, b, a + b))
        elif choice == 2:
            print("\nYou chose subtraction............\n")
            if a > b:
                print("\nHere ValueOne is bigger than ValueTwo\n")
                print("Answer: %f - %f = %f" % (a, b, a - b))
            else:
                print("\nHere ValueTwo is bigger than ValueOne\n")
                print("Answer: %f - %f = %f" % (b, a, b - a))
        elif choice == 3:
            print("\nYou chose division............\n")
            if b != 0:
                print("Answer: %f / %f = %f" % (a, b, a / b))
            else:
                print("\nDenominator is zero\n")
                print("Answer: Infinity")
        elif choice == 4:
            print("\nYou chose multiplication............\n")
            print("Answer: %f x %f = %f" % (a, b, a * b))
    elif n.lower() == "no":
        print("\nSuccessfully exited")
        break
    else:
        print("Invalid input. Please enter 'yes' to continue or 'no' to exit.")