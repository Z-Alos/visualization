import random
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import numpy as np

def lerp(a, b, t):
    return a * (1 - t) + b * t

def fade(t):
    return t * t * t * (t * (t * 6 - 15) + 10)

def gradient():
    return random.uniform(-1.0, 1.0)

num_points = 20
gradients = [gradient() for _ in range(num_points)]

def perlin(x):
    x0 = int(x) 
    x1 = x0 + 1
    
    t = x - x0
    
    g0 = gradients[x0 % num_points]
    g1 = gradients[x1 % num_points]
    
    # dot product
    d0 = t     
    d1 = t - 1.0
    dot0 = g0 * d0
    dot1 = g1 * d1
    
    return lerp(dot0, dot1, fade(t))

x_vals = np.linspace(0, 10, 500)
y_vals = [perlin(x) for x in x_vals]

plt.plot(x_vals, y_vals)
plt.show()

