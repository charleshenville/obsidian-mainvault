### Order of Operations
- NOT -> AND -> OR
$$(A+B)\cdot(\overline{AB})=A\bar B +\bar AB$$

|AND|OR|
|-|-|
|$0\cdot0=0$|$1+1=1$|
|$1\cdot1=1$|$0+0=0$|
|$0\cdot1=0$|$0+1=1$|
|$x\cdot0=0$|$x+1=1$|
|$x\cdot1=x$|$x+0=x$|
|$x\cdot x=x$|$x+x=x$|
|$x\cdot \bar x=0$|$x+\bar x=1$|
|$\bar {\bar x}=x$| |

|$x+xy=x$|Absorption|$x(x+y)=x$|
|-|-|-|
|$xy+x\bar y=x$|Combining|$(x+y)(x+\bar y)=x$|
|$\overline{xy}=\bar x+\bar y$|Demorgan's|$\overline{x+y}=\bar x\cdot \bar y$|
|$x+\bar xy=x+y$|Covering|$x\cdot (\bar x+y)=x\cdot y$|
|$xy+yz+\bar xz=xy+\bar xz$|Consensus|$(x+y)(y+z)(\bar x+\bar z)=(x+y)(\bar x+z)$|

### With the above laws, we can simplify Boolean expressions from [[Sum of Products]] or [[Product of Sums]].