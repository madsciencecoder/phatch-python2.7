# Phatch - Photo Batch Processor
# Copyright (C) 2007-2008 www.stani.be
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses/
#
# Phatch recommends SPE (http://pythonide.stani.be) for editing python.

# Embedded icon is taken from www.openclipart.org (public domain)

# Note that this is modified by TiborB
# No entitlement and credits of stani and PHATCH teams are denyied 
# by this, just the team&project seems not alive anymore

# Follows PEP8

from core import models
from lib.reverse_translation import _t


BLURED_ID = 'Blurred_x%d_y%d'

def init():
    global Image, ImageDraw, ImageFont, paste, ImageChops, ImageFilter
    from PIL import Image
    from PIL import ImageDraw
    from PIL import ImageFont
    from PIL import ImageFilter
    from PIL import ImageChops
    global calculate_location, convert_safe_mode
    from lib.imtools import calculate_location, convert_safe_mode, paste  


def draw_text(image, text, horizontal_offset, vertical_offset,
              horizontal_justification, vertical_justification, size, opacity, hallo,
              cache = {}, color='#FFFFFF', orientation=None, font=None):
    """Draws text on an image."""
    image = convert_safe_mode(image)
    img_size = image.size

    mask_layer = Image.new('L',img_size, '#FFFFFF')
    color_layer = Image.new('RGB',img_size, color)

    draw = ImageDraw.Draw(mask_layer)

    if orientation:
        orientation = getattr(Image, orientation)

    if font.strip():
        font = ImageFont.truetype(font, size)
    else:
        font = ImageFont.load_default()
        text = text.encode('ascii', 'replace')

    if orientation:
        font = ImageFont.TransposedFont(font, orientation)

    location = calculate_location(
        horizontal_offset, vertical_offset,
        horizontal_justification, vertical_justification,
        image.size, draw.textsize(text, font=font))

    if hallo:
        x,y = img_size
        blurred_id = BLURED_ID % (x,y)
        if blurred_id in cache:
			hallo_mask_layer = cache[blurred_id]
        else:
            hallo_mask_layer = Image.new('L',img_size, '#FFFFFF')
            draw_hallo = ImageDraw.Draw(hallo_mask_layer)
            draw_hallo.text(location, text, font=font, fill=255-opacity)
            n = 0
            while n < size/10:
            	hallo_mask_layer = hallo_mask_layer.filter(ImageFilter.BLUR)
            	draw_hallo.text(location, text, font=font, fill=255-opacity)
            	n += 1
            cache[blurred_id] = hallo_mask_layer
		
        hallo_color_layer = Image.new('RGB',img_size, color)
        hallo_color_layer = ImageChops.invert(hallo_color_layer)
        image = Image.composite(image,hallo_color_layer,hallo_mask_layer)
    
 
    draw.text(location, text, font=font, fill=255-opacity)
    # composite the watermark with the layer
    return Image.composite(image,color_layer,mask_layer)
    


class Action(models.OffsetMixin, models.Action):
    """Draws text on an image."""

    label = _t('Text (plus)')
    author = 'Tibor (original filer: Stani)'
    cache = True
    email = 'tiborb95@gmail.com'
    init = staticmethod(init)
    pil = staticmethod(draw_text)
    version = '0.1'
    tags = [_t('default'), _t('filter')]
    __doc__ = _t('Write text at a given position (by TB)')

    def interface(self, fields):
        fields[_t('Text')] = self.CharField(
            choices=self.STAMPS)
        fields[_t('Font')] = self.FontFileField('Free Sans')
        fields[_t('Size')] = self.PixelField('5%',
                                            choices=self.SMALL_PIXELS)
        fields[_t('Color')] = self.ColorField('#000000')
        fields[_t('Opacity')] = self.SliderField(255,0, 255)
        fields[_t('Hallo')] = self.BooleanField(False)
        #opacity = int((self.get_field('Opacity') / 100.0) * 255)

        super(Action, self).interface(fields)

    def get_relevant_field_labels(self):
        return ['Text', 'Font', 'Size', 'Color', 'Opacity', 'Hallo'] + \
            super(Action, self).get_relevant_field_labels()

    def values(self, info, pixel_fields={}):
        x, y = info['size']
        pixel_fields.update({'Size': (x + y) / 2})
        return super(Action, self).values(info,
            pixel_fields=pixel_fields)

    icon = \
