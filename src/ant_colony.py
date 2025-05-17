import random
from typing import Tuple, Set

from utils.printing import clear_last_line

TIME_MAX = 1440

class AntColony:
    def __init__(self, graph, num_lines, n_ants, n_iterations, alpha, beta, evaporation_rate, q):
        self.graph = graph
        self.num_lines = num_lines

        self.n_ants = n_ants
        self.n_iterations = n_iterations
        self.alpha = alpha
        self.beta = beta
        self.evaporation_rate = evaporation_rate
        self.q = q

        self.pheromones = {edge: 1.0 for edge in graph.keys()}

        self.nodes: Set[Tuple[int, int]] = set()
        for edge in graph.keys():
            self.nodes.add(edge[0])
        self.nodes.add(edge[1])

    def run(self, start, end, start_time = 0):
        best_path = None
        best_length = float('inf')
        prev_found = float('inf')

        i = 0
        while i < self.n_iterations : # or best_path is None:
            all_paths = self.generate_paths(start, end, start_time)
            current_best_length = float('inf')
            if all_paths:

                self.update_pheromones(all_paths)

                current_best_path, current_best_length = min(all_paths, key=lambda x: x[1])
                
                if current_best_length < best_length:
                    best_path = current_best_path
                    best_length = current_best_length


            if prev_found == current_best_length and i != 0 :
                clear_last_line()
            prev_found = current_best_length

            print(f"Iteration {i + 1}: {f'Best length = {best_length}' if best_length != float('inf') else 'No path found'}")

            i += 1

        if best_path is None:
            raise ValueError(f"No path found from {start} to {end}")

        return best_path, best_length

    def generate_paths(self, start, end, start_time):
        all_paths = []
        for _ in range(self.n_ants):
            path = self.generate_path(start, end, start_time)
            if path is not None:
                length = self.calculate_path_length(path)
                all_paths.append((path, length + path[0][1] - start_time))
        return all_paths

    def generate_path(self, start, end, start_time):
        visited = set([start])
        current = (start, start_time, 3)
        
        found = False
        for t in range(TIME_MAX) :
            if t + start_time > TIME_MAX :
                t -= TIME_MAX
            for i in range(self.num_lines) :
                current = (start, t + start_time, i)
                if current in self.nodes :
                    found = True
                    break
            if found : break
        if current not in self.nodes :
            raise ValueError(f"Start node {current} not found in the graph")
        
        path = [current]

        u = start
        v = end

        while u != v:
            neighbors = self.get_neighbors(current)
            # print(f"Current: {current}, Neighbors: {neighbors}\n")
            neighbors = [n for n in neighbors if n not in visited]
            # print(f"Filtered Neighbors: {neighbors}")

            if not neighbors:
                return None

            probabilities = []
            total = 0.0

            for neighbor in neighbors:
                pheromone = self.pheromones.get((current, neighbor), 1e-10)
                # print(f"Pheromone for edge {current} -> {neighbor}: {pheromone}")
                distance = self.graph.get((current, neighbor), float('inf'))

                if distance == 0:
                    distance = 1e-10

                attraction = (pheromone ** self.alpha) * ((1.0 / distance) ** self.beta)
                probabilities.append(attraction)
                total += attraction

            if total == 0:
                return None

            probabilities = [p / total for p in probabilities]
            next_node = random.choices(neighbors, weights=probabilities, k=1)[0]
            path.append(next_node)
            visited.add(next_node)
            current = next_node
            u, _, _ = current

        return path

    def get_neighbors(self, node):
        # print(f"Getting neighbors for {node}")
        neighbors = []
        for edge in self.graph.keys():
            # print(edge[0])
            if edge[0] == node:
                neighbors.append(edge[1])
        # print(f"Neighbors of {node}: {neighbors}")
        return neighbors

    def calculate_path_length(self, path):
        return path[-1][1] - path[0][1]

    def update_pheromones(self, all_paths):
        for edge in self.pheromones.keys():
            self.pheromones[edge] *= (1.0 - self.evaporation_rate)

        for path, length in all_paths:
            pheromone_amount = self.q / length
            for i in range(len(path) - 1):
                edge = (path[i], path[i + 1])
                if edge in self.pheromones:
                    self.pheromones[edge] += pheromone_amount