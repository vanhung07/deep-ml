import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    try:
        matrix = np.array(a)
        matrix = matrix.reshape(new_shape)
        return matrix.tolist()
    except ValueError:
        return []