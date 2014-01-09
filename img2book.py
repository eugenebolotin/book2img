#!/usr/bin/env python

import sys
from PIL import Image, ImageDraw

def chrn( val ):
    return chr( min( 255, max( 0, val ) ) )

def img_to_text( img_filename, text_filename ):
    im = Image.open( img_filename )
    width, height = im.size

    ret = ""
    delta = 5
    for y in xrange( height ):
        for x in xrange( width ):
            px = im.getpixel( ( x, y ) )
            ret += chrn( px[ 0 ] ) + chrn( px[ 1 ] ) + chrn( px[ 2 ] )

    open( text_filename, "wt" ).write( ret )            


img_to_text( sys.argv[ 1 ], sys.argv[ 2 ] )
