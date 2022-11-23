# Get_string = accept a str only from user input...
# define the function and add user input
# Once defined and user input created, print answer from user input

class GetandPrintStrings():

    def __init__(self):
        self.string_dict = {}

    def get_string(self, name_of_person, quote_from_author):
        if name_of_person in self.string_dict.keys():
            print("Sorry, this author has already been used.")
        else:
            self.string_dict[name_of_person] = quote_from_author

    def print_string(self):
        print(self.string_dict)

    def main(self):
        choice = input("Hello, would you like to add one of your favorite quotes? (Y)es | (N)o").lower()

        if choice == 'y' or choice == 'yes':
            name_of_person = input("What is the name of the person?\n:").title()
            quote_from_author = input("'What is the quote of the person'?\n:").lower()

            self.get_string(name_of_person, quote_from_author)

        elif choice == 'n' or choice == 'no':
            exit()

        else:
            print(f"'{choice}' is not a valid answer.\nPlease select: (Y)es | (N)o\n:")

        print(f"Thank you for your input!\nHere is your response:")
        self.print_string()

Test_Trial = GetandPrintStrings()
Test_Trial.main()