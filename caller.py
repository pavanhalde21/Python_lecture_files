import area
print("I am in caller.py")
area.calculate_area(5,10)

# see the output 
# we can see that when we import a file which has if __name__ == "__main__": 
# the variable __name__ changes to the name of the imported module