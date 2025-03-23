import torch

x = torch.tensor([1, 2, 3])

def log_softmax(x):
    x_safe = x - torch.max(x)
    x_exp  = torch.exp(x_safe)
    y = x_safe - torch.log(torch.sum(x_exp))
    return y

def high_dim_log_softmax(x):
    x_safe = x - torch.max(x, dim=-1, keepdim=True)[0]
    x_exp = torch.exp(x_safe)
    y = x_safe - torch.log(torch.sum(x_exp, dim=-1, keepdim=True))
    return y
    
res = log_softmax(x)
print(res)
print(torch.sum(torch.exp(res)))


x_h = torch.randn(2, 3, 4)
res2 = high_dim_log_softmax(x_h)
print(res2)
print(torch.sum(torch.exp(res2), 
                dim=-1, keepdim=True))