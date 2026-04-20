import numpy as np
import matplotlib.pyplot as plt

# 1. Define the given constants
L_max = 0.045   # H
L_min = 0.023  # H

# 2. Calculate L1 and L2 based on the formula
# L1 is the average (DC offset), L2 is the amplitude
L1 = (L_max + L_min) / 2
L2 = (L_max - L_min) / 2

# 3. Create the theta range (0 to 360 degrees)
# convert to radians for the np.cos function
theta_deg = np.linspace(0, 360, 500)
theta_rad = np.radians(theta_deg)

# 4. Define the function L(theta) = L1 + L2 * cos(2 * theta)
L_theta = L1 + L2 * np.cos(2 * theta_rad)

# 5. Plotting
plt.figure(figsize=(10, 6))
plt.plot(theta_deg, L_theta, color='hotpink', linewidth=2.5, label=r'$L(\theta)$')

# Formatting the axes to match the image style
plt.axhline(L1, color='gray', linestyle='--', alpha=0.6, label='L1 (Average)')
plt.axhline(L_max, color='orange', linestyle='--', alpha=0.8)
plt.axhline(L_min, color='orange', linestyle='--', alpha=0.8)

# Adding labels for L_max and L_min on the y-axis
plt.yticks([L_min, L1, L_max], [f'$L_{{min}}$={L_min}H', f'$L_1$={L1:.3f}H', f'$L_{{max}}$={L_max}H'])
plt.xticks([0, 90, 180, 270, 360])

plt.title(r'$L(\theta) = L_1 + L_2 \cos(2\theta)$', fontsize=14)
plt.xlabel(r'$\theta$ (degrees)', fontsize=12)
plt.ylabel(r'$L(\theta)$ (H)', fontsize=12)
plt.grid(True, which='both', linestyle=':', alpha=0.5)
plt.xlim(0, 360)

# Display the plot
plt.tight_layout()
plt.show()