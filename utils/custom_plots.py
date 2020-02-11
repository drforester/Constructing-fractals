import matplotlib.pyplot as plt
import numpy as np
import warnings
from skimage.color import gray2rgb
from skimage import img_as_ubyte
import matplotlib.patches as patches


warnings.filterwarnings("ignore", category=UserWarning)
plt.style.use('dark_background')
# https://matplotlib.org/examples/color/named_colors.html
colors = {1:'deepskyblue', 2:'lightskyblue', 3:'limegreen', 4:'orangered',
          5:'red', 6:'gold', 7:'snow', 8:'black'}

spines = ['top','bottom','left','right']
fc='black'
cm = 'gray'
theme_col = colors[5]
ticks_col = colors[6]
title_col = colors[6]
fig, ax = plt.subplots(1, 1, figsize=(6.25,6.25)) # display single image
fig.patch.set_facecolor(fc)
    
    
def show_img(img, name, cm=cm, pause=True):
    plt.ion()
    plt.imshow(img, cmap=cm)
    plt.show()

    for sp in spines:
        ax.spines[sp].set_color(theme_col)

    if type(name)==int:
        ax.set_title('frame '+str(name), fontname='Hack')
    else:
        ax.set_title(name, fontname='Hack')
    ax.title.set_color(title_col)

    plt.xticks([])
    plt.yticks([])
    ax.set_xticklabels([])
    ax.set_yticklabels([]) 
    
    plt.tight_layout()
    plt.draw()
    if pause:
        input('')
    plt.pause(0.0001)
    plt.cla()
    
    

def write_png(img, out_path, cm='gray'):
    plt.imshow(img, cmap=cm)
    for sp in spines:
        ax.spines[sp].set_visible(False)
    plt.xticks([])
    plt.yticks([])
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    plt.savefig(out_path, bbox_inches='tight', pad_inches=0)
    plt.cla()



def write_img(img, title, out_path, cm='gray'):
    plt.ion()
    plt.yticks(fontname="Hack")
    plt.xticks(fontname="Hack")    
    #fig, ax = plt.subplots(1, 1, figsize=(8,5))
    plt.imshow(img, cmap=cm)
    for sp in spines:
        ax.spines[sp].set_color(theme_col)
    ax.tick_params(axis='x', colors=ticks_col)
    ax.tick_params(axis='y', colors=ticks_col)
    ax.yaxis.label.set_color(theme_col)
    ax.xaxis.label.set_color(theme_col)
    # plt.xticks([])
    # plt.yticks([])
    # ax.set_xticklabels([])
    # ax.set_yticklabels([])
    #ax.set_title(title)
    ax.set_title(title, fontname='Hack', fontsize=14)
    ax.title.set_color(title_col)
    plt.tight_layout()
    plt.savefig(out_path, bbox_inches='tight')
    plt.cla()
