import numpy as np
import matplotlib.pyplot as plt

A = float(input("Enter coefficient A (Recommended: 1): ") or 1)
n = int(input("Enter power of x dependency (n) (Recommended: 2): ") or 2)
m = int(input("Enter power of y dependency (m) (Recommended: 2): ") or 2)
x_min = float(input("Enter minimum x value (Recommended: -5): ") or -5)
x_max = float(input("Enter maximum x value (Recommended: 5): ") or 5)
y_min = float(input("Enter minimum y value (Recommended: -5): ") or -5)
y_max = float(input("Enter maximum y value (Recommended: 5): ") or 5)
num_points = int(input("Enter number of grid points (Recommended: 100): ") or 100)

x = np.linspace(x_min, x_max, num_points)
y = np.linspace(y_min, y_max, num_points)
X, Y = np.meshgrid(x, y)

Fx = -A * X ** n
Fy = -A * Y ** m

U = A * (X ** (n + 1) / (n + 1) + Y ** (m + 1) / (m + 1))

plt.figure(figsize=(10, 6))
cp = plt.contourf(X, Y, U, cmap='viridis')
plt.colorbar(cp, label='Potential energy U(x, y)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Two-dimensional potential energy distribution')
plt.show()
