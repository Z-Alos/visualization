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
# plt.plot(x2, y2, 'x--')
plt.plot(x2, y2, '-')
plt.show()


