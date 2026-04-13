from pathlib import Path
import json


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




if __name__ == "__main__":
    main()
