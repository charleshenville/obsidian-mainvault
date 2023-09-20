# MaxTerms
|a|b|c|maxTerm|f1|f2|
|---|---|---|---|---|---|
|0|0|0|$a+b+c$|0|1|
|0|0|1|$a+b+\bar c$|0|1|
|0|1|0|$a+\bar b+c$|0|1|
|0|1|1|$a+\bar b+\bar c$|1|1|
|1|0|0|$\bar a+b+c$|1|0|
|1|0|1|$\bar a+b+\bar c$|0|0|
|1|1|0|$\bar a+\bar b+c$|1|1|
|1|1|1|$\bar a+\bar b+\bar c$|0|1|

## It follows that
$$f_1(a,b,c)=\prod m$$ Where m corresponds to min terms where $f_1$

## Also
$$f_2(a,b,c)=\prod \bar m$$
Where m corresponds to min terms where $\bar f_1$
