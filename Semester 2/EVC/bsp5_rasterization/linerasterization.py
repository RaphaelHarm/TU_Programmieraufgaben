# Copyright TU Wien (2022) - EVC: Task5
# Institute of Computer Graphics and Algorithms.

import numpy as np
from Framebuffer import Framebuffer
from Mesh import Mesh
from MeshVertex import MeshVertex


def line_rasterization(mesh: Mesh, framebuffer: Framebuffer):
    """
    Iterates over all faces of mesh and draws lines between their vertices.

    Args:
        mesh: Mesh object to rasterize.
        framebuffer: Framebuffer.
    """
    if mesh.faces is None:
        raise ValueError("Mesh has no faces to rasterize!")

    for i in range(mesh.faces.shape[0]):
        for j in range(mesh.faces[i][0]):
            i, j = (
                np.array(i).reshape(np.asarray(i).size),
                np.array(j).reshape(np.asarray(j).size),
            )

            v1 = mesh.get_face(i).get_vertex(j)
            v2 = mesh.get_face(i).get_vertex(np.remainder(j + 1, mesh.faces[i]))
            draw_line(framebuffer, v1, v2)


def draw_line(framebuffer: Framebuffer, v1: MeshVertex, v2: MeshVertex):
    """
    Draws a line between v1 and v2 into the framebuffer using the DDA algorithm.

    Args:
        framebuffer: Framebuffer.
        v1: Vertex 1.
        v2: Vertex 2.
    """
    x1, y1, depth1 = v1.get_screen_coordinates()
    x2, y2, depth2 = v2.get_screen_coordinates()

    ### STUDENT CODE
    # TODO:   [TODO1] Implement the DDA algorithms to draw a line from v1 to v2
    #         to the given Framebuffer

    ### END STUDENT CODE
