from pathlib import Path
import json
import math
import random
import time
import matplotlib.pyplot as plt
from generators import unordered_sequence, ordered_sequence





def read_data(file_name, field):
    """
    Reads a JSON file and returns data for a given field.

    Args:
        file_name (str): Name of the JSON file.
        field (str): Key to retrieve from the JSON data.
            Must be one of: 'unordered_numbers', 'ordered_numbers' or 'dna_sequence'.

    Returns:
        list | str | None:
            - list: If data retrieved by the selected field contains numeric data.
            - str: If field is 'dna_sequence'.
            - None: If the field is not supported.
    """

    # get current working directory path
    with open(file_name, "r") as file:
        data = json.load(file)

    return data.get(field)

def linear_search(sekvence, cislo):

    positions = []

    for i in range(len(sekvence)):
        if sekvence[i] == cislo:
                positions.append(i)

    return {
        "positions": positions,
        "count": len(positions)
    }

def binary_search(sequence, cislo):
    left = 0
    right = len(sequence) - 1

    found = False

    while left <= right:
        middle = int((left + right) / 2)

        value = sequence[middle]

        if value == cislo:
            found = True
            break
        else:
            if value < cislo:
                left = middle + 1
            else:
                right = middle - 1

    return found


def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")

    target = 5

    result = linear_search(sequential_data, target)
    print(result)

    sorted_data = sorted(sequential_data)

    result = binary_search(sorted_data, target)
    print(result)

    print( sequential_data)
    print( target)
    print( result)
    sizes = [100, 500, 1000, 5000, 10000]

    linear_times = []
    binary_times = []

    for size in sizes:
        print("velikost:", size)

        data1 = unordered_sequence(size)
        data2 = ordered_sequence(size)

        target1 = data1[0]
        target2 = data2[0]

        start = time.perf_counter()
        for i in range(100):
            linear_search(data1, target1)
        end = time.perf_counter()

        linear_time = (end - start) / 100
        linear_times.append(linear_time)

        print("linear time:", linear_time)


        start = time.perf_counter()
        for i in range(100):
            binary_search(data2, target2)
        end = time.perf_counter()





if __name__ == "__main__":
    main()



