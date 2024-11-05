# We Must ask
- Does order matter in sampling? If yes then our sample space is usually bigger
- Do we have replacement after every sample? This Dictates wether our sample space is static.
# With Replacement (Order matters):
- Meaning Sample space is static after every selection
- $n$ objects, $k$ selections $\to$ $n^k$ Possible outcomes if order matters.
# Without Replacement (Order matters):
- Meaning Sample Space is Dynamic
- $n$ objects, $k$ selections $\to$ $$_nP_k=\frac{n!}{(n-k)!}=C\times k!,\space C=(\begin{matrix}n\\ k\end{matrix})$$ Possible outcomes if order matters. See [[Summations and Other Important Functions]].
# Without Replacement (Order does not matter):
- $n$ objects, $k$ selections $\to$ $$_nC_k=\frac{n!}{(n-k)!k!} = C=(\begin{matrix}n\\ k\end{matrix})$$ Possible outcomes if order doesn't matter. See [[Summations and Other Important Functions]].

### When we have a sample space with all unique items, no replacement can be thought of as no repetition.

# With Replacement (Order does not matter):
- Binning-method selection
- $n$ objects, $k$ selections $\to$ $$(\begin{matrix}k+n-1\\k\end{matrix})=(\begin{matrix}k+n-1\\n-1\end{matrix})$$ Total Outcomes.