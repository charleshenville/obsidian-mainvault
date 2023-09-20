# Definition:
$$f_x(a,b)=\frac{\partial f}{\partial x}(a,b)=\lim\limits_{h\to0}\frac{f(a+h,  b)-f(a,b)}{h}$$
$$f_y(a,b)=\frac{\partial f}{\partial y}(a,b)=\lim\limits_{h\to0}\frac{f(a,  b+h)-f(a,b)}{h}$$
### To calculate them, treat all other variables as constants.

# Higher-Order Partials
$$\frac{\partial}{\partial x}(\frac{\partial f}{\partial x})=\frac{\partial^2 f}{\partial x^2}$$
$$\frac{\partial}{\partial y}(\frac{\partial f}{\partial x})=\frac{\partial^2 f}{\partial y\partial x}$$
$$\frac{\partial}{\partial y}(\frac{\partial f}{\partial y})=\frac{\partial^2 f}{\partial y^2}$$
$$\frac{\partial}{\partial x}(\frac{\partial f}{\partial y})=\frac{\partial^2 f}{\partial x\partial y}$$
### In General, the order in which you take the partials matters. There is an exception involving [[Clariaut's Theorem]]