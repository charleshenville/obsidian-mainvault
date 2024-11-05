$$G=(V,E)\space\&\space E=O(V^2)=\frac{\binom{V}{2}}{2}$$

# See a Directed unweighted vs a Undirected weighted ![[IMG_C197E8A24611-1.jpeg]]

# Path
- is simple if it doesn't go through any vertex more than once

We can have:
- Subgraphs
- Complet/clique/$k_i$ graphs
![[IMG_BE110E2E3BEC-1.jpeg]]
# Representation
![[IMG_905E812AE499-1.jpeg]]
- if we had directed and we wanted to take the opposing directions for every edge (compliment), we can take the transpose of the matrix and use that as a new Adjacency Matrix.

With [[Average Case Analytics]]

| Search     | Time   | Memory   |
| ---------- | ------ | -------- |
| Adj. List  | $O(V)$ | $O(V+E)$ |
| Adj. Matr. | $O(1)$ | $O(V^2)$ |

