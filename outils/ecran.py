# -*- coding: utf-8 -*-
"""Met le Journal Débrouya (couverture de l'édition) dans l'écran du téléphone de la pose « telephone ».
Usage : python3 ecran.py will-telephone.png 01-hero.png sortie.png"""
import sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from scipy import ndimage
pose=Image.open(sys.argv[1]).convert("RGBA"); a=np.array(pose).astype(int)
m=(a[...,3]>250)&(a[...,0]>235)&(a[...,1]>235)&(a[...,2]>235)
lab,n=ndimage.label(m); i=ndimage.sum(m,lab,range(1,n+1)).argmax()+1
scr=ndimage.binary_dilation(lab==i,iterations=2)
ys,xs=np.where(scr); x0,x1,y0,y1=xs.min(),xs.max(),ys.min(),ys.max(); W,H=x1-x0+1,y1-y0+1
S=4; cw,ch=W*S,H*S
c=Image.new("RGB",(cw,ch),"#FBF5EC"); d=ImageDraw.Draw(c)
hero=Image.open(sys.argv[2]).convert("RGB"); hh=round(hero.height*cw/hero.width)
c.paste(hero.resize((cw,hh),Image.LANCZOS),(0,0))
y=hh+int(cw*0.07); L=int(cw*0.07); R=cw-L; lh=int(cw*0.045)
for k,wid in enumerate([0.95,1,0.88,0.97,0.6]):
    d.rounded_rectangle((L,y,L+(R-L)*wid,y+lh),radius=lh//2,fill="#C9C2B7"); y+=int(lh*2.1)
y+=int(lh*0.8)
d.rounded_rectangle((L,y,R,min(ch-L,y+int(cw*0.42))),radius=int(cw*0.06),fill="#136D68")
yy=y+int(cw*0.08)
for wid in [0.8,0.9,0.55]:
    d.rounded_rectangle((L+int(cw*0.07),yy,L+int(cw*0.07)+(R-L-int(cw*0.14))*wid,yy+lh),radius=lh//2,fill="#FFD3AE" if wid==0.8 else "#FFFFFF"); yy+=int(lh*2.1)
c=c.resize((W,H),Image.LANCZOS)
mask=Image.fromarray((scr[y0:y1+1,x0:x1+1]*255).astype("uint8")).filter(ImageFilter.GaussianBlur(0.8))
pose.paste(c,(x0,y0),mask)
pose.save(sys.argv[3]); print(W,H)
