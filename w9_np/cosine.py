import numpy as np

def cosine_sim(v1, v2):
    product = sum(x * y for x, y in zip(v1, v2))
    len1 = sum(x**2 for x in v1) ** 0.5
    len2 = sum(x**2 for x in v2) ** 0.5
    sim = product / (len1 * len2)
    return sim


def cosine_sim_np(v1, v2):
    dot = np.dot(v1, v2)
    mag1 = np.linalg.norm(v1)
    mag2 = np.linalg.norm(v2)
    return dot / (mag1 * mag2)


v1 = [1, 1]
v2 = [-1, -1]
v3 = [-1, 1]