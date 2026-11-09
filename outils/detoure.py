import sys, numpy as np
from PIL import Image
from scipy import ndimage
src, out = sys.argv[1], sys.argv[2]
im = Image.open(src).convert("RGBA"); a = np.array(im)
rgb = a[..., :3].astype(int)
light = (rgb.min(axis=2) > 232)              # fond blanc / quasi blanc
lab, n = ndimage.label(light)
border = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))) - {0}
bg = np.isin(lab, list(border))
bg = ndimage.binary_dilation(bg, iterations=1) & (rgb.min(axis=2) > 200)  # ronge le liseré clair
a[..., 3] = np.where(bg, 0, 255)
Image.fromarray(a).save(out)
print(out, im.size)
