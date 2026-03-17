'''
# Library T4PPC
Transformer for Pyglet / PIL Coordinates.

 !! Requirements: pyglet, PIL (Pillow)

Description: 
    A simple library to transfer pil and pyglet's coordinates.
'''

if __name__ == '__main__':
    print(__doc__); input(); quit()

ETRMetadata = (
    'lib.extend.t4ppc', 
    ('lib', 'extend', 't4ppc'), 
    '1.0', 
    (1, 0), 
    'Transformer for Pyglet / PIL Coordinates.', 
)

def transfer(x, y, w, h, ww, wh): 
    return (
        x, wh - y - h, x + w, wh - y, 
    )