from random import randint,random
from operator import add
import os
def individual(length,min,max):
	return [randint(min,max) for x in xrange(length)]

def population(count, length, min, max):
	return [individual(length, min, max) for x in xrange(count)]
def fitness(pop):
	file = open("test.test","w")
	for i in range(1,501):
		file.write(str(i)+": ")
		for j in pop[i-1]:
			file.write(str(pop[i-1][j]))
		file.write("\n")
	file.close()
	os.system("hope -t test.test s38584.1.bench > op.out")
	with open('op.out') as file:
		lines = file.readlines()
		line = lines[26]
		a = int(line.split(': ')[-1].strip())
		return a
p = population(500,38,0,1)
print(fitness(p))