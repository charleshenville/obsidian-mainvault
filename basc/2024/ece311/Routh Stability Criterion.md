Define the following Open Left Hand Plane Set $$\text{OLHP}=\{s\in\mathbb{C}:\Re(s)<0\}$$
Used to determine if polynomial roots $\in\text{OLHP}$

$$a(s)=s^n+a_{n-1}s^{n-1}+\cdots+a_1s+a_0$$
**Routh Array** For this: 
$$\begin{matrix}
s^n & 1& a_{n-2}& a_{n-4}&\cdots&0 \\
s^{n-1} & a_{n-1}& a_{n-3}& a_{n-5}&\cdots&0 \\
s^{n-2} & b_1& b_{2}& b_{3}&\cdots&0 \\
s^{n-3} & c_1& c_{2}& c_{3}&\cdots&0 \\
\vdots &\vdots &\vdots &\vdots &\ddots&\vdots \\
s^1 & y_1& y_{2}& 0&\cdots&0 \\
s^0 & z_1& 0& 0&\cdots&0 \\
\end{matrix}$$Where any non-$a$ coefficients/array values can be found similarly to this:
$$b_1=-\frac{1}{a_{n-1}}\det\begin{pmatrix}1&a_{n-2}\\a_{n-1}&a_{n-3}\end{pmatrix};\quad b_2=-\frac{1}{a_{n-1}}\det\begin{pmatrix}1&a_{n-4}\\a_{n-1}&a_{n-5}\end{pmatrix};\quad$$$$c_1=-\frac{1}{b_1}\det\begin{pmatrix}a_{n-1}&a_{n-3}\\b_1&b_2\end{pmatrix};\quad c_2=-\frac{1}{b_1}\det\begin{pmatrix}a_{n-1}&a_{n-5}\\b_1&b_3\end{pmatrix};\quad$$
### Criteria
- (Necc., Suffic.):  Roots are in OLHP $\iff$ no changes of sign of elements of first array column.
- Number of sign changes equal to number of roots in RHP.
- If any first element in any row is zero we have roots in RHP.
- If an entire row is zero, the system has poles on the Imaginary axis.

See [[Stability In Control Systems]], 