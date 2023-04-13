import numpy.random as random

if __name__ == '__main__':
    results = {}
    for i in range(0, 10000):
        direction = random.binomial(3, 0.5)
        if results.get(direction) is None:
            results[direction] = 1
        else:
            results[direction] += 1
    print(results)