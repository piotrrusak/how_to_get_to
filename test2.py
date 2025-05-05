import random
from typing import List, Dict, Tuple, Set
from collections import defaultdict


class AntColonyTimeDependent:
    def __init__(self, graph, n_ants, n_iterations, alpha, beta, evaporation_rate, q):
        self.graph = graph

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

    def run(self, start, end):
        best_path = None
        best_length = float('inf')

        print(self.n_iterations)
        for iteration in range(self.n_iterations):
            all_paths = self.generate_paths(start, end)

            if not all_paths:
                print(f"Iteration {iteration + 1}: No path found")
                continue

            self.update_pheromones(all_paths)

            current_best_path, current_best_length = min(all_paths, key=lambda x: x[1])

            if current_best_length < best_length:
                best_path = current_best_path
                best_length = current_best_length

            print(f"Iteration {iteration + 1}: Best length = {best_length}")

        if best_path is None:
            raise ValueError(f"No path found from {start} to {end}")

        return best_path, best_length

    def generate_paths(self, start: Tuple[int, int], end: Tuple[int, int]) -> List[Tuple[List[Tuple[int, int]], float]]:
        all_paths = []
        for _ in range(self.n_ants):
            path = self.generate_path(start, end)
            if path is not None:
                length = self.calculate_path_length(path)
                all_paths.append((path, length))
        return all_paths

    def generate_path(self, start: Tuple[int, int], end: Tuple[int, int]) -> List[Tuple[int, int]]:
        path = [start]
        visited = set([start])
        current = start
        u, _ = start
        v, _ = end

        while u != v:
            neighbors = self.get_neighbors(current)
            neighbors = [n for n in neighbors if n not in visited]

            if not neighbors:
                return None

            probabilities = []
            total = 0.0

            for neighbor in neighbors:
                pheromone = self.pheromones.get((current, neighbor), 1e-10)
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
            u, _ = current

        return path

    def get_neighbors(self, node: Tuple[int, int]) -> List[Tuple[int, int]]:
        neighbors = []
        for edge in self.graph.keys():
            if edge[0] == node:
                neighbors.append(edge[1])
        return neighbors

    def calculate_path_length(self, path: List[Tuple[int, int]]) -> float:
        return path[-1][1] - path[0][1]
    def update_pheromones(self, all_paths: List[Tuple[List[Tuple[int, int]], float]]):
        for edge in self.pheromones.keys():
            self.pheromones[edge] *= (1.0 - self.evaporation_rate)

        for path, length in all_paths:
            pheromone_amount = self.q / length
            for i in range(len(path) - 1):
                edge = (path[i], path[i + 1])
                if edge in self.pheromones:
                    self.pheromones[edge] += pheromone_amount


def create_time_expanded_graph():
    from lines import starting_time, line

    n = 10
    V = set((i, j) for i in range(n) for j in range(n))

    graph = {}
    H = defaultdict(list)

    for l in range(len(line)):
        for i in range(len(line[l])):
            v, f = line[l][i]
            if f == 1:
                for st in starting_time[l]:
                    H[v].append((l, st + i))

    for key in H.keys():
        H[key].sort(key=lambda x: x[1])
        for i in range(1, len(H[key])):
            _, t1 = H[key][i - 1]
            _, t2 = H[key][i]
            graph[((key, t1), (key, t2))] = t2 - t1

    for i in range(len(line)):
        for st in starting_time[i]:
            tail = 0
            head = 1
            while head < len(line[i]):
                u, _ = line[i][tail]
                v, f = line[i][head]
                if f == 1:
                    graph[((u, st + tail), (v, st + head))] = (st+head)-(st+tail)
                    tail = head
                head += 1

    return graph


if __name__ == "__main__":

    time_expanded_graph = create_time_expanded_graph()

    aco = AntColonyTimeDependent(time_expanded_graph, n_ants=5, n_iterations=200, alpha=1.0, beta=5.0, evaporation_rate=0.3, q=500)

    start_node = ((0, 0), 0)
    end_node = ((9, 2), 28)

    try:
        best_path, best_length = aco.run(start=start_node, end=end_node)

        print("\nBest path found:")
        for point in best_path:
            print(point)
        print(f"Path length: {best_length}")

    except ValueError as e:
        print(e)