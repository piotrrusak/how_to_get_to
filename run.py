from utils.load_state_graph import load_state_graph
from src.ant_colony import AntColony
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

from data.data_3 import starting_times, lines, colors
from utils.path_utils import beautify_path, find_full_path
from utils.visualize_graph import visualize_map
from utils.printing import print_color

if __name__ == "__main__":

    state_graph = load_state_graph(lines, starting_times)

    aco = AntColony(state_graph, len(lines), n_ants=10, n_iterations=200, alpha=1.0, beta=5.0, evaporation_rate=0.3, q=500)

    start_node = (21, 61)
    end_node = (30, 74)
    start_time = 0

    try:
        # visualize_map(lines, colors)
        best_path, best_length = aco.run(start=start_node, end=end_node, start_time=start_time)
        final_path = beautify_path(best_path)

        print("\nBest path found:")
        for point in final_path:
            print_color(point[:-1], color=colors[point[2]])
        print(f"Path length: {best_length} minutes")
        
        full_path = find_full_path(final_path, lines)
        visualize_map(lines, colors, full_path)
    except ValueError as e:
        print(e)