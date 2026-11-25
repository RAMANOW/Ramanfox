# Raman Fox icon: white fox-head outline with an "R", on Raman VPN's indigo→cyan gradient (same style as its shield logo).
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os, sys
C1=(0x47,0x4b,0xe3); C2=(0x0b,0xb6,0xd8)
FONT='/workspace/work/Vazirmatn-Bold.ttf'
FOX=[(32,57),(12.5,39),(8,21),(10.5,5),(24.5,16.5),(32,15),(39.5,16.5),(53.5,5),(56,21),(51.5,39)]
NOSE=[(28.4,51),(35.6,51),(32,56.6)]
def gradient(w,h):
    g=Image.new('RGB',(w,h)); px=g.load()
    for y in range(h):
        for x in range(w):
            t=(x+y)/(w+h-2)
            px[x,y]=tuple(int(C1[i]+(C2[i]-C1[i])*t) for i in range(3))
    return g
def mark(size, scale, cx, cy, stroke):
    """White fox outline + R on a transparent layer: `scale` px per fox unit, fox centred on (cx,cy)."""
    S=4; W=size*S
    lay=Image.new('L',(W,W),0); d=ImageDraw.Draw(lay)
    ox=cx*S-32*scale*S; oy=cy*S-31*scale*S
    pts=[(ox+x*scale*S, oy+y*scale*S) for x,y in FOX]
    d.line(pts+[pts[0],pts[1]], fill=255, width=int(stroke*scale*S), joint='curve')
    f=ImageFont.truetype(FONT, int(25*scale*S))
    bb=d.textbbox((0,0),'R',font=f)
    tw=bb[2]-bb[0]; th=bb[3]-bb[1]
    d.text((ox+32*scale*S-tw/2-bb[0], oy+35*scale*S-th/2-bb[1]),'R',font=f,fill=255)
    return lay.resize((size,size),Image.LANCZOS)
def full(size, radius_frac=0.22, content=0.62):
    g=gradient(size,size).convert('RGBA')
    sc=size*content/52
    m=mark(size, sc, size/2, size/2+size*0.01, 3.6)
    white=Image.new('RGBA',(size,size),(255,255,255,255))
    g.paste(white,(0,0),m)
    if radius_frac:
        mask=Image.new('L',(size*4,size*4),0); ImageDraw.Draw(mask).rounded_rectangle([0,0,size*4-1,size*4-1],radius=int(size*4*radius_frac),fill=255)
        g.putalpha(mask.resize((size,size),Image.LANCZOS))
    return g
out=sys.argv[1]
os.makedirs(out,exist_ok=True)
full(1024).save(f'{out}/raman-fox-logo.png')
# adaptive foreground: full-bleed gradient, the mark inside the 66/108 safe zone
for d,px in dict(mdpi=108,hdpi=162,xhdpi=216,xxhdpi=324,xxxhdpi=432).items():
    os.makedirs(f'{out}/mipmap-{d}',exist_ok=True)
    full(px, radius_frac=0, content=0.40).save(f'{out}/mipmap-{d}/ic_launcher_foreground.png')
# Android TV banner 320x180 (xhdpi): gradient, mark on the left, name on the right
W,H=320,180
b=gradient(W,H).convert('RGBA')
m=mark(H, H*0.50/52, H/2, H/2, 3.6)
b.paste(Image.new('RGBA',(H,H),(255,255,255,255)),(-22,0),m)
d=ImageDraw.Draw(b)
f1=ImageFont.truetype(FONT,34); f2=ImageFont.truetype(FONT,22)
d.text((222,70),'Raman Fox',font=f1,fill='white',anchor='mm')
d.text((222,116),'رامان فاکس',font=f2,fill='white',anchor='mm',direction='rtl',language='fa')
os.makedirs(f'{out}/drawable-xhdpi',exist_ok=True)
b.convert('RGB').save(f'{out}/drawable-xhdpi/banner.png')
print('ok')
