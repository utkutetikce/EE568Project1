import numpy as np
import matplotlib.pyplot as plt

# 1. Constants
L_max, L_min = 0.45, 0.023
L2 = (L_max - L_min) / 2
L1 = (L_max + L_min) / 2
theta_deg = np.linspace(0, 360, 1000)
theta_rad = np.radians(theta_deg)

# 2. Bipolar Current Logic (Square Wave)
# - for 0-90, + for 90-180, - for 180-270, + for 270-360
conditions = [
    (theta_deg >= 0) & (theta_deg < 90),
    (theta_deg >= 90) & (theta_deg < 180),
    (theta_deg >= 180) & (theta_deg < 270),
    (theta_deg >= 270) & (theta_deg <= 360)
]
#negative max and positive max
values = [-2.5, 2.5, -2.5, 2.5]
current_bipolar = np.select(conditions, values)

# 3. Calculate Torque: T = -i^2 * L2 * sin(2*theta)
# The torque remains a sine wave centered at zero.
torque = -(current_bipolar**2) * L2 * np.sin(2 * theta_rad)

# 4. Visualization
fig, (ax_curr, ax_ind, ax_torque) = plt.subplots(3, 1, figsize=(10, 12), sharex=True)
plt.style.use('dark_background')

# --- Current Plot ---
ax_curr.step(theta_deg, current_bipolar, color='yellow', where='post', linewidth=2)
ax_curr.set_title("Bipolar Square Wave Current ($i$)", fontsize=14)
ax_curr.set_ylabel("Current (A)")
ax_curr.axhline(0, color='white', linewidth=0.5)

# --- Inductance Plot ---
ax_ind.plot(theta_deg, L1 + L2 * np.cos(2 * theta_rad), color='magenta', linewidth=2)
ax_ind.set_ylabel("Inductance (H)")

# --- Torque Plot ---
ax_torque.plot(theta_deg, torque, color='cyan', linewidth=2)
ax_torque.fill_between(theta_deg, torque, 0, where=(torque > 0), color='cyan', alpha=0.3, label='Positive Torque')
ax_torque.fill_between(theta_deg, torque, 0, where=(torque < 0), color='red', alpha=0.3, label='Negative Torque')
ax_torque.set_title("Resulting Torque (i² makes polarity irrelevant)", fontsize=14)
ax_torque.set_ylabel("Torque (N·m)")
ax_torque.set_xlabel("Rotor Position (Degrees)")
ax_torque.axhline(0, color='white', linewidth=0.5)

plt.xticks([0, 90, 180, 270, 360])
plt.xlim(0, 360)
plt.tight_layout()
plt.show()