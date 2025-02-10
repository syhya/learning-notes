# rms_norm

import torch
import torch.nn as nn

class RMSNorm(nn.Module):
    def __init__(self, hidden_dim, eps=1e-5):
        super().__init__()
        self.gamma = nn.Parameter(torch.ones(hidden_dim))
        self.eps = eps
    
    def forward(self, x):
        rms = torch.sqrt(torch.mean(x ** 2, dim=-1, keepdim=True) + self.eps)
        x_norm = x / rms
        res =  self.gamma * x_norm
        return res

x = torch.randn(2, 3, 4)

print(f"x is {x}")
rms_norm = RMSNorm(hidden_dim=4)
x_rms_norm = rms_norm.forward(x)
print(f"x_rms_norm is {x_rms_norm}")


rms_norm_val = torch.sqrt(x_rms_norm.pow(2).mean(dim=-1))
print(f"rms_norm_val is {rms_norm_val}")