# Copyright TU Wien (2022) - EVC: Task3
# Computer Vision Lab
# Institute of Computer Graphics and Algorithms

import numpy as np


def evc_compute_binary(input_image: np.ndarray, x: float, top: int) -> np.ndarray:
    """
    Computes a binary image with the specified threshold x.

    Args:
        input_image: RGB image.
        x: Scalar threshold.
        top: If 0, the output should be inverted such that 0 becomes 1 and 1
          becomes 0.

    Returns:
        Binary RGB image which must contain either zeros or ones. The result has
        to be of type float! Make sure that all three channels are preserved
        (the operation has to be performed on every channel).
    """
    ### STUDENT CODE


    result = np.copy(input_image)
    result = (result > x) ^ (x == 0)


    ### END STUDENT CODE

    return result
