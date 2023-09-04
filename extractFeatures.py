import numpy as np
import skimage
from skimage.color import rgb2gray


def extractFeatures(im, c, patch_radius):
    img = skimage.color.rgb2gray(im)
    print(c.shape)
    #print(img.shape)
    #print(c)
    img = np.pad(img, patch_radius, 'constant')
    #print(img.shape)
    coords = c[:2]
    d = ((2 * patch_radius) + 1) ** 2
    #increment = np.ones(len(coords[0]))
    #increment = increment * patch_radius
    f = np.zeros((d, c.shape[1]))
    #print(f.shape)
    for i in range(len(coords[0])):
        cx = coords[0][i] + patch_radius
        cy = coords[1][i] + patch_radius
        #print(cx)
        #print(cy)
        patch = np.zeros((2 * patch_radius + 1, 2 * patch_radius + 1))
        #print(cx)
        for j in range(2 * patch_radius + 1):
            for k in range(2 * patch_radius + 1):
                patch[j][k] = img[int(cy - patch_radius + j)][int(cx - patch_radius + k)]
        #print(patch.shape)
        patch = np.reshape(patch, (d, ))
        #print(patch.shape)
        f[:, i] = patch
    print(f.shape)
    return f


