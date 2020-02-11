import numpy as np
from utils import custom_plots

# shape and data type of the image
rows, cols = (1000, 1000)
Img = np.zeros((rows,cols), np.uint8)

# the vertices of a rotated & slightly skewed triangle
#vtx_A = (100,300)
#vtx_B = (750,850)
#vtx_C = (900,200)

# the vertices of a large triangle with base parallel to the window frame
vtx_A = (10,500)
vtx_B = (990,10)
vtx_C = (990,990)

ay, ax = vtx_A
by, bx = vtx_B
cy, cx = vtx_C

verts = [vtx_A, vtx_B, vtx_C]

x,y = (10,10) # starting location
for ii in range(36000):
    imgnumb = str(ii).zfill(5)
    
    da = np.sqrt((y-ay)**2 + (x-ax)**2)
    db = np.sqrt((y-by)**2 + (x-bx)**2)
    dc = np.sqrt((y-cy)**2 + (x-cx)**2)

    # choose at random towards which vertex to move
    idx = np.random.randint(3)
    
    # move halfway towards the indicated vertex
    delta_y = (verts[idx][0] - y) // 2
    delta_x = (verts[idx][1] - x) // 2
    y += delta_y
    x += delta_x
    print(x, y)

    # wait a few iterations to ensure point is inside the triangle
    if ii>10:
        Img[y,x] = 255

    # show every Nth image
    if ii%50==0:
        custom_plots.show_img(Img, str(ii), pause=False)
        #custom_plots.write_png(Img, './output/'+imgnumb)

#custom_plots.write_png(Img, './sattractor.png')
