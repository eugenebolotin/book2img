#!/usr/bin/env python

import sys
import math
from PIL import Image, ImageDraw

def text_to_img( text_filename, img_filename ):
    text = open( text_filename ).read()

    total_pixels = ( len( text ) + 2 ) / 3
    height = int( math.sqrt( total_pixels ) )
    width = ( total_pixels + height - 1 ) / height

    im = Image.new( "RGB", ( width, height ), ( 0, 0, 0 ) )
    for i in xrange( total_pixels ):
        x = i % width
        y = i / width

        r = ord( text[ i * 3 ] )
        g = ord( text[ i * 3 + 1 ] )
        b = ord( text[ i * 3 + 2 ] )
        
        im.putpixel( ( x, y ), ( r, g, b ) )

    im.save( img_filename, img_filename[ img_filename.rfind( "." ) + 1: ], option='optimize' ) 


text_to_img( sys.argv[ 1 ], sys.argv[ 2 ] )
