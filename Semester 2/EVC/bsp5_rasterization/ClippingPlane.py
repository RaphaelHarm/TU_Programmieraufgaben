# Copyright TU Wien (2022) - EVC: Task5
# Institute of Computer Graphics and Algorithms.

import numpy as np


class ClippingPlane:
    def __init__(self, plane: np.ndarray):
        """
        Args:
            plane: Plane stored in Hessian normal form as a 1x4 vector.
        """
        self.plane = plane

    def inside(self, pos: np.ndarray) -> bool:
        """
        Checks if a given point lies behind the plane (opposite direction of
        normal vector). Points lying on the plane are considered to be inside.

        Args:
            position: Homogeneous position with 4 components.

        Returns:
            Logical value which indicates if the point is inside or not.
        """
        ### STUDENT CODE
        # TODO:   [TODO2] Implement this function.
        # HINT:   You can access the plane property via self.plane.

        # NOTE:   The following lines can be removed. They prevent the framework
        #         from crashing.

        res = False

        ### END STUDENT CODE

        return res

    def intersect(self, pos1: np.ndarray, pos2: np.ndarray) -> float:
        """
        Intersects the plane with a line between pos1 and pos2.

        Args:
            pos1: Homogeneous position with 4 components.
            pos2: Homogeneous position with 4 components.

        Returns:
            Normalized intersection value t in [0, 1].
        """
        ### STUDENT CODE
        # TODO:   [TODO2] Implement this function.
        # HINT:   You can access the plane property via self.plane.

        # NOTE:   The following lines can be removed. They prevent the framework
        #         from crashing.

        t = 0

        ### END STUDENT CODE

        return t

    @staticmethod
    def get_clipping_planes() -> list["ClippingPlane"]:
        """
        Creates and returns a list of the six Clipping planes defined in the
        task description.
        """
        ### STUDENT CODE
        # TODO:   [TODO2] Define the correct clipping planes.

        # NOTE:   The following lines can be removed. They prevent the framework
        #         from crashing.

        res = [
            ClippingPlane(np.array([0, 0, 0, 0])),
            ClippingPlane(np.array([0, 0, 0, 0])),
            ClippingPlane(np.array([0, 0, 0, 0])),
            ClippingPlane(np.array([0, 0, 0, 0])),
            ClippingPlane(np.array([0, 0, 0, 0])),
            ClippingPlane(np.array([0, 0, 0, 0])),
        ]

        ### END STUDENT CODE

        return res
