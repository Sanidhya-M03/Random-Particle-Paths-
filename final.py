import csv
import random
import matplotlib.pyplot as plt
import numpy as ny
square_size = 20
c = 8
x = ny.linspace(-square_size/2, square_size/2, 1000)
y = ny.linspace(-square_size/2, square_size/2, 1000)
xx, yy = ny.meshgrid(x, y)
circle = (xx**2 + yy**2 < c**2)
def move_particle(position):
    x,y = position 
    direction = random.choice([(0.01, 0), (-0.01, 0), (0, 0.01), (0, -0.01)])
    x += direction[0]
    y += direction[1]
    if x < -square_size/2:
        x = square_size/2 - 1
    elif x > square_size/2 - 1:
        x = -square_size/2
    if y < -square_size/2:
        y = square_size/2 - 1
    elif y > square_size/2 - 1:
        y = -square_size/2
    return (x, y)
def generate_path(num_steps):
    particle_path = []
    n_points = 4
    angles = ny.random.uniform(0, 2 * ny.pi, n_points)
    x = c * ny.cos(angles)
    y = c * ny.sin(angles)
    points = [(x[i], y[i]) for i in range(n_points)]
    position = random.choice(points)
    particle_path.append(position)
    for i in range(num_steps):
        position = move_particle(position)
        particle_path.append(position)
    return particle_path
num_steps = 30000
path1 = generate_path(num_steps)
filename = "path1.csv"
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['x', 'y'])
    for cor in path1:
        writer.writerow(list(cor))
path2 = generate_path(num_steps)
filename = "path2.csv"
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['x', 'y'])
    for cor in path2:
        writer.writerow(list(cor))
path3 = generate_path(num_steps)
filename = "path3.csv"
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['x', 'y'])
    for cor in path3:
        writer.writerow(list(cor))
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal')
ax.contour(xx, yy, circle, levels=[0], colors='k')
ax.plot([pos[0] for pos in path1], [pos[1] for pos in path1], '-r', linewidth=1)
ax.plot([pos[0] for pos in path2], [pos[1] for pos in path2], '-b', linewidth=1)
ax.plot([pos[0] for pos in path3], [pos[1] for pos in path3], '-g', linewidth=1)
plt.savefig('finalplot.jpg')
plt.show()
