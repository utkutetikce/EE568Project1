import numpy as np
import matplotlib.pyplot as plt

# 1. Define Constants
L_max = 0.45    # H
L_min = 0.0091  # H
current = 2.5   # i (Amperes)

# 2. Calculate L1 and L2
L1 = (L_max + L_min) / 2
L2 = (L_max - L_min) / 2

# 3. Create Theta range (0 to 360 degrees)
theta_deg = np.linspace(0, 360, 500)
theta_rad = np.radians(theta_deg)

# 4. Calculate functions
torque = -(current**2) * L2 * np.sin(2 * theta_rad)
inductance = L1 + L2 * np.cos(2 * theta_rad)

# 5. Plotting (2 rows, 1 column)
# sharex=True ensures both plots use the same x-axis scale
fig, (ax_t, ax_l) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
plt.style.use('dark_background')

# --- TOP PLOT: Torque ---
ax_t.plot(theta_deg, torque, color='cyan', linewidth=2, label=r'$T(\theta)$')
ax_t.set_title(r'Torque Plot: $T(\theta) = -i^2 L_2 \sin(2\theta)$', fontsize=14)
ax_t.set_ylabel('Torque (N·m)', fontsize=12)
ax_t.axhline(0, color='white', linestyle='--', alpha=0.3)
ax_t.grid(color='gray', linestyle=':', alpha=0.3)

# --- BOTTOM PLOT: Inductance ---
ax_l.plot(theta_deg, inductance, color='hotpink', linewidth=2, label=r'$L(\theta)$')
ax_l.set_title(r'Inductance Plot: $L(\theta) = L_1 + L_2 \cos(2\theta)$', fontsize=14)
ax_l.set_ylabel('Inductance (H)', fontsize=12)
ax_l.set_xlabel(r'$\theta$ (degrees)', fontsize=12)
ax_l.axhline(L1, color='white', linestyle='--', alpha=0.3)
ax_l.grid(color='gray', linestyle=':', alpha=0.3)

# Adjusting x-axis ticks for both
plt.xticks([0, 90, 180, 270, 360])
plt.xlim(0, 360)

plt.tight_layout()
plt.show()