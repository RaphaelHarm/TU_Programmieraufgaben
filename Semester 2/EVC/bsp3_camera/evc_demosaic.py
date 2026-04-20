# Copyright TU Wien (2022) - EVC: Task3
# Computer Vision Lab
# Institute of Computer Graphics and Algorithms

import numpy as np
import scipy.ndimage


def evc_demosaic_pattern(
        input_image: np.ndarray, pattern: str = "RGGB"
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Extracts the red, green and blue values of the 'input' image. Results are
    stored in the R, G, B variables.

    Args:
        input_image: Bayer-Pattern image.
        pattern: Bayer-Pattern.

    Returns:
        A tuple (R, G, B), where
          - R is the red channel of the image. (without interpolation)
          - B is the green channel of the image. (without interpolation)
          - G is the blue channel of the image. (without interpolation)
    """
    ### STUDENT CODE

    R = np.zeros(input_image.shape, dtype=input_image.dtype)
    G = np.zeros(input_image.shape, dtype=input_image.dtype)
    B = np.zeros(input_image.shape, dtype=input_image.dtype)

    cm = {"R": R, "G": G, "B": B}

    c = cm.get(pattern[0])
    c[::2, ::2] = input_image[::2, ::2]

    c = cm.get(pattern[1])
    c[::2, 1::2] = input_image[::2, 1::2]

    c = cm.get(pattern[2])
    c[1::2, ::2] = input_image[1::2, ::2]

    c = cm.get(pattern[3])
    c[1::2, 1::2] = input_image[1::2, 1::2]

    ### END STUDENT CODE

    return R, G, B


def evc_transform_neutral(
        R: np.ndarray,
        G: np.ndarray,
        B: np.ndarray,
        asShotNeutral: tuple[float, float, float],
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Changes the red, green and blue channels depending on the neutral white
    value (asShotNeutral). Therefore, every channel needs to be divided by the
    respective channel of the white value.

    Args:
        R: The red channel of the image.
        G: The green channel of the image.
        B: The blue channel of the image.
        asShotNeutral: The neutral white value. (RGB vector)

    Returns:
        A tuple (R_trans, G_trans, B_trans), where
          - R_trans is the red channel of the image. (changed by neutral white
            value)
          - G_trans is the green channel of the image. (changed by neutral white
            value)
          - B_trans is the blue channel of the image. (changed by neutral white
            value)
    """
    ### STUDENT CODE

    R_trans = R / asShotNeutral[0]
    G_trans = G / asShotNeutral[1]
    B_trans = B / asShotNeutral[2]

    ### END STUDENT CODE

    return R_trans, G_trans, B_trans


def evc_interpolate(
        red: np.ndarray, green: np.ndarray, blue: np.ndarray
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Interpolates the red, green and blue channels. In the final image, every
    pixel now has red, green and blue values.

    Args:
        red: The red channel of the image.
        green: The green channel of the image.
        blue: The blue channel of the image.

    Returns:
        A tuple (R_inter, G_inter, B_inter) where
          - R_inter is the red channel of the image (without missing values)
          - G_inter is the green channel of the image (without missing values)
          - B_inter is the blue channel of the image (without missing values)
    """
    ### STUDENT CODE

    g_filter = np.array([[0., 0.25, 0.], [0.25, 1., 0.25], [0., 0.25, 0.]])
    rb_filter = np.array([[0.25, 0.5, 0.25], [0.5, 1., 0.5], [0.25, 0.5, 0.25]])

    R_inter = scipy.ndimage.correlate(red, rb_filter, mode='constant')
    G_inter = scipy.ndimage.correlate(green, g_filter, mode='constant')
    B_inter = scipy.ndimage.correlate(blue, rb_filter, mode='constant')

    ### END STUDENT CODE

    return R_inter, G_inter, B_inter


def evc_concat(R: np.ndarray, G: np.ndarray, B: np.ndarray) -> np.ndarray:
    """
    Combines the three individual red, green and blue channels to a single
    image.

    Args:
        R: The red channel of the image.
        G: The green channel of the image.
        B: The blue channel of the image.

    Returns:
        The resulting image.
    """
    ### STUDENT CODE

    result = np.dstack((R, G, B))

    ### END STUDENT CODE

    return result
