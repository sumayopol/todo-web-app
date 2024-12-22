FILEPATH = "todo.txt"

# Get to do function opens a file and assigns a variable and return the same variable to whoever will call the function
def get_todos(filepath=FILEPATH):
    with open(filepath, "r") as file_local: #Open the file on read mode
        todos_local = file_local.readlines()  # todo.txt read and placed in todos list
    return todos_local #returns the contents of the file


#Opens a file and write changes to the original file
def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)  # todos list is written to todo.txt



if __name__ == "__main__": #this is only implemented if function is run from the inside, but not when called
    print("Hello World")
    print(get_todos( ))