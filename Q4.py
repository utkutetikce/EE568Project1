import numpy as np
import matplotlib.pyplot as plt

# Constants
L_max, L_min = 0.45, 0.023
L2 = (L_max - L_min) / 2
theta_deg = np.linspace(0, 360, 1000)
theta_rad = np.radians(theta_deg)

# Define Pulsed Current (ON between 90-180 and 270-360)
current_sq = np.where(((theta_deg >= 90) & (theta_deg <= 180)) |
                      ((theta_deg >= 270) & (theta_deg <= 360)), 1.0, 0.0)

# Calculate Torque with Pulsed Current
# T = -i^2 * L2 * sin(2*theta)
torque_pulsed = -(current_sq**2) * L2 * np.sin(2 * theta_rad)

# Plotting
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
plt.style.use('dark_background')

# Top: Current Control
ax1.plot(theta_deg, current_sq, color='lime', linewidth=2)
ax1.fill_between(theta_deg, current_sq, color='lime', alpha=0.2)
ax1.set_title("Current Control: Pulsed DC ($i$)", fontsize=14)
ax1.set_ylabel("Current (A)")

# Bottom: Resulting Torque
ax2.plot(theta_deg, torque_pulsed, color='orange', linewidth=2)
ax2.fill_between(theta_deg, torque_pulsed, 0, where=(torque_pulsed > 0), color='orange', alpha=0.4)
ax2.axhline(0, color='white', linestyle='--', alpha=0.3)
ax2.set_title("Resulting Positive Torque", fontsize=14)
ax2.set_ylabel("Torque (N·m)")
ax2.set_xlabel("Rotor Position (Degrees)")

plt.xticks([0, 90, 180, 270, 360])
plt.tight_layout()
plt.show()