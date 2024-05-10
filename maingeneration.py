from graph_creation.graph_generation import generate
from graph_creation.graph_loading import load_graph, load_graph_heredoc
from operations.mainoperations import main_operations

def main_generation(representation):
    while True:
            print('\n| 1 - Graph generation | 2 - Graph loading by hand | 3 - Graph loading using heredoc | 4 - Exit to representation options | 5 - Close a program completely |\n')
            choice = input('Select a graph importing option you would like to take action with:\n> ')
            selected = 0

            if choice == '1':

                graph = generate(representation)
                selected = 1

            elif choice == '2':

                graph = load_graph(representation)
                selected = 1

            elif choice == '3':

                graph = load_graph_heredoc(representation)
                selected = 1

            elif choice == '4':

                break
            
            elif  choice == '5':
                     
                exit()
                    
            else:
                print("Select a valid option!\n")

            if selected != 0:
                main_operations(graph,representation)