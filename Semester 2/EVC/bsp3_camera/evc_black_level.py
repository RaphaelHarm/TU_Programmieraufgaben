# Copyright TU Wien (2022) - EVC: Task3
# Computer Vision Lab
# Institute of Computer Graphics and Algorithms
import PIL.TiffTags
import numpy as np
from PIL import Image, TiffImagePlugin
from PIL.TiffTags import TAGS


def evc_read_file_info(filename: str) -> tuple[int, tuple[float, float, float]]:
    """
    Extracts the black level (blackLevel) and the neutral white
    value (asShotNeutral) from the image file specified by filename.

    Args:
        filename: Filename of the image.

    Returns:
        A tuple (blacklevel, asShotNeutral), where
          - blackLevel is the black level, which is stored in the image infos.
          - asShotNeutral is the neutral white value, which is stored in the
            image.
    """
    ### STUDENT CODE

    # HINT: 'PIL.TiffTags.TAGS' might be useful.

    # NOTE: The following two lines can be removed. They prevent the
    #       framework from crashing.

    img = Image.open(filename)

    meta_dict = {TAGS[key]: img.tag_v2[key] for key in img.tag_v2}

    blackLevel = meta_dict.get('BlackLevel')
    asShotNeutral = meta_dict.get('AsShotNeutral')

    ### END STUDENT CODE

    return blackLevel, asShotNeutral


def evc_transform_colors(input_image: np.ndarray, blackLevel: float) -> np.ndarray:
    """
    Adjusts the contrast such that black (blackLevel and values below) becomes 0
    and white becomes 1.
    The white value of the input image is 65535.

    Args:
        input_image: The input image.
        blackLevel: Black level of the input image.

    Returns:
        image in double format where all values are transformed from the
        interval [blackLevel, 65535] to [0, 1].
        All values below the black level have to be 0.
    """
    ### STUDENT CODE

    result = input_image.astype(np.float32)
    result -= blackLevel
    result = np.clip(result, 0, None)
    result /= 65535 - blackLevel

    ### END STUDENT CODE

    return result
