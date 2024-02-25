import numpy as np
import torch
from torch import nn


class NeuralNetwork(nn.Module):
    def __init__(self, env):

        super(NeuralNetwork, self).__init__()
        self.to(get_device())

        self.fc = nn.Linear(env.observation_space.n, 128)
        self.fc2 = nn.Linear(128, env.action_space.n)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.relu(self.fc(x))
        x = self.fc2(x)
        return x

def get_device():
    device = (
        "cuda"
        if torch.cuda.is_available()
        else "mps"
        if torch.backends.mps.is_available()
        else "cpu"
    )

    print(f"Using {device} device")

    return device