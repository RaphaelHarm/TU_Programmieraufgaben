# Copyright TU Wien (2022) - EVC: Task2
# Institute of Computer Graphics and Algorithms.

import numpy as np


def define_triangle() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Defines a triangle. The points are determined by your
    matriculation number - see task description.

    Returns:
        A tuple (P1, P2, P3), where
          - P1: A vector with 3 elements. Shape: (3,).
          - P2: A vector with 3 elements. Shape: (3,).
          - P3: A vector with 3 elements. Shape: (3,).
    """
    ### STUDENT CODE

    # 1 2 5 2 7 1 8 4
    # A B C D E F G H

    P1 = np.array([(1 + 5), -(1 + 1), -(1 + 7)])
    P2 = np.array([-(1 + 8), -(1 + 2), (1 + 4)])
    P3 = np.array([-(1 + 2), (1 + 1), -(1 + 2)])

    ### END STUDENT CODE

    return P1, P2, P3


def define_triangle_edges(
        P1: np.ndarray, P2: np.ndarray, P3: np.ndarray
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Calculates the edges of the triangle by defining the vectors
    P1P2, P2P3, P3P1.

    Args:
        P1: A vector with 3 elements. Shape: (3,).
        P2: A vector with 3 elements. Shape: (3,).
        P3: A vector with 3 elements. Shape: (3,).

    Returns:
        A tuple (P1P2, P2P3, P3P1), where
          - P1P2: A vector with 3 elements, defining the edge between P1 and P2. Shape: (3,).
          - P2P3: A vector with 3 elements, defining the edge between P2 and P3. Shape: (3,).
          - P3P1: A vector with 3 elements, defining the edge between P3 and P1. Shape: (3,).
    """
    ### STUDENT CODE
    # TODO: Implement this function.

    # NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    P1P2 = P2 - P1
    P2P3 = P3 - P2
    P3P1 = P1 - P3

    ### END STUDENT CODE

    return P1P2, P2P3, P3P1


def compute_lengths(
        P1P2: np.ndarray, P2P3: np.ndarray, P3P1: np.ndarray
) -> list[float]:
    """
    Computes the lengths of the triangle's edges given the vertices.

    Args:
        P1P2: A vector with 3 elements, defining the edge between P1 and P2. Shape: (3,).
        P2P3: A vector with 3 elements, defining the edge between P2 and P3. Shape: (3,).
        P3P1: A vector with 3 elements, defining the edge between P3 and P1. Shape: (3,).

    Returns:
        A list with the lengths of the edges P1P2, P2P3, P3P1.
    """
    ### STUDENT CODE

    norms = [float(np.sqrt(e[0] ** 2 + e[1] ** 2 + e[2] ** 2)) for e in [P1P2, P2P3, P3P1]]

    ### END STUDENT CODE

    return norms


def compute_normal_vector(
        P1P2: np.ndarray, P2P3: np.ndarray, P3P1: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    """
    Calculates the normal vector as well as the normal vector with length = 1.

    Args:
        P1P2: A vector with 3 elements, defining the edge between P1 and P2. Shape: (3,).
        P2P3: A vector with 3 elements, defining the edge between P2 and P3. Shape: (3,).
        P3P1: A vector with 3 elements, defining the edge between P3 and P1. Shape: (3,).

    Returns:
        A tuple (n, n_normalized), where
          - n: A vector with 3 elements, defining the normal vector of the triangle.
            Shape: (3,).
          - n_normalized: A vector with 3 elements, defining the normalized normal vector.
            Shape: (3,).
    """
    ### STUDENT CODE

    n = np.cross(P1P2, P2P3)

    length = np.linalg.norm(n)

    n_normalized = n

    if length > 0:
        n_normalized = n_normalized / length

    ### END STUDENT CODE

    return n, n_normalized


def compute_triangle_area(n: np.ndarray) -> float:
    """
    Returns the area of the triangle given its normal vector.

    Args:
        n: A vector with 3 elements, defining the normal vector of the triangle. Shape: (3,).

    Returns:
        The area of the triangle.
    """
    ### STUDENT CODE

    # the length of n is equivalent to a * h, a triangles area is half of that
    area = float(0.5 * np.linalg.norm(n))

    ### END STUDENT CODE

    return area


def compute_angles(
        P1P2: np.ndarray, P2P3: np.ndarray, P3P1: np.ndarray
) -> tuple[float, float, float]:
    """
    Computes the angles of the triangle given its vertices. The angles should be
    returned in degrees.

    Args:
        P1P2: A vector with 3 elements, defining the edge between P1 and P2. Shape: (3,).
        P2P3: A vector with 3 elements, defining the edge between P2 and P3. Shape: (3,).
        P3P1: A vector with 3 elements, defining the edge between P3 and P1. Shape: (3,).

    Returns:
        A tuple (alpha, beta, gamma), where
          - alpha: The angle at vertex P1.
          - beta: The angle at vertex P2.
          - gamma: The angle at vertex P3.
    """
    ### STUDENT CODE

    alpha = np.arccos(np.dot(P1P2, -P3P1) / (np.linalg.norm(P1P2) * np.linalg.norm(P3P1)))
    beta = np.arccos(np.dot(P2P3, -P1P2) / (np.linalg.norm(P1P2) * np.linalg.norm(P2P3)))
    gamma = np.arccos(np.dot(P3P1, -P2P3) / (np.linalg.norm(P3P1) * np.linalg.norm(P2P3)))

    ### END STUDENT CODE

    return alpha, beta, gamma
