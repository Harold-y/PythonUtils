import numpy.random as random
from typing import List


def randPass(length: int = 20, include_special: bool = True, alphabetic_start: bool = False,
             special_pool: List[str] = ["_", "!", "-"]) -> str:
    password = ""
    start = 0
    if alphabetic_start:
        if random.binomial(1, 0.5) == 1:
            character1 = chr(random.randint(65, 91))
        else:
            character1 = chr(random.randint(97, 123))
        password += character1
        start = 1

    if include_special:
        if len(special_pool) == 0:
            print("Special Pool Size incorrect!")
            return ""
        for i in range(start, length):
            direction = random.binomial(3, 0.5)
            if direction == 2:
                sample = chr(random.randint(65, 91))
            if direction == 1:
                sample = chr(random.randint(97, 123))
            if direction == 3:
                sample = random.choice(special_pool)
            if direction == 0:
                sample = random.choice(special_pool)
            password += sample
        return password
    else:
        for i in range(start, length):
            direction = random.binomial(1, 0.5)
            if direction == 1:
                sample = chr(random.randint(97, 123))
            if direction == 0:
                sample = chr(random.randint(65, 91))
            password += sample
        return password


if __name__ == '__main__':
    print(randPass(alphabetic_start=True))
