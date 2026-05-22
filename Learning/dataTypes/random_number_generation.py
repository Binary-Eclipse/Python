import random
print(random.randint(1,10)) # generates a random integer between 1 and 10 (inclusive)
#output any digit

print(random.random()) # generates a random float between 0.0 and 1.0

print(random.choice(['apple', 'banana', 'cherry'])) # randomly selects an item from the list

print(random.sample(range(1, 50), 6)) # generates a list of 6 unique random numbers between 1 and 49 (inclusive)

print(random.shuffle(['apple', 'banana', 'cherry'])) # randomly shuffles the list

print(random.uniform(1.5, 10.5)) # generates a random float between 1.5 and 10.5 (inclusive)

print(random.randrange(1, 10, 2)) # generates a random integer between 1 and 10 (inclusive) with a step of 2

print(random.seed(42)) # sets the seed for random number generation to ensure reproducibility

print(random.randrange(1,10))
