import pygame
import numpy as np

SCRN_WIDTH = 1024
SCRN_HEIGHT = 1024
# GRID_SIZE = 256
GRID_SIZE = 128 
pygame.init()
SCREEN = pygame.display.set_mode((SCRN_WIDTH, SCRN_HEIGHT))
clock = pygame.time.Clock()
running = True;

def lerp(a, b, t):
    return a * (1 - t) + b * t

def smoothstep(t):
    return t * t * (3 - 2 * t);

def eval(x, y, c00, c10, c01, c11):
    tx = smoothstep(x)
    ty = smoothstep(y)
    nx0 = lerp(c00, c10, tx)
    nx1 = lerp(c01, c11, tx) 

    return lerp(nx0, nx1, ty)

def process_control():
    global running;
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # KEYPRESS
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False

if __name__ == "__main__":
    print("Initializing Canvas...");

    # GRID
    grid_w = SCRN_WIDTH // GRID_SIZE + 1
    grid_h = SCRN_HEIGHT // GRID_SIZE + 1
    grid = np.random.randint(0, 256, (grid_h, grid_w))

    pixels = np.zeros((SCRN_HEIGHT, SCRN_WIDTH, 3), dtype=np.uint8)

    # render
    for y in range(SCRN_HEIGHT):
        gy = y // GRID_SIZE
        ty = (y % GRID_SIZE) / GRID_SIZE

        for x in range(SCRN_WIDTH):
            gx = x // GRID_SIZE
            tx = (x % GRID_SIZE) / GRID_SIZE

            c00 = grid[gy, gx]
            c10 = grid[gy, gx+1]
            c01 = grid[gy+1, gx]
            c11 = grid[gy+1, gx+1]

            val = eval(tx, ty, c00, c10, c01, c11)
            pixels[y, x] = [val, val, val]
            # pixels[y, x] = [(val*23)%256, val, val]

    while running:
        process_control()

        pixels.swapaxes(0, 1)
        surface = pygame.surfarray.make_surface(pixels)
        SCREEN.blit(surface, (0, 0))
        pygame.display.flip()
        clock.tick(60)