'x\xda\x01\xcc\x043\xfb\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x000\x00\
\x00\x000\x08\x06\x00\x00\x00W\x02\xf9\x87\x00\x00\x00\x04sBIT\x08\x08\x08\
\x08|\x08d\x88\x00\x00\x04\x83IDATh\x81\xed\x97]h\x1cU\x14\xc7\x7f\xe7n>6\
\xa8\xa9X)\x08m\xc14Tm\xd463ij\x1b\xdb\x8e\xf5\xc9"\xf8b\x90J)\xd8\xfa\xd5\
\x87>(-\n\x15\xa1"E\xacTQ\x0c(%\xda\xfa\xf1\xa2\xf8\x81H^\x14Vl\x1b\xeb\xee,\
!\xb0\xd5j\x97\xd2*V\xec\x07a\xa3\xe9f\xe3\xcc\xf1!\xbbq2\x99]6\xb0\n\x85\
\xf9=\xcd=s\xce\xff\xfe/3\xf7\x9e\x19\x88\x89\x89\x89\x89\x89\x89\x89\x89\
\xb9j\x91F\t\xd9\xb6\xbd\x0c8\x0ct\xa8\xea`6\x9b}\xaeQ\xda\xb50\x8d\x12R\xd5\
\x83@\x1fp\x93\x88\xec\xb5,k}\xa3\xb4k\xd1\xb0\x05\x88\xc8\x1d\xb3\x84\x8dY\
\xd1(\xedZ4l\x01@"8P\xd5FjW\xe5\x7f\x99\xe4\xbf\xe4\xaa_@ST\xb0\xb3\xb3\xb3u\
\xc1\x82\x05\x8f\x00\x1b\x80\xa5"rYU\x87\x80C\x1d\x1d\x1d~>\x9f\xdf""\x8b\
\x8c1\x1f\xa6\xd3\xe9\xdf\xab\x89\x977\xf2c"r\xb3\xaa\x8e\x8bHND\x0ee2\x99S\
\xb5L\xd9\xb6}\xa3\x88lW\xd5U\xc0\x12U\xbd,"gU\xf5\xe8\xe4\xe4\xe4g\xb9\\\
\xaeT\xc9\x9ds\x8c\xda\xb6\xbd\x06\xf8\x18X\x1c\xa1\xfd-p\x06\xd8V\x1e\x9fK&\
\x93\xb7\x1f;vl\xdc\xb6\xed\xb3\xc0\xd2@\xeei`Y\xc4\x1c\x9e\x88\x1c\xccd2\
\xcf\x00\x1a1\xffn\xe0\x05\xa0\xad\xca\xfa~jjj\xba\xf7\xc4\x89\x13\xbfB\xe8\
\x15\xea\xee\xee^\x0b|]\xc5<\xc0\xfa\x80y\x80\xa5\x13\x13\x13\xbdUr;#\xcc\
\x03$Tu\x8feY\x87\xc27,\xcb:\x08\x1c\xa8a\x1e`\xb9\xe7y\xcfV\x063\x0bp\x1c\'\
i\x8c\x19\x04\xae\xa9Q<\x07cLr>\xf9\x15Dd{OO\xcf\x03\x95qOO\xcff\x11y\xaa\
\x9eZU\xbd\xb6r=\xb3\x07\n\x85\xc26\x11\xb95\x94{\x9a\xe9\xeez\x05\xe8\x07\
\xd6\xcc\xd3\xe7\x9f\xc0\xdb@\x1ep\xca\x1aA#\xfb\x81\xcf\xcb\xd7\x07\xc2\xc5\
"\xf2\x89\xaa~\x054\x8b\xc8FU\xdd\x0c\x8c\xf9\xbe\xff\xea\x9c\x05\x88\xc8C\
\xa1\xfa3---k\x86\x87\x87/\x03tuu\xbd\x91L&\x87\x80Mu\x9a\xf7\x8c1\x9b\xd2\
\xe9t\xba<\x1e\xb0m{\x1f\xf0| g\xc5\xea\xd5\xabWy\x9e\x97\x00f5>U\xdd\xeb\
\xba\xee\xfe@\xe8u\xdb\xb6\x9b]\xd7\xf5\x00\xbf\x12\x0c\xee\x81u!\x03\xafT\
\xcc\x03\xe4r\xb9\x92\xef\xfb\xfb\xea4\x8f\x88|\x1e0\x0f@KK\xcbK@!\x18\xf3}\
\xff.\x11\t\xcf}\xa1\xbd\xbd\xfd\xe5\xb0\xa6\xeb\xbaSA\xf33\x0b\xe8\xed\xed]\
\x08\xccz\x97U5\x1b\x16(\x95Jsb\xd5\xf0}\xdf\r\xc7\x86\x87\x87\xaf\x00\'C\
\xf3,\x16\x91%\xa1\xd4\x91T*\xf5w=\xf3\x18\x00\xcf\xf3\xa2N\x8b\xa9:\xbdF""\
\x93u\xa66\xfb\xbe\x1f\xd9\x8f\xea\xc1\x00\xb8\xae{\x11(\x86\xeeY\xe1\xe4\
\xb6\xb6\xb6\x95\xf3\xd0\xb6\xc3\x01\xc7q\x92@\xf8\xa08/"\xbf\x85b+\xfb\xfb\
\xfb\x13\xd4Ap\x0f\xccz_E\xe4\xe9\xae\xae\xae\x99\xe3\xaa,8\x9fo\xfc\x07m\
\xdb\x9e\xf5\x85Z(\x14v\x01\xd7\x87\xf2\xbe3\xc6\x1c\x0f\xc5\x16\xe5\xf3\xf9\
\'\xc3\x82\x8e\xe34\x85<\xff\xdbhl\xdb\xde\t\x0c\x84jFU\xf5M@Ed\x0bpO\x84\
\xd1\xfb]\xd7\xfd2\xa2\x13\x03\xfc\x01\xbc\xa6\xaa\xbf\x88\xc8F`\x07\xb3\x9b\
\xdbi\xd7uoq\x1c\xc7\x8c\x8f\x8f\xff\xc0t\xf3\xab\xe0\x01\x03"r\xdc\xf7\xfdv\
\x11\xd9\x00\xdc\x07Lx\x9e\xb7idd\xe4g\x08\x1c\xa3SSSG\x9a\x9b\x9bw\x03\x1d\
\x01\x91;E\xe4\xad\x08\xd3\xf5\xb2\x08\xd8/\x12\xfd\xe3W\xee\x03~*\x95\xf2-\
\xcb\xda\'"\xef\x05n\'\x80]\xaa\xba+T\x7fC"\x91\xd8\x03<\x0e\x81\xc71::\xfa\
\x97\x88\xec\x00\xea\xdd|\x00\x18c*\xf9\xe3\xf3\xa9\x03>\xcaf\xb3\xefT\x06\
\xd9l\xf6}U\x1d\xac\xb3\xf6\xe2\xcc\xfc\xc1h&\x93I1\xfd\x98.EU\xa9j\x1ax7\
\x10:o\x8c\xf9\xbe|\xfdi ~\x81\xe9\x865\xe7c\xad\xac3X,\x16\xb7\x86\xe3\xd9l\
\xf6Q\xe0E\xa04\xb7j\xa6v\xa8\x9c\x03T\xf9\xa9\xef\xeb\xeb\xbb\xaeX,>\x01\
\xdc\r,\x01.\x89\xc8\xd0\xd8\xd8\xd8@kk\xab&\x93\xc9\x1d\xc0B\xe0\x88\xeb\
\xba\xe7\xcae\xc6\xb2\xac\x87Ed\xb9\x88|\x90\xc9dNuww\xaf\x15\x91\x9d\xc6\
\x98\xdb|\xdf/\x89\xc8I\xe0\xb0\xeb\xbaG\xab\x19\x04\xb0,\xab\xd3\x18\xb3UU\
\xd7\x95\xe79\x0f\xfch\x8c\xf9"\x9dN\x7fS\xab6&&&&&&&&\xe6*\xe2\x1f\xc2\xaa\
\x87\xf7\xcf\x0c\x08\xce\x00\x00\x00\x00IEND\xaeB`\x82\xf0WJ\xc7'
