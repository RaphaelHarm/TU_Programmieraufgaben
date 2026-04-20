# Copyright TU Wien (2022) - EVC: Task3
# Computer Vision Lab
# Institute of Computer Graphics and Algorithms

import numpy as np


def evc_white_balance(input_image: np.ndarray, white: np.ndarray) -> np.ndarray:
    """
    Performs white balancing manually.

    Args:
        input_image: Image.
        white: A color (as RGB vector) that should become the new white.

    Returns:
        The image after the white balance.
    """
    ### STUDENT CODE

    # HINT: Make sure the program does not crash if 'white' is zero!

    # NOTE: pixels brighter than 'white' will have values > 1.
    #       This requires a normalization which will be performed
    #       during the histogram clipping.

    result = np.copy(input_image)
    white = np.where(white == 0, 1e-10, white)
    result /= white

    ### END STUDENT CODE

    result = np.minimum(result, 1)

    return result
