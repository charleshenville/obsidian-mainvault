[[Geometric Optics]], [[Lenses]], [[Focal Length]]

# Charles Henville - Lab 1 Prelab
# Preparation

1. **Three** Methods for determining [[Focal Length]] of *C*.

| 1                                                                                                                                                                                            | 2                                                                                                                                           | 3                                                                                                                                                                   |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Use an extraneous lens with a known focal point to act as a collimator (making light rays parallel). The collimated light is achieved when the object distance is equal to the focal length. | With just the object, *C*, and a screen, arrange them in such a way where we get a clear image on the screen.                               | Place a lens with known focal length close to the object such that a virtual image is formed.                                                                       |
| Use the collimated light > place the lens *C* to the right of the first lens.                                                                                                                | use the Gaussian formula to get the focal length from the measured object and image (screen) distances: $$\frac1{s_o}+\frac1{s_i}=\frac1f$$ | Create a real image by using the virtual image as a real object into *C*.                                                                                           |
| Finally we must place a screen at some distance such that the image produced on it from the system is sharp (this distance from *C*) is the focal length.                                    | Calculate Transverse Magnification and compare with measurements and orientation:$$M_T=\frac{y_i}{y_o}=-\frac{s_i}{s_o}$$                   | From object/image distances involved and known focal length of extraneous lens, calculate $f_C$ via cascading gaussian formulas:$$\frac1{s_o}+\frac1{s_i}=\frac1f$$ |

2. Can you use the first two methods for a concave lens?
- No, assuming the screen is fully opaque. we would have to change the configuration of the screen and lens such that we can observe a negative image distance (as the resultant focal length is negative and we know the object length to be positive).

3. Completing the following table

| **Object Location(s)** (to the left of lens) | **Image Location** (to the right of lens), **Orientation**, and **Relative Size** |                                   |
| -------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------- |
|                                              | Convex Lens                                                                       | Concave Lens                      |
| $\infty > s > 2f$                            | $f<s_i<2f$, inverted, smaller                                                     | $2f<s_i<f$, upright, smaller      |
| $s = 2f$                                     | $s_i=2f$, inverted, equal                                                         | $s_i=2f$, upright, equal          |
| $2f > s > f$                                 | $2f<s_i<\infty$, inverted, bigger                                                 | $-\infty<s_i<2f$, upright, bigger |
| $s = f$                                      | $s_i=\pm\infty$, upright, bigger                                                  | $s_i=-\infty$, upright, bigger    |
| $s < f$                                      | $-\infty<s_i<0$, upright, bigger                                                  | $-\infty<s_i<0$, upright, bigger  |

4. The collimator ensures that egressing light travels in parallel lines. We need it to mimic an object that is essentially infinitely far away.
5. A convex lens is placed at a distance equal to its focal length from the light source. This lens refracts the diverging light rays into parallel rays, creating a collimated beam.
6. Set up a collimator to the right of the object, and then use a mirror immediately after to see where an image will land on a variable-distance screen. that distance will be the focal point backed by the **Gaussian Mirror Formula**: $$\frac{1}{f}=\frac1u+\frac1v$$
7. Completing the Following Table

| **Object Location(s)** (to the left of lens) | **Image Location** (to the right of lens), **Orientation**, and **Relative Size** |                                                                    |
| -------------------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
|                                              | Convex Mirror                                                                     | Concave Mirror                                                     |
| $s > 2f$                                     | Image: Between $F$ and $C$, **virtual**, **upright**, **diminished**              | Image: Between $F$ and $C$, **real**, **inverted**, **diminished** |
| $C < s < F$                                  | Image: Between $F$ and $C$, **virtual**, **upright**, **diminished**              | Image: Beyond $C$, **real**, **inverted**, **magnified**           |
| $s = C$                                      | Image: At $C$, **virtual**, **upright**, **same size**                            | Image: At $C$, **real**, **inverted**, **same size**               |
| $s = F$                                      | Image: At infinity, **no image formed**                                           | Image: At infinity, **no image formed**                            |
| $F < s < C$                                  | Image: Behind mirror, **virtual**, **upright**, **magnified**                     | Image: Beyond $C$, **real**, **inverted**, **magnified**           |

8. $$MP_{mic}=-\left(\frac L{f_o}\right)\left(\frac D{f_e}\right)$$
- Where L is the distance between the two lenses and D=25cm This could be derived by using the angle subtended formula for Magnifying Power: $$MP=\frac{\alpha_{aided}}{\alpha_{unaided}}$$
9. For microscope: $f_e=10cm,f_o=5cm$. 
10. $$MP_{tele}=-\frac{f_o}{f_e}$$
- We can derive this in a similar fashion to the microscope calculation.
11. For telescope: $f_o=50cm,f_e=10cm$
12. Astronomical telescopes must have much larger magnification powers than terrestrial ones. Despite this, the image of an astronomical telescope can be inverted while a terrestrial one likely mist remain upright.
13. My advice would be to add another copy of *C* at its focal length away from the image on the screen, and move the other copy of *C* to its focal length from the object. this way we could verify weather what we know is correct. If we did not know $f_c$, we could use a collimator lens with a known focal length.

# Report

### Part I
#### For the Convex Lens
Method 1
- $f_{measured}=26cm$
Method 2
- $d_o=31cm$
- $d_i=132cm$
$f_{measured}=\frac1{\frac1{d_o}+\frac1{d_i}}$
$f_{measured}=25.1cm$
Method 3
- $f_{known}=50cm$
- $s_{o1}=10cm$
- $d=39cm$
- $s_{i2}=48cm$
$s_{i1}=\frac1{\frac1{f_{known}}-\frac1{s_o1}}=-12.5cm$
$s_{o2}=12.5+d=51.5cm$
$f_{measured}=\frac1{\frac1{51.5}+\frac1{48}}=24.84cm$

#### For the Concave Lens and Method 3
- $s_{o1}=10cm$
- $d=10cm$
- $s_{i2}=28cm$
- $f_{known}=10cm$
1. $s_{i1}=\frac{1}{\frac{1}{f}-\frac{1}{s_{o1}}}$
2. $|s_{i1}|+d=\frac1{\frac1{f_{known}}-\frac1{s_{i2}}}$
solving for $f$:
- $f_{measured}=-12.5cm$

#### For the Concave Mirror
- $u=36cm$
- $v=26cm$
- $f=\frac1{\frac1u+\frac1v}=15.1cm$

### Part II
#### (1) Compounded Microscope
- $d_i^{obj}=50cm$
- $d_o^{obj}=12cm$
- $f_e=25cm$
- $f_o=10cm$
$$MP{calculated}=-\frac{50}{12}\frac{25.4}{25}=-4.23$$
$MP_{observed}=-\frac{0.5cm}{0.1cm}=-5$ where we measured on mm-long tick on the object.

#### (2) Telescopic Lens
$M_{calculated}=\frac{50}{10}=5$

For the modified terrestrial telescope: Magnification is now -5, and the length of the telescope is 20cm longer.

#### BONUS:
- We re-measured the focal length of the $f=50cm$ lens and found it to be closer to $f=40cm$. We did the same for the $f=10cm$ lens and found it to be closer to $f=11cm$. Then, using our new $M=\frac{40}{11}=3.63636363636$ and $f_{eye}=11cm$, we get $\frac{f_e}{M}=3.025cm$. We validated this and saw the full image from that eyepiece distance and further beyond.