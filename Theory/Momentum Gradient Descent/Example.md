### How Beta Changes Things
1. Beta is a fixed value (e.g., 0.9), but its effect accumulates.
* At the start, the velocity (vt) is small because past values are small.
* But as we go through iterations, vt builds up more past gradients.
2 Beta controls how much past gradients influence updates.

* If beta is high (0.9 - 0.99) → More momentum, faster updates. 🚀
* If beta is low (0.5 - 0.8) → Less momentum, more like vanilla GD.
3. When does it speed up?

* At the beginning, vt is small (because past gradients were zero).
* But over time, vt gets bigger, and updates become stronger.
* This means the formula "remembers" previous gradients more and more → allowing it to speed up gradually.

### Let's See It in Action with Numbers!
* Let’s assume: θ^0 =10 (initial parameter)
* Learning rate 𝛼=0.1
* β=0.9 (typical value)
* Gradient values over time: [5, 4, 3, 2, 1] (just for example)

![](/images/image_2025-03-03_114831876.png)

### Key Observations:
* Even though the gradient is decreasing (5 → 4 → 3 → 2 → 1), the velocity keeps growing at first (0.5 → 0.85 → 1.06 → 1.15 → 1.14).
* This happens because momentum keeps stacking past gradients, making updates smoother and faster than vanilla GD.
* Eventually, when gradients get small, the update size decreases (slows down near minima), preventing overshooting.

### Final Answer to Your Speed Question
1. Early on, it starts slow (like vanilla GD).
2. As iterations increase, it speeds up because past gradients accumulate.
3. When gradients get smaller, momentum ensures smoother convergence instead of stopping suddenly.
4. Momentum is like Miya running after a treat:

* At first, she’s slow (still waking up).
* As she builds up speed, she zooms across the room. 🚀
* When she reaches the treat, she doesn’t just stop immediately—she slides a bit before stopping.
