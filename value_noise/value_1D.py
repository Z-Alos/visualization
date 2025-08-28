import random
import matplotlib
matplotlib.use("TkAgg")  
import matplotlib.pyplot as plt
import numpy as np

frequency = 1.0;
amplitude = 1.0;

def lerp(x, y, t):
    return x * (1 - t) + y * t

num_points = int(10 * frequency)
y1 = np.array([random.random()*amplitude for _ in range(num_points)])
x1 = np.arange(len(y1))

x2 = []
y2 = []

for i in range(len(y1)):
    for t in np.arange(0, 1.1, 0.1):
        x2.append(i + t) 
        tRemapSmoothstep = t * t * (3 - 2 * t);
        if(i==len(y1)-1):
            y2.append(lerp(y1[i], y1[0], tRemapSmoothstep))
        else:
            y2.append(lerp(y1[i], y1[i+1], tRemapSmoothstep))

print(y1[0])
print(y2[len(y2)-1])

x2 = np.array(x2) / frequency
y2 = np.array(y2)

# plt.plot(x1, y1, 'o-')
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

# plt.plot(x2, y2, 'x--')
plt.plot(x2, y2, '-')
plt.show()


