import numpy as np
import matplotlib. pyplot as plt

N = 10000 # total population
S0 = 9999 # initial number of susceptible individuals
I0 = 1 # initial number of infected individuals
R0 = 0 # initial number of recovered individuals

beta = 0.3 # infection rate
gamma = 0.05 # recovery rate

S = [S0]
I = [I0]
R = [R0]
Times = 1000

for t in range(1, Times + 1):
    infection_prob = beta * (I[t-1] / N)
    infect_results = np.random.choice([0, 1], size=S[t-1], p=[1 - infection_prob, infection_prob])
    New_I = np.sum(infect_results)
    
    S_current = S[t-1] - New_I
    I_current = I[t-1] + New_I
    
    recover_results = np.random.choice([0, 1], size=I_current, p=[1 - gamma, gamma])
    new_recovered = np.sum(recover_results)
    
    I_current -= new_recovered
    R_current = R[t-1] + new_recovered
    
    S.append(S_current)
    I.append(I_current)
    R.append(R_current)

plt.figure(figsize=(10, 6))
plt.plot(S, label='Susceptible', color='blue')
plt.plot(I, label='Infected', color='red')
plt.plot(R, label='Recovered', color='green')
plt.xlabel('Time Steps')
plt.ylabel('Number of Individuals')
plt.title('SIR Model Simulation')
plt.legend()
plt.grid()
plt.show()