from utils.load_state_graph import load_state_graph
from src.ant_colony import AntColony

from data.data_1 import starting_times, lines

if __name__ == "__main__":

    state_graph = load_state_graph(lines, starting_times)

    aco = AntColony(state_graph, n_ants=5, n_iterations=200, alpha=1.0, beta=5.0, evaporation_rate=0.3, q=500)

    start_node = (0, 0)
    end_node = (9, 2)

    try:
        best_path, best_length = aco.run(start=start_node, end=end_node)

        print("\nBest path found:")
        for point in best_path:
            print(point)
        print(f"Path length: {best_length}")

    except ValueError as e:
        print(e)