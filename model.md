# how_to_get_to

## I. Idea

The program aims to determine the fastest route from point A to point B on a map, taking into account available public transportation connections, vehicle departure schedules from stops, stop locations, and possible walking routes. The user provides a starting point, a destination, and the time at which they want to begin their journey. As a result, they receive the estimated arrival time along with the means of transportation used and the transfer locations.

## II. Mathematical Model

### a) Map:

- A set of vertices \( V \) in the form: \( (x, y) \) — where \( x, y \) are the coordinates of a vertex  
- A set of edges \( E \) in the form: \( (u, v, w) \) — where \( w \) is the weight of the edge, and \( u, v \in V \)

### b) Set of bus lines:

- A list of vertices:  
  \[
  [(v_0, f_0), (v_1, f_1), (v_2, f_2), \dots, (v_n, f_n)]
  \]  
  where:  
  - \( v_i \in V \) — the i-th vertex on the bus route  
  - \( f_i \) — a flag indicating whether the i-th vertex is a bus stop

### c) Departure schedule:

- A set \( H \) in the form:  
  \[
  [v, [(l_0, h_0), (l_1, h_1), \dots, (l_n, h_n)]]
  \]  
  where:  
  - \( l_i \) — the i-th bus at the stop  
  - \( h_i \) — the departure time of the i-th bus

### d) Route function:

- \( f(v_0, v_n, t_0) \), where:  
  - \( v_0 \in V \) — starting vertex  
  - \( v_n \in V \) — ending vertex  
  - \( t_0 \) — journey start time

- \( f \) returns \( \mathbb{P} \): the set of all possible routes of the form:  
  \[
  P = [(v_0, v_1, id_0), (v_1, v_2, id_1), \dots, (v_{n-1}, v_n, id_m)]
  \]  
  where:  
  - \( v_i \in V \)  
  - \( id_k \) — the ID of the means of transport  
  - \( (v_i, v_j, id_k) \) — travel from \( v_i \) to \( v_j \) using the transport with ID \( id_k \)

### e) Objective function:

- For a route:  
  \[
  P = [(v_0, v_1, id_0), (v_1, v_2, id_1), \dots, (v_{n-1}, v_n, id_m)]
  \]

- Define the objective function:  
  \[
  T(P, t_0) = \sum_{i=0}^{m} \text{(waiting time for } id_i \text{ at } v_i + \text{travel time from } v_i \text{ to } v_{i+1})
  \]

- The waiting time depends on the schedule at stop \( v_i \), and the travel time depends on the segment length.

## III. Objective

We are looking for:

\[
\underset{P \in f(v_0, v_n, t_0)}{\arg\min}\ T(P, t_0)
\]  
(a route with the minimum travel time), where:

- \( v_0 \in V \) — starting vertex  
- \( v_n \in V \) — ending vertex  
- \( t_0 \) — journey start time  

The function \( f \) is intended to find all possible routes from vertex \( v_0 \) to vertex \( v_n \), taking into account transfers and walking segments along with the time required to complete each route.  
The target value is the route with the shortest travel time.
