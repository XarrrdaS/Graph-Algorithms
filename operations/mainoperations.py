from operations.graph_display.graph_display import display_graph
from operations.edge_search.graph_edge_search import search

def main_operations(graph, representation):
    while True:
            print('\n| 1 - Graph display | 2 - Graph find edge | Exit to graph loading options | Close a program completely |\n')
            choice = input('Select an option you would like to take action with:\n> ')

            if choice == '1':

                display_graph(graph, representation)
                
            elif choice == '2':

                search(graph, representation)

            elif  choice == '3':
            
                exit()

            else:
                print("Select a valid option!\n")