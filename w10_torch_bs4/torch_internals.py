import torch

tensor = torch.tensor(([1.0, 2.0], [3.0, 4.0]), requires_grad=True)
output = tensor + tensor

x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
y = x + 2

print(x.is_leaf)
print(y.is_leaf)

y.sum().backward()

print(y.grad)
print(x.grad)