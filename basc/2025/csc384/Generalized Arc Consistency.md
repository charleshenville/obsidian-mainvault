Relating to [[Constraint Satisfaction Problems]] and [[Backtracking Search]].
- This is essentially a more powerful version of Forward Checking:
![[Pasted image 20250223164847.png]]
### Support to an Assignment $V=d$
- An assignment $A$ to a all other variables (within the scope of $C$ but can be more) st. when both are used together - they satisfy $C$.

A Constraint $C$ is said to be **Generally Arc Consistent** **(GAC)**$\iff\forall V_i\in\text{scope}(C)\space\exists\space A_i\in C\space\forall d_i\in\text{CurDom}(V_i)$
A binary constraint, $C(X,Y)$ is arc consistent over X and Y if, for each value in the domain of X there is a corresponding value in the domain of Y that will satisfy the constraint; and vv.
#### We then say [[Constraint Satisfaction Problems]] are GAC $\iff$ all of its unique constraint sets are themselves GAC.