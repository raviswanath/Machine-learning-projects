# Hamming Distance
def hamming_distance(a, b):
    """
    Calculates the distance between two one hot encoded binary features
    as the avg of abs difference between each input row.
    """
    if len(a) == len(b):
        dist = sum(abs(i - j) for i, j in zip(a, b))/len(a)
        return dist
    else:
        return "Error: Length mismatch in input columns"

# Euclidean Distance
def euclidean_distance(a, b):
    """
    Euclidean distance is calculated as the square root of the sum of the
    squared differences between the two vectors.
    """
    from math import sqrt
    if len(a) == len(b):
        dist = sqrt(sum((x - y)**2 for x, y in zip(a, b)))
        return dist
    else:
        return "Error: Length mismatch in input columns"

# Manhattan Distance
def manhattan_distance(a, b):
    """
    Manhattan distance is calculated as the sum of the absolute differences
    between the two vectors
    """
    if len(a) == len(b):
        dist = sum(abs(x-y) for x, y in zip(a, b))
        return dist
    else:
        return "Error: Length mismatch in input columns"

# Minkowski Distance
def minkowski_distance(a, b, p):
    """
    It is a generalization of the Euclidean and Manhattan distance measures and
    adds a parameter, called the “order” or “p“, that allows different distance
    measures to be calculated
    """
    if len(a) == len(b):
        dist = sum(abs(x - y)**p for x, y in zip(a, b))**(1/p)
        return dist
    else:
        return "Error: Length mismatch in input columns"


if __name__ == "__main__":

    row1 = [0, 0, 0, 0, 0, 1]
    row2 = [0, 0, 0, 0, 1, 0]

    dist = hamming_distance(row1, row2)
    print(f"Hamming distance is {dist}")

    row1 = [10, 20, 15, 10, 5]
    row2 = [12, 24, 18, 8, 7]
    e_dist = euclidean_distance(row1, row2)
    m_dist = manhattan_distance(row1, row2)
    mink_dist = minkowski_distance(row1, row2, 3)
    print(f"Euclidean distance is {e_dist}")
    print(f"Manhattan distance is {m_dist}")
    print(f"Minkowski Distance is {mink_dist}")
