from utils.load_state_graph import load_state_graph
from src.ant_colony import AntColony
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

from data.data_3 import starting_times, lines, colors
from utils.path_utils import beautify_path, find_full_path
from utils.visualize_graph import visualize_map
from utils.printing import print_color
from utils.impute import impute_lines

if __name__ == "__main__":
    lines = impute_lines(lines)
    state_graph = load_state_graph(lines, starting_times)

    aco = AntColony(state_graph,
                    len(lines),
                    n_ants=50,
                    n_iterations=200,
                    alpha=2.0,
                    beta=0.1,
                    evaporation_rate=0.3,
                    q=15)

    start_node = (10, 29)
    end_node = (58, 27)
    start_time = 0

    try:
        visualize_map(lines, colors)
        best_path, best_length = aco.run(start=start_node, end=end_node, start_time=start_time)
        final_path = beautify_path(best_path)

        print("\nBest path found:")
        for point in final_path:
            print_color(point, color=colors[point[2]])
        print(f"Path length: {best_length} minutes")
        
        full_path = find_full_path(final_path, lines)
        visualize_map(lines, colors, full_path)
    except ValueError as e:
        print(e)