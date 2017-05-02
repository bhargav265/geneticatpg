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
def fitnessindi(individual):
	file = open("test.test","w")
	file.write(str(1)+": ")
	for j in individual:
		file.write(str(individual[j]))
	file.write("\n")
	file.close()
	os.system("hope -t test.test s38584.1.bench > op.out")
	with open('op.out') as file:
		lines = file.readlines()
		line = lines[26]
		a = int(line.split(': ')[-1].strip())
		return a	

def evolve(pop, retain = 1, random_select = 0.05, mutate = 0.01):
	#fit = fitness(pop)
	retain_length = int(len(pop)*retain)
	parents = pop[:retain_length]
	graded = [(fitnessindi(x),x) for x in parents]
	graded = [x[1] for x in sorted(graded, reverse = True)]
	for individual in pop[retain_length:]:
		if random_select > random():
			parents.append(individual)
	for individual in parents:
		if mutate > random():
			pos_to_mutate = randint(0,len(individual)-1)
			individual[pos_to_mutate] = randint(min(individual),max(individual))

	parents_length = len(parents)

	desired_length = len(pop)
	#print(graded)
	#print(graded[1])
	children = []
	count = 0
	while len(children) < desired_length:
		male = graded[count]
		count = count + 1
		if count == len(graded):
			count = 0
		female = graded[count]
		count = count + 1
		if count == len(graded):
			count = 0
		half =  int(len(male) / 2)
		child1 = male[:half] + female[half:]
		child2 = female[:half] + male[half:]
		children.append(child1)
		children.append(child2)
		
	
	if(fitness(children)>fitness(parents)):
		return children
	else:
		return parents

p = population(500, 38, 0,1)

fitness_history = [fitness(p)]
print(fitness(p))
maxi = fitness(p)
c = evolve(p)
for i in xrange(10):
	c = evolve(c)
	presnt = fitness(c)
	if(maxi<presnt):
		maxi = presnt
	fitness_history.append(presnt)
	print(presnt)

print(maxi)








