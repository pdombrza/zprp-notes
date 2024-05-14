def convolve(signal, kernel, mode="valid", padding=0):
    def dot(vec1, vec2):
        return sum(x * y for x, y in zip(vec1, vec2))

    if mode == "full":
        padding = len(kernel) - 1
    elif mode == "valid":
        padding = 0
    else:
        raise ValueError("Mode must be full or valid")

    padded = [0] * padding + signal + [0] * padding
    output_size = len(padded) - len(kernel) + 1
    conv = [0 for _ in range(output_size)]

    for i in range(output_size):
        conv[i] = dot(padded[i : i + len(kernel)], kernel[::-1])

    return conv

# zamiast tego całego - zaimplementowane już w numpy - np.convolve(np.array([1, 2, 3]), np.array([4, 5, 6]))