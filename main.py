from maingeneration import main_generation

while True:
        print('\n| 1 - Matrix | 2 - List | 3 - Table | 4 - Exit |\n')
        choice = input('Select a representation you would like to take action with:\n> ')
        representation = 0

        if choice == '1':

            representation = 1

        elif choice == '2':

            representation = 2

        elif choice == '3':

            representation = 3

        elif choice == '4':

            break

        else:
            print("Select a valid option!\n")

        if representation != 0:
            main_generation(representation)