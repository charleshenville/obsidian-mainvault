# Class $P$
- $P =\{L\in\{0,1\}^*:\exists\text{ algorithm(TM) A that decides }L\text{ in poly-time}\}$ [[Powersets]]
- With [[Turing Machines]], TM
# Class $NP$
- Problems that can be verified in poly-time
- $L\in NP \text{ if }\exists \text{ poly-time algoritm A and cosntant C:}$ $L=\{\text{ certificate }y, |y|=\mathcal{O}(|x|^C):A(x,y)=1\}$

$P\subseteq NP$

``` mermaid
graph TD

subgraph PSPACE
	subraph NP
		NPC
		P
	end
	subgraph CO_NP
		PN
	end
end
```