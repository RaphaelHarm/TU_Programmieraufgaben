# Copyright TU Wien (2022) - EVC: Task2
# Institute of Computer Graphics and Algorithms.

import matplotlib.pyplot as plt
import numpy as np


def define_transformations() -> list[np.ndarray]:
    """
    Returns the four transformations t1, .., t4 to transform the square.
    The transformations are determined by using mscale, mrotate and mtranslate.

    Returns:
        A list of four (3x3) numpy arrays representing the transformations t1, .., t4.
    """
    ### STUDENT CODE
    # TODO: Implement this function.

    # NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    t1, t2, t3, t4 = (
        mtranslate(-3, 0) @ mrotate(55),
        mrotate(55) @ mtranslate(-3, 0),
        mtranslate(3, 1) @ mrotate(-20) @ mtranslate(-2, 0) @ mscale(2, 3),
        mscale(1, 3) @ mrotate(45),
    )

    ### END STUDENT CODE

    return [t1, t2, t3, t4]


def mscale(sx: float, sy: float) -> np.ndarray:
    """
    Defines a scale matrix. The scales are determined by sx in x and sy in y
    dimension.

    Args:
        sx: The scale factor in x direction.
        sy: The scale factor in y direction.

    Returns:
        A (3x3) numpy array representing the scale transformation.
    """
    ### STUDENT CODE

    m = np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])

    ### END STUDENT CODE

    return m


def mrotate(angle: float) -> np.ndarray:
    """
    Defines a rotation matrix (z-axis) determined by the angle in degrees (!).

    Args:
        angle: The rotation angle in degrees.

    Returns:
        A (3x3) numpy array representing the rotation transformation.
    """
    ### STUDENT CODE

    angle = np.radians(angle)
    m = np.array([[np.cos(angle), -np.sin(angle), 0], [np.sin(angle), np.cos(angle), 0], [0, 0, 1]])

    ### END STUDENT CODE

    return m


def mtranslate(tx: float, ty: float) -> np.ndarray:
    """
    Defines a translation matrix. tx in x, ty in y direction.

    Args:
        tx: The translation in x direction.
        ty: The translation in y direction.

    Returns:
        A (3x3) numpy array representing the translation transformation.
    """
    ### STUDENT CODE

    m = np.array([[1, 0, tx], [0, 1, ty], [0, 0, 1]])

    ### END STUDENT CODE

    return m


def transform_vertices(v: np.ndarray, m: np.ndarray) -> np.ndarray:
    """
    Transform the (3xN) vertices given by v with the (3x3) transformation matrix
    determined by m.

    Args:
        v: A (3xN) numpy array representing the vertices to be transformed.
        m: A (3x3) numpy array representing the transformation matrix.

    Returns:
        A (3xN) numpy array representing the transformed vertices.
    """
    ### STUDENT CODE

    out = m @ v

    ### END STUDENT CODE

    return out


def display_vertices(v: np.ndarray, title: str) -> None:
    """
    Plot the vertices in a matplotlib figure.

    Args:
        v: A (3xN) numpy array representing the vertices to be displayed.
        title: The title of the plot.
    """
    # create the figure and set the title
    plt.figure()
    plt.axis("square")

    plt.title(title, fontsize=8, fontweight="bold")

    # x and y limits
    plt.xlim((-6, 6))
    plt.ylim((-6, 6))
    plt.xticks(range(-6, 6), fontsize=6)
    plt.yticks(range(-6, 6), fontsize=6)

    # plot coordinate axis
    plt.axvline(color="black", linewidth=0.5)
    plt.axhline(color="black", linewidth=0.5)

    plt.gca().spines[["top", "right"]].set_visible(False)
    plt.grid(linestyle="--", linewidth=0.5, alpha=0.5)

    # we just add the last element, so plot can do our job :)
    v_ = np.concatenate((v, v[:, 0].reshape(3, -1)), axis=1)
    # _annotate_points(v_) # NOTE: You can uncomment this line to annotate the points with their coordinates.

    plt.plot(v_[0, :], v_[1, :], linewidth=1)
    plt.show()


def _annotate_points(v: np.ndarray) -> None:
    """
    Annotates the points of the quad with their coordinates.
    The annotation is placed in a way that it does not overlap with the point
    and is readable.

    Args:
        v: A (3xN) numpy array representing the vertices to be annotated.
    """
    xmin, xmax = np.min(v[0, :]), np.max(v[0, :])
    ymin, _ = np.min(v[1, :]), np.max(v[1, :])
    for i in range(v.shape[1] - 1):
        annotation = f"({v[0, i]:.2f}, {v[1, i]:.2f})"
        x = v[0, i]
        y = v[1, i]
        if x <= xmin:
            x -= 0.1
            ha = "right"
            va = "center"
        elif x >= xmax:
            x += 0.1
            ha, va = "left", "center"
        else:
            if y <= ymin:
                y -= 0.1
                ha, va = "center", "top"
            else:
                y += 0.1
                ha, va = "center", "bottom"
        plt.text(x, y, annotation, fontsize=3, ha=ha, va=va, color="grey")
