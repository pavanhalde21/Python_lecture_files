
# importing req modules
import argparse

# create a parser object
parser = argparse.ArgumentParser(description = "An addition program")

# add argument
parser.add_argument("add", nargs = "*", metavar = "num",type = int,
                    help = "All the numbers seperated by spaces will be added")

# parse the arguments from standard input
args = parser.parse_args()

# check if add argument has any input data
# # if it has, then print sum of the given numbers
# if len(args.add) != 0:
#     print(sum(args.add))

# argument 1: (“add”) It is nothing but the name of the argument. We will use this name to access the add arguments by typing args.add. 
# argument 2: (nargs = ‘*’) The number of command-line arguments that should be consumed. Specifying it to ‘*’ means it can be any no. of arguments i.e, from 0 to anything. 
# argument 3: (metavar = ‘num’) A name for the argument in usage messages. 
# argument 4: (type = int) The type to which the command-line argument should be converted. It is str by default. 
# argument 5: (help) A brief description of what the argument does.