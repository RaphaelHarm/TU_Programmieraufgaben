# Copyright TU Wien (2022) - EVC: Task5
# Institute of Computer Graphics and Algorithms.
from typing import TYPE_CHECKING

import numpy as np
from MeshVertex import MeshVertex
from numpy.matlib import repmat

if TYPE_CHECKING:
    from Mesh import Mesh


class MeshFace:
    def __init__(self, mesh: "Mesh", index: int | np.ndarray):
        self.mesh = mesh
        self.index = np.array(index, dtype=int)

    def get_vertex(self, i: int | np.ndarray) -> MeshVertex:
        """
        Get vertex/vertices with the index/indices i.
        """
        i = np.array(i).reshape(np.asarray(i).size)

        if self.index.size > 1 and i.size > 1:
            idx = repmat((self.index) * self.mesh.vert_per_face, i.size, 1)
            idx = np.reshape(idx, (1, len(self.index) * i.size))
            idx = idx + repmat(i, 1, len(self.index))
        else:
            idx = self.index * self.mesh.vert_per_face + i
        return MeshVertex(self.mesh, idx)

    # def add_vertex(self, position: np.ndarray, color: np.ndarray):
    #     """
    #     Adds an vertex with given position and color to this face.
    #     A face can store up to 6 vertices.
    #     If more are added an error will be thrown!
    #
    #     Args:
    #         position: Position of the vertex as a row or column vector with 4
    #           components.
    #         color: Color of the vertex as a row or column vector with 3
    #           components.
    #     """
    #     if self.mesh.faces(self.index) == self.mesh.vert_per_face:
    #         raise
    #
    #     if len(position) != 4 or len(color) != 3:
    #         raise
    #
    #     V_idx = self.index * self.mesh.vert_per_face + self.mesh.faces(self.index) - 1
    #     self.mesh.V_position[V_idx] = position
    #     self.mesh.V_color[V_idx] = color
    #     self.mesh.faces[self.index] = self.mesh.faces(self.index) - 1
