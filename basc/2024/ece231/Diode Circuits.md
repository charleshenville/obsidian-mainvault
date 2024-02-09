# PE1
## A [[First-Order Analysis]]
![[Pasted image 20240128142649.png]]
![[Pasted image 20240128142631.png]]

## B
![[Pasted image 20240128143103.png]]
![[Pasted image 20240128143047.png]]

## C
Use $$V_r=\frac{V_p}{fCR}$$ or, alternatively,
$$V_p=2.5V$$
$$V_D=0.5$$
$$t_{\Delta}=t_{2.5V}+1ms-t_\delta$$
$$t_{\delta}=0.25ms-0.148ms=0.102$$
$$t_\Delta=1.148-0.25=0.898$$
Thus, we have a falloff (ripple) time of 0.898ms. 
We must go from $V_o(25ms)=2.5V-V_D$ -> $V_o(0.898ms+0.25ms)=2V-V_D$
$$V_o(t)=(2.5-V_D)e^{-\frac{(t-0.25ms)}{R(100nF)}}$$
Solving for $R$, we attain (approximately):
$$R=\frac{0.898ms+0.25ms-0.25ms}{100nF(-\ln(\frac{V_o(0.898ms+0.25ms)}{2.5-V_D}))}$$
For $V_D=0V$
$$R\approx40243\Omega\approx40.243 k\Omega\to\text{std. }39.2k\Omega$$
## D
![[Pasted image 20240129005657.png]]
![[Pasted image 20240129005737.png]]

For $V_D=0.5V$
$$R\approx31215\Omega\approx31.215 k\Omega\to\text{std. }30.9k\Omega$$
## D
![[Pasted image 20240128172223.png]]
![[Pasted image 20240128172239.png]]

## E
![[Pasted image 20240128182308.png]]
![[Pasted image 20240128182337.png]]

## F
![[Pasted image 20240128182637.png]]
![[Pasted image 20240128182557.png]]

# PE2
## A
![[Pasted image 20240128191425.png]]
![[Pasted image 20240128191410.png]]
## B
![[Pasted image 20240128192549.png]]
$$V_{DC}=4.6887V$$
$$V_{r(pp)}=4.6917V-4.6857V=0.006V=6mV$$
## C
![[Pasted image 20240128193003.png]]
![[Pasted image 20240128192939.png]]
![[Pasted image 20240128193107.png]]
$$V_{DC}=3.4155V$$
$$V_{r(pp)}=3.4890V-3.3420V=0.147V=147mV$$
