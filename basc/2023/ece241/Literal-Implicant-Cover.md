## Neighbours

- Two adjacent rows or columns in a [[K-Maps]]. They can “wrap around” the table. All 4 corners can be neighbours.

## Literal:

- Variable in either “true” or “compliment” form.
- e.g: $a\bar bcd\to$ 4 literals.

## Implicant:

- Particular or singular entry: Just a minTerm.
- Here: $ab\bar c, abc, \bar abc$

| |$ab\to00$|$ab\to01$|$ab\to11$|$ab\to10$|
|---|---|---|---|---|
|$c\to0$|$0$|$0$|$1$|$0$|
|$c\to1$|$0$|$1$|$1$|$0$|

## Prime Implicant:

- Largest possible group of 1s (By powers of 2 only).
- Here: $ab, bc$

| |$ab\to00$|$ab\to01$|$ab\to11$|$ab\to10$|
|---|---|---|---|---|
|$c\to0$|$0$|$0$|$1$|$0$|
|$c\to1$|$0$|$1$|$1$|$0$|

## Essential Prime Implicant:

- Prime Implicant that cannot be left out iot describe the logic function.
- Corresponds to Anti-overlaps in Prime Implicants. Must itself be a Prime Implicant.

## Cover

- Collections of implicants that includes every key entry in a [[K-Maps]].

## Minimal Cover

- Simplest Logic expression that covers all key entries in a [[K-Maps]]: Taking all Essential Prime Implicants first, then selecting necessary Prime Implicants to form a cover.