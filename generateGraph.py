import matplotlib.pyplot as plt

resultsFile = open("results.csv", "r")
lines = resultsFile.readlines()
resultsFile.close()

valuesInput = []
valuesCode1 = []
valuesCode2 = []

for line in lines:
    line = line.split()
    valuesInput.append(float(line[0]))
    valuesCode1.append(float(line[1]))
    valuesCode2.append(float(line[2]))

plt.plot(valuesInput, valuesCode1, label="Code 1")
plt.plot(valuesInput, valuesCode2, label="Code 2")
plt.xlabel("Input")
plt.ylabel("Time")
plt.legend()
plt.show()