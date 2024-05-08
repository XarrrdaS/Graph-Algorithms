from graph_creation.graph_generation import generate
from graph_creation.graph_loading import load_graph, load_graph_heredoc
from operations.mainoperations import main_operations

def main_generation(representation):
    while True:
            print('\n| 1 - Graph generation | 2 - Graph loading by hand | 3 - Graph loading heredoc | 4 - Exit |\n')
            choice = input('Select an option you would like to take action with:\n> ')

            if choice == '1':

                graph = generate(representation)

            elif choice == '2':

                graph = load_graph(representation)

            elif choice == '3':

                graph = load_graph_heredoc(representation)

            elif choice == '4':

                break

            else:
                print("Select a valid option!\n")

            main_operations(graph,representation)