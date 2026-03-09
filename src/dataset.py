import pandas as pd

def load_movielens(path):

    ratings = pd.read_csv(path)

    num_users = ratings["userId"].nunique()
    num_items = ratings["itemId"].nunique()

    return ratings, num_users, num_items
