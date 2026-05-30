# Copyright TU Wien (2022) - EVC: Task2
# Institute of Computer Graphics and Algorithms.

import numpy as np
import scipy.ndimage
import utils
from PIL import Image


def read_img(inp: str) -> Image.Image:
    """
    Returns a PIL Image given by its input path.

    Args:
        inp: The path to the input image.

    Returns:
        A PIL Image object.
    """
    img = Image.open(inp)
    return img


def convert(img: Image.Image) -> np.ndarray:
    """
    Converts a PIL image [0,255] to a numpy array [0,1].

    Args:
        img: A PIL Image object.

    Returns:
        A float numpy array of the image in range [0,1].
    """
    ### STUDENT CODE

    out = np.array(img) / 255.0

    ### END STUDENT CODE

    return out


def switch_channels(img: np.ndarray) -> np.ndarray:
    """
    Swaps the red and green channel of an RGB image given by a numpy array.

    Args:
        img: A numpy array of shape (H, W, 3) representing an RGB image.

    Returns:
        A numpy array of shape (H, W, 3) with the red and green channels swapped.
    """
    ### STUDENT CODE

    out = img.copy()
    out = out[:, :, [1, 0, 2]]

    ### END STUDENT CODE

    return out


def image_mark_green(img: np.ndarray) -> np.ndarray:
    """
    Returns a numpy-array (HxW) with 1 where the green channel of the input
    image is greater than or equal to 0.7, otherwise zero.

    Args:
        img: A numpy array of shape (H, W, 3) representing an RGB image.

    Returns:
        A numpy array of shape (H, W) with 1 where the green channel is >= 0.7, otherwise 0.
    """
    ### STUDENT CODE

    mask = (img[:, :, 1] >= 0.7).astype(int)

    ### END STUDENT CODE

    return mask


def image_masked(img: np.ndarray, mask: np.ndarray) -> np.ndarray:
    """
    Sets the pixels of the input image to zero where the mask is 1.

    Args:
        img: A numpy array of shape (H, W, 3) representing an RGB image.
        mask: A numpy array of shape (H, W) with 1 where the pixel should be masked, otherwise 0.

    Returns:
        A numpy array of shape (H, W, 3) where the pixels are set to zero where the mask is 1.
    """
    ### STUDENT CODE

    out = img.copy()
    out[mask == 1] = 0

    ### END STUDENT CODE

    return out


def grayscale(img: np.ndarray) -> np.ndarray:
    """
    Returns a grayscale image of the input. Use utils.rgb2gray().

    Args:
        img: A numpy array of shape (H, W, 3) representing an RGB image.

    Returns:
        A numpy array of shape (H, W) representing the grayscale image.
    """
    ### STUDENT CODE

    out = utils.rgb2gray(img)

    ### END STUDENT CODE

    return out


def cut_and_reshape(img_gray: np.ndarray) -> np.ndarray:
    """
    Cuts the image in half (x-dim) and stacks it together in y-dim.

    Args:
        img_gray: A numpy array of shape (H, W) representing a grayscale image.

    Returns:
        A numpy array of shape (2*H, W/2) representing the cut and reshaped image.
    """
    ### STUDENT CODE

    out = np.vstack((img_gray[:, img_gray.shape[1] // 2:], img_gray[:, :img_gray.shape[1] // 2]))

    ### END STUDENT CODE

    return out


def filter_image(img: np.ndarray) -> np.ndarray:
    """
    Filters the image with the gaussian kernel given below.

    Args:
        img: A numpy array of shape (H, W, 3) representing an RGB image.

    Returns:
        A numpy array of shape (H, W, 3) representing the filtered image.
    """
    gaussian = utils.gauss_filter(5, 2)

    ### STUDENT CODE

    # create new empty dimension (5, 5, 1) to enable multiplication with image cutout (5, 5, 3)
    # multiplication possible if last dimension equal to other or 1
    # much faster than using a loop to set each color-value
    gaussian = gaussian[:, :, np.newaxis]

    h, w, _ = img.shape

    out = np.zeros(img.shape)

    padded_img = np.pad(img, ((2, 2), (2, 2), (0, 0)), "constant", constant_values=0)

    for y in range(h):
        for x in range(w):
            # calculate sum over x- (0) and y-axis (1) and leave the color (2) as is => result is [r, g, b]
            out[y, x] = np.sum(padded_img[y:y + 5, x:x + 5, :] * gaussian, axis=(0, 1))
    ### END STUDENT CODE

    return out


def horizontal_edges(img: np.ndarray) -> np.ndarray:
    """
    Defines a sobel kernel to extract horizontal edges and convolves the image with it.

    Args:
        img: A numpy array of shape (H, W, 3) representing an RGB image.

    Returns:
        A numpy array of shape (H, W) representing the horizontal edges of the image.
    """
    ### STUDENT CODE

    sobel = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
    out = scipy.ndimage.correlate(img, sobel, mode='constant', cval=0)

    ### END STUDENT CODE

    return out
