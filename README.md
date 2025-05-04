# how_to_get_to

## I. Idea
<div style="margin-left: 40px;">
The program aims to determine the fastest route from point A to point B on a map, taking into account available public transportation connections, vehicle departure schedules from stops, stop locations, and possible walking routes. The user provides a starting point, a destination, and the time at which they want to begin their journey. As a result, they receive the estimated arrival time along with the means of transportation used and the transfer locations.
</div>

## II. Mathematical Model

<div style="margin-left: 40px;">

### a) Map:
<div style="margin-left: 40px;">

A set of vertices \(V\) in the form: \((x, y)\) — where \(x, y\) are the coordinates of a vertex  
A set of edges \(E\) in the form: \((u, v, w)\) — where \(w\) is the weight of the edge, and \(u, v \in V\)

</div>

### b) Set of bus lines in the form:

<div style="margin-left: 40px;">

A list of vertices: \([(v_0, f_0), (v_1, f_1), (v_2, f_2), …, (v_n, f_n)]\),  
where  
<div style="margin-left: 40px;">

\(v_i \in V\) — the i-th vertex on the bus route  
\(f_i\) — a flag indicating whether the i-th vertex is a bus stop or not  

</div>
</div>
 
### c) Departure schedule:

<div style="margin-left: 40px;">

A set \(H\) in the form: \([v, [(l_0, h_0), (l_1, h_1), …, (l_n, h_n)]]\),  
where  
<div style="margin-left: 40px;">

\(l_i\) — the i-th bus at the stop  
\(h_i\) — the departure time of the i-th bus  

</div>
</div>

### d) Route function:

<div style="margin-left: 40px;">

\(f(v_0, v_n, t_0)\),  
where  
<div style="margin-left: 40px;">

\(v_0 \in V\) — starting vertex  
\(v_n \in V\) — ending vertex  
\(t_0\) — journey start time  

</div>

\(f\) returns \(\mathbb{P}\) — the set of all possible routes in the form:

<div style="margin-left: 40px;">

\(P = [(v_0, v_1, id_0), (v_1, v_2, id_1), \dots, (v_{n-1}, v_n, id_m)]\),  
where  
<div style="margin-left: 40px;">

\(v_i \in V\)  
\(id_k\) — the ID of the means of transport  
\((v_i, v_j, id_k)\) — travel from \(v_i\) to \(v_j\) using the transport with ID \(id_k\)  

</div>
</div>
</div>


### e) Objective function:

<div style="margin-left: 40px;">

For the route

<div style="margin-left: 40px;">

\(P = [(v_0, v_1, id_0), (v_1, v_2, id_1), \dots, (v_{n-1}, v_n, id_m)]\)

</div>

we define the objective function:

<div style="margin-left: 40px;">

\(T(P, t_0) = \sum_{i=0}^{m}\) (waiting time for \(id_i\) at \(v_i\) + travel time from \(v_i\) to \(v_{i+1}\))

</div>

The waiting time depends on the schedule at stop \(v_i\), and the travel time depends on the segment length.

</div>
</div>


## III. Objective

<div style="margin-left: 40px;">

We are looking for:  
<div style="margin-left: 40px;">

\(\underset{P\ \in\ f(v_0, v_n, t_0)}{\argmin}\ T(P, t_0)\) (route with the minimum travel time)

</div>  
where  
<div style="margin-left: 40px;">

\(v_0 \in V\) — starting vertex  
\(v_n \in V\) — ending vertex  
\(t_0\) — journey start time  
</div>

The function \(f\) is intended to find all possible routes from vertex \(v_0\) to vertex \(v_n\), taking into account transfers and walking segments along with the time to complete each route.  
The target value is the route with the shortest travel time.

</div>
