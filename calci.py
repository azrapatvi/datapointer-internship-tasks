while True:
    print("\n--- Simple Calculator ---\n")
    print("Select an operation:")
    print("1 - Addition (+)")
    print("2 - Subtraction (-)")
    print("3 - Multiplication (*)")
    print("4 - Division (/)")
    print("5 - Modulus (%)")
    print("6 - Exponentiation (**)")
    print("7 - Exit")

    choice = int(input("\nEnter your choice (1-7): "))
    print(f"You selected option {choice}.\n")

    if choice==7:
        break

    num1=int(input("enter a number:"))
    num2=int(input("enter another number:"))

    match choice:
        case 1:
            print("Addition:",num1+num2)
        case 2:
            print("Subtraction:",num1-num2)
        case 3:
            print("Multiplication:",num1*num2)
        case 4:
            try:
                print("division:",num1/num2)
            except ZeroDivisionError:
                print("cant divide by zero")
        case 5:
            try:
                print("division:",num1%num2)
            except ZeroDivisionError:
                print("cant divide by zero")
        case 6:
            print("Exponential:",num1**num2)
        case _:
            print("invlaid selection")
            continue