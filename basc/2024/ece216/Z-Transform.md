# We will use it like we used [[LTI Laplace Transforms]] to analyze [[LTI DT Systems]]:$$X:\mathcal{R}_x\to\mathbb{C},\space X(z)=\sum_{n=0}^\infty x[n]z^{-n}$$
# Sampled Laplace Interpretation, Consider:$$x_{\text{ct}}(t)=\sum_{n=0}^\infty x[n]\delta(t-nT_s)$$
Which is a fictitious, right-sided, [[Continuous Time Signals]] constructed with a sampling period, $T_s$ and the[[Discrete Time Signals]] $x[n]$:
$$X_{\text{ct}}(s)=\int_o^\infty(\sum_{n=0}^\infty x[n]\delta(t-nT_s))e^{-st}dt$$$$X_{\text{ct}}(s)=\sum_{n=0}^\infty x[n]\int_o^\infty\delta(t-nT_s)e^{-st}dt$$$$X_{\text{ct}}(s)=\sum_{n=0}^\infty x[n](e^{-sT_s})^{-n}=X(z)\to z≜e^{sT_s}$$
# We can Establish the Following Conclusions:
## Z-Transform of the Impulse response $h[n]$: $$H(z)=\sum_{n=0}^\infty h[n]z^{-n}$$Region of Convergence (RoC/$\mathcal{R}_h$) of $H(z)$:$$\text{If: } \{z\in\mathbb{C}:|z|=1\}\subseteq\mathcal{R}_h$$$$\text{Then: }H(e^{j\omega})=H(z)|_{z=e^{j\omega}}$$Output of [[LTI DT Systems]]:$$Y(z)=H(z)X(z)$$We will use this Transform to Determine $H(z)$ for systems defined by LICC-[[Difference Equations]].
