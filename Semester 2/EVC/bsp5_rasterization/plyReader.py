# Copyright TU Wien (2022) - EVC: Task5
# Institute of Computer Graphics and Algorithms.
import os

import numpy as np
from Mesh import Mesh

fdir = "data"


def check_file(file: str):
    if not os.path.isfile(os.path.join(fdir, file)):
        raise ValueError("File is missing in directory")


def check_for_files():
    fdir = os.path.join(os.getcwd(), "data")

    if not os.path.isdir(fdir):
        raise ValueError("fdir is not a directory")

    plyList = [
        "clipped_star.ply",
        "clipped_torus.ply",
        "plane.ply",
        "star.ply",
        "text.ply",
        "torus.ply",
    ]

    for file in plyList:
        check_file(file)


class PlyReaderError(RuntimeError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class PlyElementPropertyDef:
    def __init__(self, name: str, dtype: type[np.generic], islist: bool) -> None:
        self.name = name
        self.dtype = dtype
        self.isList = islist
        self.count: int | None = None


class PlyElementDef:
    def __init__(self, name: str, count: int) -> None:
        self.name = name
        self.count = count
        self.properties: list[PlyElementPropertyDef] = list()


def readPly(file: str) -> dict[str, dict[str, np.ndarray]]:
    # we need:
    # V: n x 3 matrix where each row corresponds to a vertex position.
    # C: n x 3 matrix where each row corresponds to a vertex color.
    # F: f x 3 matrix where each row corresponds to a triangle with 3 vertex indices.
    with open(file, "r") as f:
        fiter = iter(f)

        magicBytes = next(fiter).strip()
        if magicBytes != "ply":
            raise PlyReaderError("Not a ply file")

        fmat = next(fiter).strip()
        if fmat != "format ascii 1.0":
            raise PlyReaderError("Can only read ply files in ascii format")

        _comment = next(fiter).strip()  # This is the same in all of our files

        dtypes: dict[str, type[np.generic]] = {
            "float": np.float32,
            "uchar": np.ubyte,
            "uint": np.uint32,
        }

        elements: list[PlyElementDef] = list()
        headerRun = True

        while headerRun:
            line = next(fiter).strip()

            if line is None:
                raise PlyReaderError("Unexpected EOF")
            if line.startswith("element"):
                lp = line.split()
                elements.append(PlyElementDef(lp[1], int(lp[2])))
            elif line.startswith("property"):
                lp = line.split()

                if len(elements) == 0:
                    raise PlyReaderError(
                        "Invalid file structure, expected element definition"
                    )

                elem: PlyElementDef = elements[-1]

                if lp[1] == "list":
                    if lp[3] not in dtypes:
                        raise PlyReaderError("Unknown property type")

                    elem.properties.append(
                        PlyElementPropertyDef(lp[4], dtypes[lp[3]], True)
                    )
                else:
                    if lp[1] not in dtypes:
                        raise PlyReaderError("Unknown property type")

                    elem.properties.append(
                        PlyElementPropertyDef(lp[2], dtypes[lp[1]], False)
                    )
            elif line == "end_header":
                headerRun = False
            else:
                raise PlyReaderError("Malformed file, expected end_header")

        data: dict[str, dict[str, np.ndarray]] = dict()

        for elem in elements:
            data[elem.name] = dict()
            elemDat = data[elem.name]

            for prop in elem.properties:
                if not prop.isList:
                    elemDat[prop.name] = np.empty(elem.count, prop.dtype)

        for elem in elements:
            elemDat = data[elem.name]

            for i in range(elem.count):
                line = next(fiter)
                lp = line.split()
                lpIt = iter(lp)

                for prop in elem.properties:
                    if prop.isList:
                        c = int(next(lpIt))

                        if prop.name not in elemDat:
                            elemDat[prop.name] = np.empty((elem.count, c), prop.dtype)
                            prop.count = c

                        if c != prop.count:
                            raise PlyReaderError(
                                "The reader does not support varying property list lengths"
                            )

                        arr = elemDat[prop.name]

                        for j in range(c):
                            arr[i, j] = prop.dtype(next(lpIt))
                    else:
                        elemDat[prop.name][i] = prop.dtype(next(lpIt))
    return data


def load_transformed_model(file: str, aspect: int = 1):
    mesh = readPly(file)

    vertexData = mesh["vertex"]
    faceData = mesh["face"]

    F = faceData["vertex_indices"]
    V = np.stack((vertexData["x"], vertexData["y"], vertexData["z"]), axis=1)
    C = (
        np.stack((vertexData["red"], vertexData["green"], vertexData["blue"]), axis=1)
        / 255
    )

    # fmt: off
    # init MVP
    modelM = np.array(
        [
            [1, 0, 0,  0],
            [0, 1, 0,  0],
            [0, 0, 1, -3],
            [0, 0, 0,  1],
        ]
    )
    # fmt: on

    viewM = np.eye(4)
    projM = perspective_projection(90, aspect, 0.1, 10)

    # transform to clip space
    MVP = projM @ viewM @ modelM

    V = np.append(V, np.ones((V.shape[0], 1)), axis=1)
    V = (MVP @ (V.T)).T

    # init mesh object
    mesh = Mesh(V, C, F)
    return mesh


def perspective_projection(fov: float, aspect: float, nearZ: float, farZ: float):
    tanHalf = np.tan(np.pi / 180 * fov / 2)
    FN1 = -(nearZ + farZ) / (farZ - nearZ)
    FN2 = (-2 * farZ * nearZ) / (farZ - nearZ)

    # fmt: off
    proj = np.array(
        [
            [1 / (tanHalf * aspect),           0,   0,   0],
            [                     0, 1 / tanHalf,   0,   0],
            [                     0,           0, FN1, FN2],
            [                     0,           0,  -1,   0],
        ]
    )
    # fmt: on

    return proj
