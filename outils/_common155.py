def hero(ban, num, l1, l2, icon, H=560):
    g=(f'<image href="data:image/jpeg;base64,{ban}" x="0" y="0" width="600" height="229" preserveAspectRatio="xMidYMid slice"/>'
       f'<path d="M0 200 C120 182 240 226 360 206 S540 188 600 204 V{H} H0 Z" fill="{TEAL_M}" opacity="0.55"/>'
       f'<path d="M0 214 C120 196 240 240 360 220 S540 202 600 218 V{H} H0 Z" fill="{TEAL}"/>'
       + txt(300,272,f"ÉDITION #{num}",18,PEACH,800,ls=4) + txt(300,320,l1,36,WHITE,800) + txt(300,364,l2,32,PEACH,800))
    g+=icon
    g+=(f'<path d="M0 520 C60 506 120 532 180 520 S300 506 360 520 S480 534 540 520 S600 514 620 520 V{H} H0 Z" fill="{TEAL_D}"/>'
        f'<path d="M0 536 C60 526 120 546 180 536 S300 526 360 536 S480 546 540 536 S600 532 620 536 V{H} H0 Z" fill="#0A403C"/>')
    return svg(600,H,g,TEAL)
def rowcards(rows, bg, icon_fn=None, accent=None, size_t=22, size_l=21, head=None):
    """rows: (titre, [lignes]) ; icon_fn(cx,cy,k) -> svg"""
    g=""; y=24
    if head: g=txt(300,48,head,17,TEAL,800,ls=1); y=70
    for k,(t,lines) in enumerate(rows):
        h=(54 if t else 22)+32*len(lines); hl_=(accent==k)
        g+=f'<rect x="24" y="{y}" width="552" height="{h}" rx="14" fill="{TEAL if hl_ else WHITE}"/>'
        x0=48
        if icon_fn: g+=icon_fn(66,y+h/2,k,hl_); x0=104
        yy=y+38
        if t: g+=txt(x0,yy,t,size_t,WHITE if hl_ else INK,800,anchor="start"); yy+=34
        g+="".join(txt(x0,yy+j*32,l,size_l,WHITE if hl_ else INK,600,anchor="start") for j,l in enumerate(lines))
        y+=h+12
    return svg(600,y+12,g,bg)
def bigcards(rows,bg):
    """rows: (titre, gros, [lignes], fill, col)"""
    g=""; y=24
    for t,big,lines,fill,col in rows:
        hh=60+46+30*len(lines)+30
        g+=f'<rect x="24" y="{y}" width="552" height="{hh}" rx="16" fill="{fill}"/>'+txt(48,y+40,t,21,col,800,anchor="start")
        g+=txt(48,y+92,big,40,MANGO if fill==WHITE else (PEACH if fill==TEAL else INK),800,anchor="start")
        g+="".join(txt(48,y+126+j*30,l,20,col,600,anchor="start") for j,l in enumerate(lines))
        y+=hh+12
    return svg(600,y+12,g,bg)
def numbadge(cx,cy,k,hl_=False,col=MANGO):
    return f'<circle cx="{cx}" cy="{cy}" r="22" fill="{WHITE if hl_ else col}"/>'+txt(cx,cy+8,str(k+1),23,TEAL if hl_ else WHITE,800)
