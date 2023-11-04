import matplotlib.pyplot as plt

if __name__ == '__main__':
    path = "G:\Programming\PythonUtils\img_encryption\img_1.jpg"
    img = plt.imread(path)
    img_flat = img.reshape(-1)
    print(img_flat)