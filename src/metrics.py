import numpy as np

def precision_at_k(recommended, relevant, k):

    recommended = recommended[:k]

    hits = len(set(recommended) & set(relevant))

    return hits / k
