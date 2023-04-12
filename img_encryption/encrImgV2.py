import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def deviate(matrix, val):
    return matrix + val


def restore(matrix, val):
    return matrix - val


def encrypt(path, key):
    np.random.seed(key)
    img = plt.imread(path)
    img = img.copy()
    offsetArr = np.random.randint(low=0, high=255, size=img.shape[0])
    dim = img.shape[:2]
    offset = np.vectorize(deviate)
    for i in range(img.shape[0]):
        img[i] = offset(img[i], offsetArr[i])
    with open("encry.cbrei", "wb") as f:
        np.savez(f, img, dim)


def decrypt(path, key):
    with np.load(path) as f:
        img, dim = f.values()
    np.random.seed(key)
    offsetArr = np.random.randint(low=0, high=255, size=dim[0])
    recover = np.vectorize(restore)
    for i in range(img.shape[0]):
        img[i] = recover(img[i], offsetArr[i])
    im = Image.fromarray(img)
    im.save("decry.jpg")


if __name__ == '__main__':
    # encrypt("ttm.jpg", 9123)
    decrypt("encry.cbrei", 9123)