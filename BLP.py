class Bpl:
    def __init__(self, name):
        self.name = name
        self.authorized = {"Moe": "Her majesty's eyes only", "Larry": "Top secret", "Curly": "Secret",
                           "Shemp": "Public"}

    def create_file(self, file_name):
        f = open(file_name, "x")

    def read_file(self, file_name):
        pass

    def write_file(self, file_name, write):
        pass


def main():
    userinput = input("Enter your name: ")
    bpl = Bpl(userinput)
    accesscontrol = input("Are you trying to create, read, or write a file?: ")
    if accesscontrol == "create":
        file_name = input("What is the name of the file you are trying to create?: ")
        bpl.create_file(file_name)

    elif accesscontrol == "read":
        file_name = input("What is the name of the file you are trying to read?: ")
        bpl.read_file(file_name)

    elif accesscontrol == "write":
        file_name = input("What is the name of the file you are trying to write?: ")
        write = input("What would you like to write to the file?: ")
        bpl.write_file(file_name, write)


main()

# Notes:  Bryanna: make a dictionary with the file names and the security level that goes with the file.

# Tasks: Alberto: make a function that will create a file, make a function that will read a file, make a function that will