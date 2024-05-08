from operations.graph_display.graph_display import display_graph

def main_operations(graph, representation):
    while True:
            print('\n| 1 - Graph display | 2 - Exit |\n')
            choice = input('Select an option you would like to take action with:\n> ')

            if choice == '1':

                display_graph(graph, representation)
            elif choice == '2':

                break

            else:
                print("Select a valid option!\n")