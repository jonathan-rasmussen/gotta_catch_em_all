"""MNIST DataModule"""

import argparse

from torch.utils.data import random_split
from torchvision.datasets import MNIST as TorchMNIST
from torchvision import transforms

from data.base_data_module import BaseDataModule, load_and_print_info 

