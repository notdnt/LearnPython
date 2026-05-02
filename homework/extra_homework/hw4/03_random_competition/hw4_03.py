import random
random.seed()
firstTeam = [round(random.uniform(5, 10), 2) for i in range(20)]
secondTeam = [round(random.uniform(5, 10), 2) for i in range(20)]
results = []
print(firstTeam)
print(secondTeam)
for i in range(20):
    results.append(max(firstTeam[i], secondTeam[i]))
print(results)