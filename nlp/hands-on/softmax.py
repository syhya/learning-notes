# softmax
import torch
import torch.nn as nn

def original_softmax(x):
    return torch.exp(x) / torch.sum(torch.exp(x))

print("original softmax")
x = torch.randn(4)
print(x)
x_softmax = original_softmax(x)
print(x_softmax)


def softmax_one_dim(x):
    e_x = torch.exp(x - torch.max(x))
    return e_x / torch.sum(e_x)

print("one dimension softmax")
a = torch.randn(4)
print(a)
a_softmax = softmax_one_dim(a)
print(a_softmax)
print(torch.sum(a_softmax))


def softmax_high_dim(x, dim=-1):
    max_x = torch.max(x, dim=dim, keepdim=True)[0]
    e_x = torch.exp(x - max_x)
    return e_x / torch.sum(e_x, dim=dim, keepdim=True)


print("high dimensions softmax")
# (batch_size, seq_len, hidden_dim)
b = torch.randn(2, 3, 4)
print(b)
b_softmax = softmax_high_dim(b)


print(f"b_softmax is {b_softmax}")
print(torch.sum(b_softmax, dim=-1))

b_torch_softmax = torch.softmax(b, dim=-1)
print(f"b_torch_softmax is {b_torch_softmax}")
nn_softmax = nn.Softmax(dim=-1)
b_nn_softmax = nn_softmax(b)
print(f"b_nn_softmax is {b_nn_softmax}")


assert torch.allclose(b_softmax, b_torch_softmax), "b_softmax and b_torch_softmax are not equal"
assert torch.allclose(b_softmax, b_nn_softmax), "b_softmax and b_nn_softmax are not equal"
