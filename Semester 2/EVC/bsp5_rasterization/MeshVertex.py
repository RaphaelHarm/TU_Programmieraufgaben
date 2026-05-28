# Copyright TU Wien (2022) - EVC: Task5
# Institute of Computer Graphics and Algorithms.
from typing import TYPE_CHECKING

import numpy as np

if TYPE_CHECKING:
    from Mesh import Mesh


class MeshVertex:
    def __init__(self, mesh: "Mesh", index: int | np.ndarray):
        """
        Initializes mesh vertex.
        """
        self.mesh = mesh
        self.index = np.array(index, dtype=int)

    def get_position(self) -> np.ndarray:
        """
        Returns position of the mesh vertex.
        """
        if self.mesh.V_position is None:
            raise ValueError("Mesh vertex positions are not defined")

        return self.mesh.V_position[self.index]

    def get_color(self) -> np.ndarray:
        """
        Returns color of the mesh vertex.
        """
        if self.mesh.V_color is None:
            raise ValueError("Mesh vertex colors are not defined")

        return self.mesh.V_color[self.index]

    def get_screen_coordinates(self) -> tuple[float, float, float]:
        """
        Returns screen position of the mesh vertex.
        """
        if self.mesh.V_screen_position is None:
            raise ValueError("Mesh vertex screen positions are not defined")

        x = self.mesh.V_screen_position[self.index, 0]
        y = self.mesh.V_screen_position[self.index, 1]
        z = self.mesh.V_screen_position[self.index, 2]

        if not isinstance(x.item(), float):
            raise ValueError("Mesh vertex screen positions must be of type float")
        if not isinstance(y.item(), float):
            raise ValueError("Mesh vertex screen positions must be of type float")
        if not isinstance(y.item(), float):
            raise ValueError("Mesh vertex screen positions must be of type float")

        return float(x.item()), float(y.item()), float(z.item())

    @staticmethod
    def mix(
        a: float | np.ndarray, b: float | np.ndarray, t: float | np.ndarray
    ) -> float | np.ndarray:
        """
        Interpolates the line defined by a,b at position t and returns the
        result.
        """
        ### STUDENT CODE
        # TODO:   [TODO1] Implement the interpolation of the line defined by a and b,
        #         the interpolation coefficient is given by t.

        res = a

        ### END STUDENT CODE

        return res

    @staticmethod
    def barycentric_mix(
        a: np.ndarray,
        b: np.ndarray,
        c: np.ndarray,
        alpha: float | np.ndarray,
        beta: float | np.ndarray,
        gamma: float | np.ndarray,
    ) -> np.ndarray:
        """
        Interpolates the triangle defined by a,b,c at barycentric coordinates
        alpha, beta, gamma and returns the result.
        """
        ### STUDENT CODE
        # TODO:   [TODO3] Implement the barycentric interpolation of the triangle
        #         defined by a, b, c. The interpolation coefficients are given by
        #         alpha, beta, gamma.

        res = a

        ### END STUDENT CODE

        return res
