import scipy

quantitative = []
vocabulary = []
reading = []

print(scipy.stats.friedmanchisquare(quantitative, vocabulary, reading))
