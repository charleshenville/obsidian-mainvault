Looking at [[Trees]]

Goal: to get a tree that covers all vertices of a graph such that we have a minimum sum of weights.

# MST Properties
-  May not be unique for a given graph, $G=(V,E)$
- $w(T)=\min\sum_{(u,v)\in T}w(u,v)$

# Cuts in G:
this property holds when we partition V into $V_1, V_2$ : $V_1\cup V_2=V,\quad V_1\cap V_2=Ø$

The [[Greedy Algorithms]] aspect of this is choosing the lighter edge in the case of the safe edge.

Use Prim's algo - similar to Djikstra's:
- Lookup later