## Comparison of Adjacency Matrix and Adjacency List:  
  
Given a graph G(V,E):  
1. Memory:  
   - Adjacency List: Theta(V + E) (V: Number of vertices in a graph, E: Number of edges in a graph).  
   - Adjacency Matrix: Theta(V * V).  
2. Check if there is an edge from u to v (u and v are arbitrary vertices of a graph):  
   - Adjacency List: BigO(V)  
   - Adjacency Matrix: Theta(1)  
3. Find all adjacent of u:  
   - Adjacency List: Theta(degree(u))  
   - Adjacency Matrix: Theta(V)  
4. Add an edge:  
   - Adjacency List: Theta(1)  
   - Adjacency Matrix: Theta(1)  
5. Remove an edge:
   - Adjacency List: Theta(V).  
   - Adjacency List: Theta(1).  
