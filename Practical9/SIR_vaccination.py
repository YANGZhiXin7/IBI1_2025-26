import numpy as np
import matplotlib.pyplot as plt

N = 10000 # total population
I0 = 1 # initial number of infected individuals
beta = 0.3 # infection rate
gamma = 0.05 # recovery rate
Times = 1000

vaccination_rates = np.arange(0, 1.1, 0.1)

plt.figure(figsize=(12, 8))

colors = plt.cm.viridis(np.linspace(0, 1, len(vaccination_rates)))

for i, vaccination_rate in enumerate(vaccination_rates):
    R0 = int(vaccination_rate * N)  # initial number of recovered (vaccinated) individuals
    S0 = N - I0 - R0  # initial number of susceptible individuals
    
    S = [S0]
    I = [I0]
    R = [R0]
    
    for t in range(1, Times + 1):
        if S[t-1] > 0:
            infection_prob = beta * (I[t-1] / N)
            infect_results = np.random.choice([0, 1], size=S[t-1], p=[1 - infection_prob, infection_prob])
            New_I = np.sum(infect_results)
        else:
            New_I = 0
        
        S_current = S[t-1] - New_I
        I_current = I[t-1] + New_I
        
        if I_current > 0:
            recover_results = np.random.choice([0, 1], size=I_current, p=[1 - gamma, gamma])
            new_recovered = np.sum(recover_results)
        else:
            new_recovered = 0
        
        I_current -= new_recovered
        R_current = R[t-1] + new_recovered
        
        S.append(S_current)
        I.append(I_current)
        R.append(R_current)
    
    plt.plot(range(Times + 1), I, label=f'Vaccination {int(vaccination_rate*100)}%', color=colors[i])

plt.xlabel('Time Steps')
plt.ylabel('Number of Infected Individuals')
plt.title('Infected Population Over Time for Different Vaccination Rates')
plt.legend()
plt.grid()
plt.show()

