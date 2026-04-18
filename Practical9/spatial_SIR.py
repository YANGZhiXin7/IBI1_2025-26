'''
Initialize parameters
Set beta to 0.3
Set gamma to 0.05
Set time_steps to 100

Initialize population grid (100x100)
Create a 100 x 100 grid called population, initialized to 0 (susceptible)

Randomly select one cell (x0, y0) in the grid
Set population[x0][y0] to 1 (infected)

Define neighbor offsets (8 possible directions)
Define neighbors as list of tuples: [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

Main simulation loop
For each time step t from 0 to time_steps-1:
    Create a copy of the current population
    Create new_population as a copy of population
    
Find all currently infected cells
    Find all positions (i,j) where population[i][j] == 1
    
Process each infected cell
    For each infected cell (i,j):
        For each neighbor offset (di,dj) in neighbors:
            Calculate neighbor position: ni = i + di, nj = j + dj
            If ni and nj are within grid bounds (0 to grid_size-1):
                If population[ni][nj] == 0 (susceptible):
                    Generate random number r between 0 and 1
                    If r < beta:
                        Set new_population[ni][nj] to 1 (infected)
        
Attempt recovery
        Generate random number r between 0 and 1
        If r < gamma:
            Set new_population[i][j] to 2 (recovered)
    
Update population with new state
    Set population to new_population
    
Visualization (every 10 steps or final step)
    If t is divisible by 10 OR t == time_steps-1:
        Display the current population grid as an image
Use color mapping: 0=susceptible, 1=infected, 2=recovered
'''
import numpy as np
import matplotlib.pyplot as plt

beta = 0.3
gamma = 0.05
time_steps = 100

population = np.zeros((100, 100), dtype=int)

outbreak = np.random.choice(range(100), 2)
population [outbreak[0], outbreak[1]] = 1


neighbors = [(-1, -1), (-1, 0), (-1, 1),
             (0, -1),          (0, 1),
             (1, -1),  (1, 0), (1, 1)]


for t in range(time_steps):
    new_pop = population.copy()
    
    infected = np.argwhere(population == 1)
    
    for (i, j) in infected:
        for di, dj in neighbors:
            ni = i + di
            nj = j + dj
            if 0 <= ni < 100 and 0 <= nj < 100:
                if population[ni, nj] == 0:
                    if np.random.rand() < beta:
                        new_pop[ni, nj] = 1
        
        if np.random.rand() < gamma:
            new_pop[i, j] = 2

    population = new_pop
    
    if t % 10 == 0 or t == time_steps - 1:
        plt.figure(figsize=(6, 4), dpi=150)
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title(f'Spatial SIR Model | Time step = {t}')
        plt.axis('off')
        plt.show()