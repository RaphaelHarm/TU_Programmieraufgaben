# Copyright TU Wien (2022) - EVC: Task5
# Institute of Computer Graphics and Algorithms.

import numpy as np
from MeshFace import MeshFace


class Mesh:
    """
    Stores all the information of a loaded model.
    The mesh consists of faces (initially triangles) which consist of vertices.
    """

    def __init__(self, V: np.ndarray, C: np.ndarray, F: np.ndarray):
        """
        Constructor for the class Mesh.

        Args:
            V: n x 4 matrix where each row corresponds to a vertex position.
            C: n x 3 matrix where each row corresponds to a vertex color.
            F: f x 3 matrix where each row corresponds to a triangle with 3
              vertex indices.
        """
        self.vert_per_face = 9  # maximum number of vertices per face, default 9
        # Clipping of a 3D triangle against a 3D box can yield up to 9 vertices.

        self.num_faces: int = F.shape[0]  # initial number of faces
        self.num_vertices: int = V.shape[0]  # initial number of vertices
        self.V_position: np.ndarray | None = np.zeros(
            (self.vert_per_face * self.num_faces, 4)
        )  # vpf x n x 4 - (vpf := vertices per face, vertex store)
        self.V_color: np.ndarray | None = np.zeros(
            (self.vert_per_face * self.num_faces, 3)
        )  # see vertices but only RGB values
        self.V_screen_position: np.ndarray | None = np.zeros(
            (self.vert_per_face * self.num_faces, 3)
        )  # vpf x n x 3 values with x, y and depth components
        self.faces: np.ndarray | None = 3 * np.ones(
            (self.num_faces, 1), dtype=int
        )  # f x 1 - number of vertices per face, face store (default use triangles)

        for i in range(self.num_faces):
            j = self.vert_per_face * i
            self.V_position[j : j + 3, :] = V[F[i, :], :]
            self.V_color[j : j + 3, :] = C[F[i, :], :]

    def get_face(self, i: int | np.ndarray) -> MeshFace:
        """
        Returns the face/faces with index/indices i.
        If any of the indices in i is out of bounds an error will be thrown!

        Args:
            i: Face index/indices which should be accessed. This can either be a
              scalar to select one face or a vector to select multiple faces at
              once.

        Returns:
            MeshFace object with index/indices i of this mesh.
        """
        ret = MeshFace(self, i)
        return ret

    def add_face(self, vertex_count: int, positions: np.ndarray, colors: np.ndarray):
        """
        Adds a face to this mesh. The face has vertex_count vertices with
        positions corresponding to rows of the parameter positions and colors
        corresponding to rows of the parameter colors. There have to be at least
        as many rows in positions and colors as the value of vertex_count.

        Args:
            vertex_count: Number of vertices of the new face.
            positions: n x 4 matrix where each row corresponds to a vertex
              position.
            colors: n x 3 matrix where each row corresponds to a vertex color.
        """
        if vertex_count < 1 or vertex_count > self.vert_per_face:
            raise ValueError(
                "Cannot add face with "
                + str(vertex_count)
                + " vertices. A face must have more than 1 and less than "
                + str(self.vert_per_face)
                + " vertices!"
            )
        elif vertex_count > positions.shape[0]:
            raise ValueError(
                "There have to be at least as many positions as in vertex count defined!"
            )
        elif vertex_count > colors.shape[0]:
            raise ValueError(
                "There have to be at least as many color as in vertex count defined!"
            )
        elif positions.shape[1] != 4 or colors.shape[1] != 3:
            raise ValueError(
                "Positions or colors have the wrong format! Positions must have 4 components and colors 3!"
            )

        positions_ = np.zeros([self.vert_per_face, 4])
        colors_ = np.zeros([self.vert_per_face, 3])
        positions_[:vertex_count] = positions[:vertex_count]
        colors_[:vertex_count] = colors[:vertex_count]

        self.faces = (
            np.concatenate([self.faces, np.array([[vertex_count]])], axis=0)
            if self.faces is not None
            else np.array([[vertex_count]])
        )
        self.V_position = (
            np.concatenate([self.V_position, positions_], axis=0)
            if self.V_position is not None
            else positions_
        )
        self.V_color = (
            np.concatenate([self.V_color, colors_], axis=0)
            if self.V_color is not None
            else colors_
        )
        self.V_screen_position = (
            np.concatenate(
                [self.V_screen_position, np.zeros([self.vert_per_face, 3])], axis=0
            )
            if self.V_screen_position is not None
            else np.zeros([self.vert_per_face, 3])
        )

    def homogenize(self):
        """
        Homogenizes all positions of this mesh. This is done by dividing each
        position by its w component.
        """
        if self.V_position is None:
            raise ValueError("There are no positions to homogenize!")

        if self.V_position.shape[0] > 0:
            zs = self.V_position[:, -1]
            zs[zs == 0] = 1e-10
            self.V_position = self.V_position / zs[:, None]

    def screen_transform(self, width: int, height: int):
        """
        Performs the viewport or screen transform where 3 coordinates in NDC
        space are transformed to screen coordinates (pixel coordinates).

        Args:
            width: Width of the framebuffer.
            height: Height of the framebuffer.
        """
        if self.V_position is None:
            raise ValueError("There are no positions to transform!")

        if self.V_screen_position is None:
            raise ValueError("There are no screen positions to transform to!")

        if self.V_position.shape[1] > 0:
            eps = 0.001
            sx = (width - eps) / 2.0
            dx = (width - eps) / 2.0
            sy = (height - eps) / -2.0
            dy = (height - eps) / 2.0
            self.V_screen_position[:, 0] = np.floor(self.V_position[:, 0] * sx + dx)
            self.V_screen_position[:, 1] = np.floor(self.V_position[:, 1] * sy + dy)
            self.V_screen_position[:, 2] = self.V_position[:, 2]

    def clear(self):
        """
        Clears the current mesh.
        """
        self.num_faces = 0
        self.num_vertices = 0
        self.V_position = None
        self.V_color = None
        self.V_screen_position = None
        self.faces = None
