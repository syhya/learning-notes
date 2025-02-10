import torch

def relu(x):
    torch_zero = torch.tensor(0)
    return torch.maximum(x, torch_zero)

x = torch.randn(2, 3, 4)

x_relu = relu(x)
print(x_relu)