import numpy as np
import os

def SaveNpy(npy, save_path, save_name):
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    if isinstance(npy, list):
        npy = np.array(npy)
    np.save(os.path.join(save_path, save_name), npy)