import scipy

quantitative = [90, 60, 45, 48, 58, 72, 25, 85]
vocabulary = [62, 81, 92, 76, 70, 75, 95, 72]
reading = [60, 91, 85, 81, 90, 76, 93, 80]

print(scipy.stats.friedmanchisquare(quantitative, vocabulary, reading))