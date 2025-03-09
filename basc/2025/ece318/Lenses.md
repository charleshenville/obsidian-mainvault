# The Thin-Lens Imaging Problem
![[Pasted image 20250122152416 1.png]]
## Notable Approximation:$$d<<s'_i;\quad s_i'-d\approx s_i'$$
Through splitting this problem into two parts (using insights from [[Spherical Refracting Surfaces]]) where we first consider refractions only at $R_1$, and then only at $R_2$, we arrive at the following formula:$$\frac{1}{s_0}+\frac{1}{s_i}=\frac{n_l-n_m}{n_m}\left(\frac{1}{R_1}-\frac{1}{R_2}\right)$$ And in air, when $n_m=1$, we arrive at the **Lensmaker's Forumula**:$$\frac{1}{s_0}+\frac{1}{s_i}=(n_l-1)\left(\frac{1}{R_1}-\frac{1}{R_2}\right)$$
### If Refractive Indices are Different on Either Side of the Lens: $$\frac{n_{m1}}{s_o}+\frac{n_{m2}}{s_i}=\frac{n_l-n_{m1}}{R_1}-\frac{n_l-n_{m2}}{R_2}$$
## [[Focal Length]]s of these Lenses in Air:
- Derived by setting either $s_i$ or $s_o$ to $\infty$ by definition:$$f_o=f_i=\left((n_l-1)\left(\frac{1}{R_1}-\frac{1}{R_2}\right)\right)^{-1}$$
## Gaussian Thin-Lens Formula:$$\frac{1}{s_o}+\frac{1}{s_i}=\frac{1}{f}=(n_l-1)\left(\frac{1}{R_1}-\frac{1}{R_2}\right)$$
- Note on **sign convention**: $f$ is positive for convex lenses and negative for concave lenses.

# Properties
### Parallel Rays
![[Pasted image 20250122155028 1.png]]
![[Pasted image 20250122155040 1.png]]

### Rays Through Lens Optical Centers (oc)
![[Pasted image 20250122155126 1.png]]

### Magnification In Air

#### Transverse (By similar triangles) $$M_T=\frac{y_i}{y_o}=\frac{-s_i}{s_o}$$
![[Pasted image 20250122155843 1.png]]

#### Longitudinal (By differentiating wrt $s_o$) $$M_L\equiv\frac{ds_i}{ds_o}=-M_T^2$$
![[Pasted image 20250122155915 1.png]]

# Types
### Concave
![[Pasted image 20250122160529 1.png]]
### Convex
![[Pasted image 20250122160520 1.png]]

# (Thin) Lens Combinations via Superposition:
![[Pasted image 20250122170239 1.png]]
- Apply Gaussian Formula to solve first lens
- Same for Second
- Then combine to get $s_i$ given $s_o$ and $d$ for example
$$s_i=\frac{df_2(s_o-f_1)-f_1f_2s_o}{(d-f_2)(s_o-f_1)-s_of_1}$$
## Transverse Magnification of this system combo $$M_T=M_{T1}\cdot M_{T2}$$
## And [[Focal Length]]s when the distance between is zero: $$\frac{1}{f_o}=\frac{1}{f_i}\equiv\frac{1}{f}=\frac{1}{f_1}+\frac{1}{f_2}$$
- Where the pattern continues down the line as we add more cascading lenses.

# Thick Lens via [[Matrix Optics]]: ![[Pasted image 20250211142638.png]] $$M=M_3M_2M_1$$$$=\begin{bmatrix}1-\frac{d(n_l-n_{m1})}{n_lR_1} & \frac{dn_{m1}}{n_l} \\ \frac{(n_l - n_{m2})}{n_{m2} R_2} - \frac{(n_l - n_{m1})}{n_{m2} R_1} - \frac{d (n_l - n_{m1}) (n_l - n_{m2})}{n_l n_{m2} R_1 R_2} & \frac{n_{m1}}{n_{m2}} + \frac{d n_{m1} (n_l - n_{m2})}{n_l n_{m2} R_2}\end{bmatrix}$$
![[Pasted image 20250211143104.png]]
$$\frac{n_{m1}}{s_{oeff}}+\frac{n_{m2}}{s_{ieff}}=\frac{n_{m1}}{f_{eff1}}=\frac{n_{m2}}{f_{eff2}}$$
![[Pasted image 20250211144242.png]]
