# $L$ is NP Complete or $L\in\text{ NPC}$ $\iff$
# $$L\in\text{NP}\space\&\space\forall L'\in\text{ NP}, \space L'\leq_P L$$
# NP Hard
- The latter part of the above definition$$\forall L'\in\text{ NP}, \space L'\leq_P L$$
- hard 

# Theorems for this: $$\text{ if }L\in\text{ NPC}:L\in P\to\text{NP = P}$$
- Since for any $L'\in\text{ NP}\to L'\leq_P L$. We can solve $L$, map to $L'$ all in poly-time.
# $$\text{NP = CO-NP}\iff\exists\space L\in\text{NPC}:\bar L\in\text{ NPC}$$
Showing the NP-Completeness of $L$
- Show $L\in\text{ NP}$
- For a known $L'\in\text{ NPC}$ we must show $L'\leq_PL$
[[Complexity Classes]]