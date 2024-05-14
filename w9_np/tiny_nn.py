import numpy as np
import sys

inputs = np.array(
    [
        [0, 0, 1],
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 1],
    ]
)

outputs = np.array([0, 1, 1, 0]).T

# Sieć - warstwy: 1 warstwa (3, 4) - 3 wymiary, 4 neurony, 2 warstwa (4, 1) bo 1 output

w0 = 2 * np.random.random((3, 4)) - 1
w1 = 2 * np.random.random((4, 1)) - 1

epochs = int(sys.argv[1])

for i in range(epochs):
    layer_0 = inputs
    layer_1 = 1 / (1 + np.exp(-(layer_0 @ w0)))
    layer_2 = 1 / (1 + np.exp(-(layer_1 @ w1)))
    loss = outputs - layer_2 # Uproszczenie - przyjmujemy różnicę jako loss - można bo różniczkowalna

    if i % 1000 == 0:
        print("loss: ", np.mean(np.abs(loss)))

    dsigmoid_layer2 = loss * (layer_2 * (1 - layer_2))
    dw1 = layer_1.T @ dsigmoid_layer2
    print(dsigmoid_layer2.shape)
    dlayer1 = dsigmoid_layer2 @ w1.T
    dsigmoid_layer1 = dlayer1 * (layer_1 * (1 - layer_1))
    dw0 = layer_0.T @ dsigmoid_layer1

    w1 += dw1
    w0 += dw0

print(layer_2)