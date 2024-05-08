from graph_creation.graph_generation import generate_dag
from graph_creation.graph_loading import load_graph, load_graph_heredoc

if __name__ == "__main__":
    while True:
        print('\n\n| 1 - Graph Generation | 2 - Graph loading | 3 - Exit |\n')
        choice = input('Select an option you would like to take action with:\n> ')

        if choice == '1':

            nodes = int(input("Podaj liczbę wierzchołków: "))
            saturation = float(input("Podaj wartość nasycenia (między 0 a 100): "))
            graph,rep = generate_dag(nodes, saturation)

        elif choice == '2':

            print('\n\n| 1 - By Hand | 2 - Heredoc | 3 - Exit |\n')
            choice = input('Select an option you would like to take action with:\n> ')

            if choice == '1':
                graph,rep = load_graph()
            elif choice == '2':
                graph,rep = load_graph_heredoc()
            elif choice == '3':
                break
            else:
                print("Select a valid option!\n")

        elif choice == '3':
            break
        else:
            print("Select a valid option!\n")