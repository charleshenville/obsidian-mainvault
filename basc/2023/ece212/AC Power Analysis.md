[[AC-Steady State]] current definition:
$$\bar I_{SS}=\frac{\bar V}{\bar Z}=\frac{V_0}{R+j\omega L}(\frac{R-j\omega L}{R-j\omega L})=\frac{V_0(1-j\omega\tau)}{1+\omega^2t^2}$$
Where $\tau = \frac{L}{R}$;
$$\bar I_{SS}=\frac{V_0}{R}\frac{1}{\sqrt{1+\omega^2\tau^2}}\angle{\arctan(-\omega t)}$$
$$P_{SS}(t)=V_{SS}(t)\cdot i_{SS}(t)$$
![[IMG_5625EC98EC93-1.jpeg]]
Due to [[Inductors]]?

![[IMG_57ED53A23661-1.jpeg]]

$$P_{avg} = \frac{1}{T}\int_0^T V_{SS}(t)i_{SS}(t)dt$$
Where we integrate over one period length, $T$.
$$P_{avg} = \frac{1}{T}\int_0^T V_0\cos(\omega t+\phi_V)i_0\cos(\omega t+\phi_I)dt$$
From the above diagram and this result:
$$\frac{1}{2}V_0i_0\cos(\theta_V-\theta_i)$$
When $\Delta\theta\to 0$:
$$P_{avg}=\frac{1}{2}V_0i_0$$
