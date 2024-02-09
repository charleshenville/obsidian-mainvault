## [[Assembly Language]] to perform $\sum_{n=1}^{30}n$ in a loop.

```nasm
.global _start
_start:
      movi r8, 1
	  mov r9, r0
	  movi r11, 30
	  mov r12, r0
	  
	  addloop:
		  add r9, r9, r8
		  add r12, r12, r9
		  bne r11, r9, addloop ;branch here if whatever is at r11 and r9 are not equal.
		  
   done: br done
```

## Conditional Branches in the General sense

```nasm
bxx ra, rb, label ;ra, rb are registers, and the label is the label we branch to if the xx condition is met
```

### Some Possible conditions; branch if:

- eq: if the first two arguments are equal.
- le: if $ra\leq rb$
- ne: if $ra\neq rb$
- ge: $ra\geq rb$
- lt: $ra\lt rb$
- gt: $ra\gt rb$
- geu: $ra\geq rb\text{ (unsigned)}$ We won’t treat 2’s complimented negative numbers as such