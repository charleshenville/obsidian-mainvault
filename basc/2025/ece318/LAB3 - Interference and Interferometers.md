# Preparation

1. 
![[Screenshot 2025-03-04 at 01.45.33.png]]
2. The micrometer reads $$8.6mm+12.5µm=8.6125mm$$
 ![[Pasted image 20250304014921.png]]
3. Green is $500-600nm$, but in this lab we will work with HeNe ($600-700nm$)
4. Increasing, micrometer yields higher and higher values
5. $∆𝑛 = \frac{𝑁𝜆}{2𝐿}$->$∆𝑛 = \frac{(550\pm10nm)}{2(50\pm2mm)}$
	- Nominal: $∆𝑛 = \frac{550nm}{2(50mm)}=5.5µm$
	- Max: $∆𝑛 = \frac{560nm}{2(48mm)}=5.83µm$
	- Min: $∆𝑛 = \frac{540nm}{2(52mm)}=5.19µm$
	- %Error $\approx \frac{(5.83-5.5)+(5.5-5.19)}{2(5.5)}\cdot100\%=5.8\%$
		- Alternatively we could use an averaging integral for a more exact answer: $$100\%\cdot\frac{1}{20}\frac{1}{4}\int_{-10}^{10}\int_{-2}^{2}\left|\frac{\frac{550+x}{2(50+y)}-5.5}{5.5}\right|dydx=2.14\%$$
6. Given a monochromatic source with a known wavelength (like the one in the lab) we can extrapolate microscopic measurements given the knowledge of the wavelength whereas with a mechanical method we have no reference.
7. White light is composed of many different wavelengths of light and thus will have abnormal construction/destruction interference patterns. This is highly contrasted by the single wavelength of light observed in something like green mercury light.

# Experiment

### Part 1.
$l_i=1mm$
$l_{f1}=1.31mm$
$l_{f2}=1.63mm$
$l_{f3}=1.96mm$
$\Delta l_avg=\frac{(1.31-1)+(1.63-1.31)+(1.96-1.63)}{3}=0.32mm$
$𝜆 = \frac{2Δ𝑙}{100}=6340nm$
But, accounting for the reduction ratio of 0.1 ->
$\lambda_f=634nm$

### Part 2.

$p_i=100kPa$
$p_1=75kPa, N_1=5$
$p_2=62kPa, N_2=8$
$p_3=50kPa, N_3=11$
$p_4=34kPa, N_4=14$

$N\approx -0.2115p+21.2345$ (By Linear Regression)

$$\frac{n_i - n_f}{P_i - P_f} = \frac{N}{P_i - P_f} \frac{\lambda}{2L}$$
$$n_i = \frac{N}{P_i - P_f} \frac{\lambda}{2L}(P_i-P_f)+n_f$$
$$n_i \approx -0.2115\cdot10^{-3} \frac{632.8\cdot10^{-9}}{2\cdot30\cdot10^{-3}}(101.325\cdot10^{3})+1=1.000226$$