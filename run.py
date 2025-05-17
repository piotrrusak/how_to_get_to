from utils.load_state_graph import load_state_graph
from src.ant_colony import AntColony

from data.data_1 import starting_times, lines
from utils.path_utils import beautify_path

if __name__ == "__main__":

    state_graph = load_state_graph(lines, starting_times)

    aco = AntColony(state_graph, len(lines), n_ants=5, n_iterations=200, alpha=1.0, beta=5.0, evaporation_rate=0.3, q=500)

    start_node = (0, 0)
    end_node = (9, 9)
    start_time = 0

    try:
        best_path, best_length = aco.run(start=start_node, end=end_node, start_time=start_time)
        best_path = beautify_path(best_path)

        print("\nBest path found:")
        for point in best_path:
            print(point)
        print(f"Path length: {best_length} minutes")

    except ValueError as e:
        print(e)