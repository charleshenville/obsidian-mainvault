A method of [[Uninformed Search]].
- State space for this can be very large, getting up to $10^{154}$ nodes for chess
## Game Properties
- Single-Player v.s. Multiple-Player
- Deterministic (Player Control) v.s. Stochastic (Partial Chance in $\Delta$ state)
- Perfect Information v.s. Imperfect Information
- Zero-Sum (Win what others Lose) v.s. Non-Zero-Sum (Net payoff to everyone is different depending on scenario).

## General Minimax Strategy
**Assumption:** The other player always plays its best move. Strategy is optimal $\iff$ opponent is playing optimally. If the opponent isn’t optimal, can develop a better strategy that exploits weaknesses.
**Decision:** Play a move that minimizes the payoff that could be gained by other player.
**Time Complexity:** $\mathcal{O}(b^d)$ (Exhaustive [[Depth First Search]])
$b\to$ number of legal moves at each state.
$d\to$ total number of turns for both players.
$1 + b + b^2 + … + b^{d-1} ∈ \mathcal{O}(b^d)$.

![[Pasted image 20250411002915.png]]

## The Eval Function ([[Heuristics]])
We can stop minimax+alpha beta early and guess which move we should make by taking the value of an evaluation function. Could be the number of max pieces minus the number of min pieces for orthello.