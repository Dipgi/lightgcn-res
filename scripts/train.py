import torch
from src.model import LightGCN

def train():

    num_users = 1000
    num_items = 2000

    model = LightGCN(num_users, num_items, 64)

    print("Model initialized")

if __name__ == "__main__":
    train()
