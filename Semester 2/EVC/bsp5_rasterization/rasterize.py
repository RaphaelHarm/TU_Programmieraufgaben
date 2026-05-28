# Copyright TU Wien (2022) - EVC: Task5
# Institute of Computer Graphics and Algorithms.

import importlib

import fillrasterization
import linerasterization
from clip import clip
from ClippingPlane import ClippingPlane
from Framebuffer import Framebuffer
from Mesh import Mesh


def rasterize(mesh: Mesh, framebuffer: Framebuffer, mode: str = "line"):
    """
    Rasterizes a given mesh and put it into the given framebuffer.
    Mode can be selected (line, fill)
    """
    framebuffer.clear()
    clipping_planes = ClippingPlane.get_clipping_planes()

    mesh_clipped = clip(mesh, clipping_planes)

    mesh_clipped.homogenize()
    mesh_clipped.screen_transform(framebuffer.width, framebuffer.height)

    import sys

    sys.path.insert(0, sys.path[-1])

    if mode == "line":
        importlib.reload(linerasterization)
        linerasterization.line_rasterization(mesh_clipped, framebuffer)

    if mode == "fill":
        importlib.reload(fillrasterization)
        fillrasterization.fill_rasterization(mesh_clipped, framebuffer)

    sys.path.pop(0)
