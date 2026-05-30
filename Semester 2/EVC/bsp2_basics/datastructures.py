# Copyright TU Wien (2022) - EVC: Task2
# Institute of Computer Graphics and Algorithms.

import numpy as np


def define_structures() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Defines the two vectors v1 and v2 as well as the matrix M determined by your
    matriculation number.

    Returns:
        A tuple (v1, v2, M), where
          - v1: Vector with 3 elements. Shape: (3,).
          - v2: Vector with 3 elements. Shape: (3,).
          - M: Matrix with 3 rows and 3 columns. Shape: (3, 3).
    """
    ### STUDENT CODE

    # 1 2 5 2 7 1 8 4
    # A B C D E F G H

    v1 = np.array([2, 1, 5])
    v2 = np.array([1, 2, 7])
    M = np.array([[2, 2, 5], [2, 8, 1], [7, 4, 1]])

    ### END STUDENT CODE

    return v1, v2, M


def sequence(M: np.ndarray) -> np.ndarray:
    """
    Defines a vector given by the minimum and maximum digit of your
    matriculation number. Step size = 0.25.

    Args:
        M: The matrix defined by your matriculation number. Shape: (3, 3).

    Returns:
        A vector with (max - min) * 4 + 1 elements.
        Shape: ((max - min) * 4 + 1,).
    """
    ### STUDENT CODE

    result = np.arange(np.min(M), np.max(M) + 0.1, 0.25)

    ### END STUDENT CODE

    return result


def matrix(M: np.ndarray) -> np.ndarray:
    """
    Defines the 15x9 block matrix as described in the task description.

    Args:
        M: The matrix defined by your matriculation number. Shape: (3, 3).

    Returns:
        A matrix with 15 rows and 9 columns.
        Shape: (15, 9).
    """
    ### STUDENT CODE

    # NOTE: Loops, or functions that use loops internally, are forbidden for
    #       this task.

    # NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    a = np.hstack((M, np.zeros_like(M), M))
    b = np.hstack((np.zeros_like(M), M, np.zeros_like(M)))

    r = np.vstack((a, b, a, b, a))

    ### END STUDENT CODE

    return r


def dot_product(v1: np.ndarray, v2: np.ndarray) -> float:
    """
    Dot product of v1 and v2.

    Args:
        v1: A vector with 3 elements. Shape: (3,).
        v2: A vector with 3 elements. Shape: (3,).

    Returns:
        The dot product of v1 and v2.
    """
    ### STUDENT CODE

    r = sum([v1[i] * v2[i] for i in range(3)])

    ### END STUDENT CODE

    return r


def cross_product(v1: np.ndarray, v2: np.ndarray) -> np.ndarray:
    """
    Cross product of v1 and v2.

    Args:
        v1: A vector with 3 elements. Shape: (3,).
        v2: A vector with 3 elements. Shape: (3,).

    Returns:
        The cross product of v1 and v2.
        Shape: (3,).
    """
    ### STUDENT CODE

    r = np.array([v1[1] * v2[2] - v1[2] * v2[1], v1[2] * v2[0] - v1[0] * v2[2], v1[0] * v2[1] - v1[1] * v2[0]])

    ### END STUDENT CODE

    return r


def vector_X_matrix(v: np.ndarray, M: np.ndarray) -> np.ndarray:
    """
    Defines the vector-matrix multiplication v*M.

    Args:
        v: A vector with 3 elements. Shape: (3,).
        M: A matrix with 3 rows and 3 columns. Shape: (3, 3).

    Returns:
        The result of the vector-matrix multiplication v*M.
        Shape: (3,).
    """
    ### STUDENT CODE

    r = np.array([dot_product(v, M[:, i]) for i in range(3)])

    ### END STUDENT CODE

    return r


def matrix_X_vector(M: np.ndarray, v: np.ndarray) -> np.ndarray:
    """
    Defines the matrix-vector multiplication M*v.

    Args:
        M: A matrix with 3 rows and 3 columns. Shape: (3, 3).
        v: A vector with 3 elements. Shape: (3,).

    Returns:
        The result of the matrix-vector multiplication M*v.
        Shape: (3,).
    """
    ### STUDENT CODE

    r = np.array([dot_product(v, M[i, :]) for i in range(3)])

    ### END STUDENT CODE

    return r


def matrix_X_matrix(M1: np.ndarray, M2: np.ndarray) -> np.ndarray:
    """
    Defines the matrix multiplication M1*M2.

    Args:
        M1: A matrix with 3 rows and 3 columns. Shape: (3, 3).
        M2: A matrix with 3 rows and 3 columns. Shape: (3, 3).

    Returns:
        The result of the matrix multiplication M1@M2.
        Shape: (3, 3).
    """
    ### STUDENT CODE

    r = np.array([[dot_product(M1[i, :], M2[:, j]) for j in range(3)] for i in range(3)])

    ### END STUDENT CODE

    return r


def matrix_Xc_matrix(M1: np.ndarray, M2: np.ndarray) -> np.ndarray:
    """
    Defines the element-wise matrix multiplication M1*M2 (Hadamard Product).

    Args:
        M1: A matrix with 3 rows and 3 columns. Shape: (3, 3).
        M2: A matrix with 3 rows and 3 columns. Shape: (3, 3).

    Returns:
        The result of the element-wise matrix multiplication M1*M2.
        Shape: (3, 3).
    """
    ### STUDENT CODE
    # TODO: Implement this function.

    # NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    r = np.array([[M1[i, j] * M2[i, j] for j in range(3)] for i in range(3)])

    ### END STUDENT CODE

    return r
