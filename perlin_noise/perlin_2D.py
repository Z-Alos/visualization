import pygame
import numpy as np
import random

# SCRN_WIDTH = 512
# SCRN_HEIGHT = 512
SCRN_WIDTH = 512*2
SCRN_HEIGHT = 512*2
# GRID_SIZE = 64   
# GRID_SIZE = 128 
GRID_SIZE = 256

pygame.init()
SCREEN = pygame.display.set_mode((SCRN_WIDTH, SCRN_HEIGHT))
clock = pygame.time.Clock()
running = True

def lerp(a, b, t):
    return a * (1 - t) + b * t

def fade(t):
    return t * t * t * (t * (t * 6 - 15) + 10)

def random_2D_vector():
    angle = random.uniform(0, 2 * np.pi)
    return np.array([np.cos(angle), np.sin(angle)])

def dot_grid_gradient(ix, iy, x, y, grid):
    dx = x - ix
    dy = y - iy

    return dx * grid[iy, ix][0] + dy * grid[iy, ix][1]

def process_control():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            running = False

if __name__ == "__main__":
    print("Generating Perlin Noise...")

    grid_w = SCRN_WIDTH // GRID_SIZE + 2
    grid_h = SCRN_HEIGHT // GRID_SIZE + 2
    grid = np.array([[random_2D_vector() for _ in range(grid_w)] for _ in range(grid_h)])

    pixels = np.zeros((SCRN_HEIGHT, SCRN_WIDTH, 3), dtype=np.uint8)

    for y in range(SCRN_HEIGHT):
        gy = y // GRID_SIZE
        ty = (y % GRID_SIZE) / GRID_SIZE

        for x in range(SCRN_WIDTH):
            gx = x // GRID_SIZE
            tx = (x % GRID_SIZE) / GRID_SIZE

            # pixel position in grid space
            xf = x / GRID_SIZE
            yf = y / GRID_SIZE

            n00 = dot_grid_gradient(gx,     gy,     xf, yf, grid)
            n10 = dot_grid_gradient(gx + 1, gy,     xf, yf, grid)
            n01 = dot_grid_gradient(gx,     gy + 1, xf, yf, grid)
            n11 = dot_grid_gradient(gx + 1, gy + 1, xf, yf, grid)

            u = fade(tx)
            v = fade(ty)

            nx0 = lerp(n00, n10, u)
            nx1 = lerp(n01, n11, u)
            val = lerp(nx0, nx1, v)

            # grayscale
            c = int((val + 1) * 127.5)  # [-1,1] → [0,255]
            pixels[y, x] = (c, c, c)

            # colorized
            # pixels[y, x] = ((c*23)%255, c, c)

            # meth head 
            # pixels[y, x] = ((c*23)%255, (c*47)%255, (c*89)%255)


    while running:
        process_control()
        surface = pygame.surfarray.make_surface(pixels.swapaxes(0, 1))
        SCREEN.blit(surface, (0, 0))
        pygame.display.flip()
        clock.tick(60)
