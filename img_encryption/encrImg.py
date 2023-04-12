import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def encryption(path, key):
    np.random.seed(key)
    img = plt.imread(path)

    offset = np.random.randint(low=0, high=255, size=img.shape)
    encry_img = []
    img_flat = img.reshape(-1)
    offset_flat = offset.reshape(-1)
    for i in range(0, len(img_flat)):
        encry_img.append((img_flat[i] + offset_flat[i]) % 256)
    encr_np_arr = np.array(encry_img, dtype=np.uint8)
    im = Image.fromarray(encr_np_arr.reshape(img.shape))
    im.save(path+"_cbrEncry.jpg")


def deciphering(path, key):
    encr_np_arr = plt.imread(path)
    np.random.seed(key)
    shape = encr_np_arr.shape
    offset_flat = np.random.randint(low=0, high=255, size=shape).reshape(-1)
    decry_img = []
    encr_np_arr = encr_np_arr.reshape(-1)
    for i in range(0, len(encr_np_arr)):
        if encr_np_arr[i] - offset_flat[i] < 0:
            decry_img.append(256 + encr_np_arr[i] - offset_flat[i])
        else:
            decry_img.append(encr_np_arr[i] - offset_flat[i])
    decry_np_img = np.array(decry_img, dtype=np.uint8).reshape(shape)
    im = Image.fromarray(decry_np_img)
    im.save(path + "_deciphering.jpg")


if __name__ == '__main__':
    # encryption("ttm.jpg", 240)
    deciphering("ttm.jpg_cbrEncry.jpg", 240)
