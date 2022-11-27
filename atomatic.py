import os
import json

#Load the connfiguration file 
f = open("config.json", "r")
content = f.read()
data = json.loads(content)
f.close()

#Load codes files
fileExemple = open("code1.example", "r")
content = fileExemple.read()

fileExemple = open("code2.example", "r")
content2 = fileExemple.read()

#Delete result file
resultsFile = open("results.csv", "w+")
resultsFile.write("")
resultsFile.close()

#Create code file to rum
def createCFile(value, number):
    
    if number == 1:
        fileC = open("code1.c", "w")
        fileC.write(content.replace("<VALUE>", str(value)))
    elif number == 2:
        fileC = open("code2.c", "w")
        fileC.write(content2.replace("<VALUE>", str(value)))

    fileC.close()

#Compile the code and run it and saving the output
for i in range(data["minValue"], data["maxValue"], data["minInterval"]):
    createCFile(i, 1)
    os.system("gcc code1.c -o code1")
    createCFile(i, 2)
    os.system("gcc code2.c -o code2")

    for j in range(data["turns"]):
        os.system("time ./code1 >> " + data["fileResults"])
        os.system("time ./code2 >> " + data["fileResults"])
        os.system("echo '' >> " + data["fileResults"])
        print("\n")

#Delete the code files
os.system("rm code1.c")
os.system("rm code2.c")
os.system("rm code1")
os.system("rm code2")

#Average the results
resultsFile = open("results.csv", "r")
lines = resultsFile.readlines()
resultsFile.close()

valuesInput = []
valuesCode1 = []
valuesCode2 = []

for line in lines:
    line = line.split()
    valuesInput.append(line[0])
    valuesCode1.append(line[1])
    valuesCode2.append(line[3])

toValue1 = 0.0
toValue2 = 0.0

resultsFile = open("results.csv", "w+")

for i in range(0, len(valuesInput), data["turns"]):
    for j in range(data["turns"]):
        toValue1 += float(valuesCode1[i+j])
        toValue2 += float(valuesCode2[i+j])
        toValue1 = toValue1 / data["turns"]
        toValue2 = toValue2 / data["turns"]
    resultsFile.write(str(valuesInput[i]) + " " + str(toValue1) + " " + str(toValue2) + "\n")

resultsFile.close()


#Generate the graph
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