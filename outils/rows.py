import sys
from PIL import Image
im=Image.open(sys.argv[1]).convert('RGB')
x0,x1=int(sys.argv[2]),int(sys.argv[3])
W,H=im.size
px=im.load()
runs=[];start=None
for y in range(H):
    dark=any(sum(px[x,y])<300 or (px[x,y][0]>180 and px[x,y][1]<140) for x in range(x0,x1,2))
    if dark and start is None: start=y
    if not dark and start is not None: runs.append((start,y-start)); start=None
print(runs)
