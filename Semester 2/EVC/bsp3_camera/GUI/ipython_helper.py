from io import BytesIO

import numpy as np
from IPython import display
from PIL import Image


def imEmbed(img: np.ndarray, lossless: bool = True, maxAxis: int = 500):
    if img.dtype.kind == "f":
        img = np.clip(img * 255, 0, 255).astype(np.uint8)
    size = (img.shape[1], img.shape[0])
    longestAxis = np.max(size)
    pilImg = Image.fromarray(img).resize(
        (size / longestAxis * maxAxis).astype(np.int32)
    )
    buff = BytesIO()
    format = "png" if lossless else "jpeg"
    pilImg.save(buff, format)
    dispImage = display.Image(data=buff.getvalue(), format=format)
    display.display(dispImage)
