import sys
args = sys.argv

first_numbers = len(args[1])
second_numbers = len(args[3])

if args[2] == "+":
    result = first_numbers + second_numbers
elif args[2] == "-":
    result = first_numbers - second_numbers
elif args[2] == "mb":
    result = first_numbers * second_numbers
elif args[2] == "/":
    result = first_numbers / second_numbers
else:
    sys.exit("what is this "+args[2]+" symbol ? ")

print(result)