# Minterms
|a|b|c|minTerm|f1|f2|
|---|---|---|---|---|---|
|0|0|0|$\bar a\bar b\bar c$|0|1|
|0|0|1|$\bar a\bar bc$|0|1|
|0|1|0|$\bar ab\bar c$|0|1|
|0|1|1|$\bar abc$|1|1|
|1|0|0|$a\bar b\bar c$|1|0|
|1|0|1|$a\bar bc$|0|0|
|1|1|0|$ab\bar c$|1|1|
|1|1|1|$abc$|0|1|

## It follows that
$$f_1(a,b,c)=\sum m$$ Where m corresponds to min terms where $f_1$

## Also
$$f_2(a,b,c)=\sum \bar m$$
Where m corresponds to min terms where $\bar f_1$
