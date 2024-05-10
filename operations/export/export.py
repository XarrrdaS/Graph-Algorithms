import numpy as np
import os

def adjust_positions(pos, node_sizes, min_distance):
    num_nodes = len(pos)
    for i in range(num_nodes):
        for j in range(i+1, num_nodes):
            distance = np.linalg.norm(pos[i] - pos[j])
            min_dist_ij = (node_sizes[i] + node_sizes[j]) * min_distance
            if distance < min_dist_ij:
                direction = pos[j] - pos[i]
                direction /= np.linalg.norm(direction)
                adjustment = (min_dist_ij - distance) / 2
                pos[i] -= direction * adjustment
                pos[j] += direction * adjustment
    return pos

def export_tikz(graph, filename, representation):
    if not filename.endswith('.tex'):
        filename += '.tex'
    folder_path = os.path.join(os.getcwd(), "tex")
    try:
        os.makedirs(folder_path, exist_ok=True)
    except OSError as e:
        print(f"Error creating folder: {e}")

    file_path = os.path.join(folder_path, filename)
    num_nodes = len(graph)

    if num_nodes > 75:
        scale = 10
    elif num_nodes > 50:
        scale = 7
    elif num_nodes > 20:
        scale = 6
    else:
        scale = 4

    node_size = 0.5
    pos = np.random.rand(num_nodes, 2)
    pos = adjust_positions(pos, np.full(num_nodes, node_size), min_distance=node_size)

    tikzpicture="{tikzpicture}"

    if representation == 1:
        with open(file_path, 'w') as f:
            f.write(r"\documentclass{standalone}" + "\n")
            f.write(r"\usepackage{tikz}" + "\n")
            f.write(r"\usetikzlibrary{arrows.meta}" + "\n")
            f.write(r"\begin{document}" + "\n")
            f.write(r"\begin{tikzpicture}[scale=" + str(scale) + "]" + "\n")
            f.write(r"\begin{scope}[every node/.style={fill=red!60,circle,inner sep=1pt}]" + "\n")
            for node, coordinates in enumerate(pos):
                f.write(r"\node[draw, circle, minimum size=" + str(node_size) + "cm] (v" + str(node+1) + ") at (" + str(coordinates[0]) + "," + str(coordinates[1]) + ") {" + str(node+1) + "};" + "\n")
            f.write(r"\end{scope}" + "\n")
            f.write(r"\begin{scope}[>={Stealth[black]}]" + "\n")
            for i in range(num_nodes):
                for j in range(num_nodes):
                    if graph[i, j]:
                        f.write(r"\draw[->] (v" + str(i+1) + ") -- (v" + str(j+1) + ");" + "\n")
            f.write(r"\end{scope}" + "\n")
            f.write(r"\end{tikzpicture}" + "\n")
            f.write(r"\end{document}" + "\n")
            return 1

    elif representation == 2:
        with open(file_path, 'w') as f:
            f.write(r"\documentclass{standalone}" + "\n")
            f.write(r"\usepackage{tikz}" + "\n")
            f.write(r"\usetikzlibrary{arrows.meta}" + "\n")
            f.write(r"\begin{document}" + "\n")
            f.write(r"\begin{tikzpicture}[scale=" + str(scale) + "]" + "\n")
            f.write(r"\begin{scope}[every node/.style={fill=red!60,circle,inner sep=1pt}]" + "\n")
            for node, coordinates in enumerate(pos):
                f.write(r"\node[draw, circle, minimum size=" + str(node_size) + "cm] (v" + str(node+1) + ") at (" + str(coordinates[0]) + "," + str(coordinates[1]) + ") {" + str(node+1) + "};" + "\n")
            f.write(r"\end{scope}" + "\n")
            f.write(r"\begin{scope}[>={Stealth[black]}]" + "\n")
            for i in range(num_nodes):
                for j in graph[i]:
                    f.write(r"\draw[->] (v" + str(i+1) + ") -- (v" + str(j+1) + ");" + "\n")
            f.write(r"\end{scope}" + "\n")
            f.write(r"\end{tikzpicture}" + "\n")
            f.write(r"\end{document}" + "\n")
            return 1

    elif representation == 3:
        with open(file_path, 'w') as f:
            f.write(r"\documentclass{standalone}" + "\n")
            f.write(r"\usepackage{tikz}" + "\n")
            f.write(r"\usetikzlibrary{arrows.meta}" + "\n")
            f.write(r"\begin{document}" + "\n")
            f.write(r"\begin{tikzpicture}[scale=" + str(scale) + "]" + "\n")
            f.write(r"\begin{scope}[every node/.style={fill=red!60,circle,inner sep=1pt}]" + "\n")
            for node, coordinates in enumerate(pos):
                f.write(r"\node[draw, circle, minimum size=" + str(node_size) + "cm] (v" + str(node+1) + ") at (" + str(coordinates[0]) + "," + str(coordinates[1]) + ") {" + str(node+1) + "};" + "\n")
            f.write(r"\end{scope}" + "\n")
            f.write(r"\begin{scope}[>={Stealth[black]}]" + "\n")
            for i, edges in enumerate(graph):
                for edge in edges:
                    f.write(r"\draw[->] (v" + str(i+1) + ") -- (v" + str(edge[0]+1) + ");" + "\n")
            f.write(r"\end{scope}" + "\n")
            f.write(r"\end{tikzpicture}" + "\n")
            f.write(r"\end{document}" + "\n")
            return 1