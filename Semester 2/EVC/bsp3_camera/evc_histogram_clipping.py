# Copyright TU Wien (2022) - EVC: Task3
# Computer Vision Lab
# Institute of Computer Graphics and Algorithms

import numpy as np


def evc_prepare_histogram_range(
    input_image: np.ndarray, low: float, high: float
) -> tuple[float, float]:
    """
    First calculates the new upper- and lower- bounds. During the normalization,
    those two values are then mapped to [0,1].
    If 'low' < 0, it should be set to 0.
    If 'high' > than the maximum intensity in the image, it should be set to the
    maximum intensity.

    Args:
        input_image: Image.
        low: Current black value.
        high: Current white value.

    Returns:
        A tuple (newLow, newHigh) where
          - newLow is the new black value.
          - newHigh is the new white value.
    """
    ### STUDENT CODE
    # TODO: Implement this function.

    # NOTE: The following two lines can be removed. They prevent the
    #       framework from crashing.

    newLow = low
    newHigh = high

    ### END STUDENT CODE

    return newLow, newHigh


def evc_transform_histogram(
    input_image: np.ndarray, newLow: float, newHigh: float
) -> np.ndarray:
    """
    Performs the 'histogram normalization' and maps the
    interval [newLow, newHigh] to [0, 1].

    Args:
        input_image: Image.
        newLow: Black value.
        newHigh: White value.

    Returns:
        The image after the histogram normalization.
    """
    ### STUDENT CODE
    # TODO: Implement this function.
    # HINT: If the current white value is smaller than the maximum intensity
    #       of the image, this function will create values larger than 1.

    # NOTE: The following line can be removed. It prevents the framework
    #       from crashing.

    result = np.zeros(input_image.shape)

    ### END STUDENT CODE

    return result


def evc_clip_histogram(input_image: np.ndarray) -> np.ndarray:
    """
    After the transformation of the histogram, evc_clip_histogram sets all
    values that are < 0 to 0 and values that are > 1 to 1.

    Args:
        input_image: The image after the histogram normalization.

    Returns:
        The image after the clipping operation.
    """
    ### STUDENT CODE
    # TODO: Implement this function.

    # NOTE: The following line can be removed. It prevents the framework
    #       from crashing.

    result = np.zeros(input_image.shape)

    ### END STUDENT CODE

    return result
