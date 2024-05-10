from operations.graph_display.graph_display import display_graph
from operations.edge_search.graph_edge_search import search
from operations.traversal.graph_BFS import bfs
from operations.traversal.graph_DFS import dfs
from operations.topological_sort.kahn import kahn
from operations.topological_sort.tarjan import tarjan
from operations.export.export import export_tikz

def main_operations(graph, representation):
    while True:
            print('\n| 1 - Graph display | 2 - Graph find edge | 3 - BFS | 4 - DFS | 5 - Kahn (BFS) | 6 - Tarjan (DFS) | 7 - Export | 8 - Exit to graph loading options | 9 - Close a program completely |\n')
            choice = input('Select an option you would like to take action with:\n> ')

            if choice == '1':

                display_graph(graph, representation)
                
            elif choice == '2':

                search(graph, representation)

            elif  choice == '3':
                 
                bfs(graph, representation)

            elif choice == '4':
                 
                dfs(graph, representation)

            elif choice == '5':
                 
                kahn(graph, representation)

            elif choice == '6':
            
                tarjan(graph, representation)

            elif choice == '7':
            
                filename = input('\nEnter the name of the file you want to export the graph to:\n> ')
                success = export_tikz(graph, filename, representation)
                if success == 1:
                    print("\nExporting the graph to a file...")
                    print("Exporting the graph to a file has been completed!\n")
                else:
                    print("\nExporting the graph to a file has been failed!\n")

            elif choice == '8':
            
                break

            elif choice == '9':
            
                exit()

            else:
                print("Select a valid option!\n")