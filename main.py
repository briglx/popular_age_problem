import numpy as np
import itertools as it

def main():

    age = np.arange(1, 99)
    combinations = it.combinations_with_replacement(age, 3)

    for combination in combinations:
        a, b, c = combination
        prod = a * b * c
        sum = a + b + c

        if prod == 72:
            print(f"| {combination} | {prod} | {sum} |")

main()

