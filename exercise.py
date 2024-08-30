#Integrate a “WHILE” flow into the last solution,
# which repeats the flow until the user enters only correct information

# Ask the user to write their name

try::
    name = iput("Write your name: ")
    
    # Check if the name is empty:
    if len(name) == 0:
        raise ValueError("The name can't to be empty!")
        exit()
        
    # Check if there are any numbers in the name:
    elif any(char.isdigit() for char in name):
        raise ValueError("The name can't have any number.")
        exit()
    else:
        print("Name not valid", name)
except ValueError as e:
    print(e)
    exit()
    
# Ask the user to write the value of his salary and convert it to float

try:
        salary