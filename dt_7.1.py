import numpy as np
import matplotlib.pyplot as plt

g = 9.81


def derivatives(t, y, k, m):
    v_x, v_y, x, y = y
    dv_x = -k / m * v_x
    dv_y = -g - k / m * v_y
    dx = v_x
    dy = v_y
    return np.array([dv_x, dv_y, dx, dy])


def rk4_step(f, t, y, dt, k, m):
    k1 = dt * f(t, y, k, m)
    k2 = dt * f(t + dt / 2, y + k1 / 2, k, m)
    k3 = dt * f(t + dt / 2, y + k2 / 2, k, m)
    k4 = dt * f(t + dt, y + k3, k, m)
    return y + (k1 + 2 * k2 + 2 * k3 + k4) / 6


def simulate_motion(v0, angle, h0, k, m, dt=0.01, t_max=10):
    angle_rad = np.radians(angle)
    v_x0 = v0 * np.cos(angle_rad)
    v_y0 = v0 * np.sin(angle_rad)

    t = 0
    y = np.array([v_x0, v_y0, 0, h0])

    positions = []
    velocities = []
    times = []

    while y[3] >= 0 and t <= t_max:
        positions.append((y[2], y[3]))
        velocities.append(np.sqrt(y[0] ** 2 + y[1] ** 2))
        times.append(t)
        y = rk4_step(derivatives, t, y, dt, k, m)
        t += dt

    return np.array(positions), np.array(velocities), np.array(times)


v0 = float(input("Enter initial speed (m/s) (Recommended: 50): ") or 50)
angle = float(input("Enter launch angle (degrees) (Recommended: 45): ") or 45)
h0 = float(input("Enter initial height (m) (Recommended: 0): ") or 0)
k = float(input("Enter drag coefficient (Recommended: 0.1): ") or 0.1)
m = float(input("Enter body mass (kg) (Recommended: 1): ") or 1)

positions, velocities, times = simulate_motion(v0, angle, h0, k, m)

x, y = positions[:, 0], positions[:, 1]

plt.figure(figsize=(10, 8))

plt.subplot(3, 1, 1)
plt.plot(x, y)
plt.xlabel("Horizontal distance, m")
plt.ylabel("Height, m")
plt.title("Body trajectory")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(times, velocities)
plt.xlabel("Time, s")
plt.ylabel("Speed, m/s")
plt.title("Speed over time")
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(times, x, label="x(t)")
plt.plot(times, y, label="y(t)")
plt.xlabel("Time, s")
plt.ylabel("Coordinates, m")
plt.title("Coordinates over time")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
