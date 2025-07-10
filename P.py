1. Coin Toss & Dice Roll Simulation
•	(a) Simulate 10,000 coin tosses using random.choice(['H', 'T']).
•	(b) Roll two dice, count how often their sum is 7 out of 10,000 trials.
________________________________________
2. At Least One '6' in 10 Die Rolls
•	Simulate rolling a die 10 times, for 10,000 trials.
•	Count how often at least one 6 appears.
•	Estimate the probability from these trials.
3. Conditional Probability & Bayes’ Theorem
•	5 red, 7 green, 8 blue balls = 20 total.
•	Simulate drawing a ball 1000 times with replacement.
•	Track when previous draw is blue → what is chance current draw is red.
•	Estimate and compare with Bayes’ theorem formula.
________________________________________
4. Discrete Random Variable (Empirical Mean/Variance)
•	Sample 1000 values where:
o	P(X=1) = 0.25
o	P(X=2) = 0.35
o	P(X=3) = 0.40
•	Use numpy.random.choice and compute mean, variance, std.
5. Exponential Distribution
•	Simulate 2000 values from np.random.exponential(scale=5)
•	Plot:
o	Histogram
o	Overlay PDF using scipy.stats.expon.pdf
________________________________________
6. Central Limit Theorem
•	Generate 10,000 values from Uniform[0, 1]
•	Take 1000 samples of size 30
•	Compute mean of each sample
•	Plot histogram of:
•	
o	Uniform distribution
o	Sample means (which should look Normal)

