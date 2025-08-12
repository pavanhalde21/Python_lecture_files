import argparse
# CLI (command-line interface) is a means of interacting with a computer program 
# where the user issues commands to the program in the form of 
# successive lines of text.


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("number",help = "first number")      # positional argument
    parser.add_argument("number2", help = "second number")   # positional argument
    parser.add_argument("operation", help = "operation")     # operational argument

    # args = parser.parse_args()
    args, unknown = parser.parse_known_args()

    print(args.number1)
    print(args.number2)
    print(args.operation)

    n1 = int(args.number1)
    n2 = int(args.number2)
    result = None

    if args.operation == "add":
        result = n1 + n2

    elif args.operation == "subtract":
        result = n1 - n2

    elif args.operation == "multiply":
        result = n1*n2
    
    print(result)
