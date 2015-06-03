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
# Phatch recommends SPE (http://pythonide.stani.be) for editing python files.

# Embedded icon is taken from www.openclipart.org (public domain)

# Follows PEP8

from core import models
from lib.reverse_translation import _t

#---PIL


def init():
    global Image, ImageFilter, imtools
    from PIL import Image
    from PIL import ImageFilter
    from lib import imtools


def minimum(image, radius, amount=100):
    """Apply a filter
    - amount: 0-1"""
    image = imtools.convert_safe_mode(image)
    minimumed = image.filter(ImageFilter.MinFilter(radius))
    if amount < 100:
        return imtools.blend(image, minimumed, amount / 100.0)
    return minimumed

#---Phatch


class Action(models.Action):
    """"""

    label = _t('Minimum')
    author = 'Stani'
    email = 'spe.stani.be@gmail.com'
    init = staticmethod(init)
    pil = staticmethod(minimum)
    version = '0.1'
    tags = [_t('filter')]
    __doc__ = _t("Copies the minimum pixel value")

    def interface(self, fields):
        fields[_t('Radius')] = self.RankSizeField(self.RANK_SIZES[0])
        fields[_t('Amount')] = self.SliderField(100, 1, 100)

    icon = \
'x\xda\x01\x97\x08h\xf7\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x000\x00\
\x00\x000\x08\x06\x00\x00\x00W\x02\xf9\x87\x00\x00\x00\x04sBIT\x08\x08\x08\
\x08|\x08d\x88\x00\x00\x08NIDATh\x81\xed\x98ml[\xe5\x15\xc7\x7f\xe7\xde\xeb\
\xeb\xb7\xb8n\xda\xe0$n\x1aw!-\x1d 6\xc8B\x9a&\xb6\xb2\xacH\xdb\xd8\x04\x1a\
\x12l\xec\x85\xb1\x1766\x81\x06Lb\x1b\xe2\xc3\x06\xdb4m\xd3\xb4\xb1\x0f\xa8e\
c\x1a\xa8\xd2@\xe2\x0b\xf0\xa1\xa3\xd0@\xa2\x86\xa8M(UK\xb3\x92\x9a\xe08\xe9\
\x1b\x89k\xd2\xc4/\xd7\xbe\xcf>\xd8n\x03\xcb\x9b\x89\xdbj\x12\x7f\xe9\xca~|\
\xcf=\xe7\xfc}\x9e\xe7\xbc\\\xf8\x18\x97\x16\xfa\xc52\xd4\xdd\xdd}y]]]:\x1e\
\x8f\xe7*\xa9W\xab\xa4\xb2\xc5`\xdb\xb6\x18\x86\x11\xa9\xb4\xde\x8bI \xafiZ\
\xdb<\xb7V\x01\xd7\x01\xb7\x02\x8f\x025\xe5\xe85*\xe0\xdb\xb2\xa0\x94j\x02\
\xc6\x81\x87\x81\x8d\xc0Q@\x01g\x80\x11`\x10\xd8E\x81\xcc\x9e\xe5\xea\xbdh\
\x04Dd3\xf0\x06\xf0\x14p\x1b\xb0\x19x\x11\xd8[\x14\xd9\x0c\xb4\x02=\xe5\xe8\
\xbdh\x04\x80+M\xd3|\x1a\xc8R !\xc0\x1d\x1b7n\xfcM8\x1cN\xbb\xddn-\x91H<\xba\
s\xe7\xce\xb2\x0e\xf9\xc5"\xa0\x01\x97\xed\xde\xbd;Y\\\xfb4M{p\xdd\xbau\x0f\
\x84B!\x97\xa6i\xd4\xd7\xd7SUU\x15\x06|\xc0\x16\xa0o9\x8a/\x06\x01iiiY\x03$\
\x8a\xebO\x00/\xd9\xb6}\xf9\xd8\xd8\x18SSSLLL0>>\x8ei\x9aN\xe0&\xe0\xdf\x153\
\x1e\x0e\x87\xaf\xe9\xee\xee\x0e\xadD\xc7\xd6\xad[o\xe9\xec\xec\xfcZq\xfdg\n\
\x87\xf7\x03\x97\xdf\xefW\x8d\x8d\x8dq\n[\xab\x84\x1f/\xa5|\xb14*\x80\xa3\
\xb7\xb7\xf7\x88eYw\xb5\xb4\xb4x>\x9a\xff\x88\xae\xeb_\xb2,\xeb\x95\x86\x06\
\xdc.\x93\xf7\xe6\x13J&\x93\xc4b\xb1A\n\x84\x00\xc2@|)\xe5KUb\x1dp\xd4\xd7\
\xd7G\xddn\xf7?C\xa1Pmcc\xa3\'\x14\n\x9d\x8d\xc5b\xb3s\x05\xb7m\xdb\xe6\x0f\
\x06\x83\x9eM\x9b69\xa3\xd1h\xa6\xe4|GGG\x9b\xaeK\xc8m\x1d\xfc\xd4\x15\xa1\
\x86g>}U\xe3\x17\x9d\x92\x9e\x1c?\x9d\xf9\xf0\x1f\xa2\x80\x9d\xc0kE\xbbw\x03\
\x7f]\x8a\x80,\xe3\xbe\x0b\x90\xa6\xa6&G0\x18\xdc,"\xd7\x88\xc8UJ\xa9\x80\
\x88\x18J\xa9\x9c\x88L\x9f\xf3B\xa9M\xbd\xbd\xbd\x9f-\xfd\x01\x91H\xe49I\xbe\
\xfe\x9e\xcf\xe7\xff\x8e\xd3\xe5\xc6\xe9t\x03\xf0J\xff\x7fN\x9e\x98\xa2v\x8e\
\xad\xed\xc0\x18\x85b\xf6=\n\x87xx)\x02K\x1dbE!\xed\x99\xd1h4\x17\x8dF\x0f\
\x01\x07\x16{ \x12\x89\xfc\xadD\xbe\xb3\xb3\xf3\x07v\xe6\xcc.r\xd9\xbf\x9cI\
\x9cFDp:\xdd8L\'MAc\xdf\x89\xa9\\\x1bp\x19\x85zp\x0f\xf0\xb3\xe2:\xb0\x1c\
\xe7\x97C\x00 \x0f\xa4)\x9c\x17)~\xda\xf3\xc8Iccc\x95R*U\\\xeb"\xf2\x15{\xfa\
\xe0\x93"\x85\xad\xaa\x94"\x9d\x9e%\x9d\x9eE \x03\xb4\x00\xb5\x14\n\\\x9eBE\
\xfe\x13\xf0\xc3\xe58\xbf\\\x02P\x88D~\t\x19=\x10\x08\xac\x13\x91q\nDu\xc1Z\
\x83\xc8\xaf\xcf\x9f\xcbs\xc8\x8b\xcd\xe3\xc0q\n\x07\xb5$\xb0\x1b\x08\x02g\
\x97\xe9WE\xeb\x80\x18\x86\xe1WJ}.\x1c\x0e\x9b\xcc\x1c\xd1}D7\xd9\xabV{\xa7\
\xdfO\x9c\x13R\x8aQ\xa5\xf8\xf9\xde#\xbc\\\xfai\x8e\x8eS\xc0\x1f\xca1Z\xd6<P\
\xca4\xb1X,=\xcfm-\x1e\x8f\x9f\xd44\xed\xd9*g&\xe0\xd1\x12\x8f\x98\xa6\xd3\
\xedry\xb0\xed<9+\x0b0\xab\x14\xf7\xee=\xc23\xcc\x13\x96\x8f\x82\xa5\xb2\xd0\
9ttt\x04u]\xdfA!ST+\xa5l\x11y_)5\xac\xeb\xfa\x91T*ul`` \xde\xba\x99kM\xe1.\
\xd1\xb8\xe3\x1c3M\xcb+\xb3\xfe\xfd\xac\xd2o\x18\x18\x8a\xbd\xd1\xd1\xd1Qg\
\x18F\x9bRj\x93m\xdb\xdb\xfb\xfa\xfa\x12\x0b[\xae\x00\x81\xb6\xb6\xb6\x06\
\xd34w$\x93\xc9\x9f\x1c<x\xb0T\\\xd4\x9d_\xaei\x15q\xde\x9c\xb2<\xa1\xa9d\
\xbaav\xfa\xc4\xd5\xca\xb6\xdc\xffk\xc5|J\xf9[w\xe8\xba\xfe00\x05\x1cWJ\r\
\x00\xc7E\xe4>\xdb\xb6\x9f\xe8\xeb\xeb{\xe1B\x10\x90\xd6\xd6\xd6\x06\x97\xcb\
\xb5}zz\xfa\xde\x03\x07\x0e\xbcK!\xf4\xf2\xd0\xed\xee\xdf\xaf\xa9Y\x7f\x8f\
\xcb\xbbFle3\x9d\x9cd\xe8p\x8c\x13\x93\xd6\xdc\xe7\x95\xc2\xb1G\xfc\xd7\r\
\xf7\xed\x1d\xb8\xbf\xf8[)\x19(@\x9a\x9b\x9b\xf5\xfa\xfa\xfa\x07\x80\rJ\xa9\
\x07\xcb\x8d\xc6b\x04J\xce\xefH$\x12\xf7\x1d:t\xe8h\xd1\xb8\xfe\xd0\xedUw\
\xfb\xfck\x1fs\xbaW\x91\xcd\xcc\x92I%\xc9eS \xc2\xc9D\x9e\xa3\xb1\xb4=\x99T\
\xcd\xabC\x91\x172\x99\xcc\xcd\xa6i\xfe\xb2\xb7\xb7\xf7[s\x1c\x9f\x9b\x865@\
\xda\xdb\xdb?\xe9p8\x1e\x01\xf6\x88\x88\xad\x94\xf2\x8aHR)5)"c\xaf\xbe\xfaj\
\xff|N.\x94\x85\xb4\xf6\xf6\xf6\x1b\x0c\xc3\xb8\xaf\xe8\xfc\xdbE\xe7\xe5\x0b\
\xd7\xb2\xc6\xb7z\xed\xaf\xf2\xb9,g\x93\'\xc9\xe7\xb2\xd8v\x0e\xa5\x14\x9ah\
\x04k\\\xac\xf62\xf9\xbb\x7f\xa5&\xc2\x8djj`` \x16\x0e\x87\xf3\xc0B}\xbe\rh\
\xfd\xfd\xfdG\x9a\x9b\x9bo\xab\xab\xabk\x07&\x0c\xc3\x88\xf6\xf4\xf4,9\x1b|\
\x80\xc0\x86\r\x1b\\\xc1`\xf0F\x11\xb9"\x97\xcb\x9d\x98\x98\x98\xf8\xfe\xb1c\
\xc7&8\x1fv\xa3\xf5\x9a\xdaox\xbck\xab\xa7\x93\xc7\x01\x10\xd1\xd04\x1d%\x1a\
R\xbc\xdc.\xd7QH\xc1\xf9f\xac\xaa\xab\xab\xab\xa1\xa7\xa7g\xbe\xe6\xacTcdddD\
\x8d\x8c\x8c\xf4RF\x86\x9aK\xc01::\xea\x1c\x1d\x1d}\x89\xc2lj\x15\xafR\xb8\
\x05pT_\x16\xbc\xc9tWa\xcc\xba\xb0\xec\xd9\x82\xf3JPJ!"\x05\x12\x86qh\x8es\
\xa4\xd3\xe9\x07\xdcn\xf7\xe3\xdb\xb6m\xfb\xfa\x9c\xa1f!"ean;mSh\x19f\x81\
\x19\n\xa5\xfe\x03{\xd5\xef\xc7\xe9\xf3\xd7|\xc6\xe5\xf1\xe3\xf6T\xa3\xe9\
\x06\xa2i\x88\xa6\x17\xbf\xeb\x88\xa6\xa1\xeb\x9e\x97kkk\r\x11Q@~\xdf\xbe}\
\xe3\x96e\xfd4\x9b\xcdn_A[\xbe$\x81|\xd1\xe9\x1c\xf3\x87P\xbb\xf1:G\x93ou\
\xbd\xd7\xed\xad\xc6\xb3\xaa\x06\xef\xaa\x00\x0e\xa7\x07M\xd7\xcf]\xa6\xd3\
\x9b>\x99\xd0{\x9a\x9a\x9a\xbe\xaa\x94z\xbe\xa8/\xdf\xdf\xdf\xff\x8em\xdbO{\
\xbd\xde\xbb+I\xa0\x9cVBs\x18\xca\xe5\xf1\xadE\x10\x94\xb2\xd1t\x03\xd3\xe5\
\xc5\xca\xa4\nkM\'\x95:\xfb\xe2c\xcf\x0e\xcfD"\xc1\x9bfffn)>\x9b\x07\xc4\xb2\
\xac\t\xd34\xaf\xbeT\x04\x18?c\x1c\xb723\xaa:\xd0$\xa2i\x18\x0e\x17Y\xf7*rV\
\x1ae\xdbL\x9f9n\x8f\xc5\xdf\xfd\xc3\x96-[>o\xdb\xf6\xee\xc1\xc1\xc1RQ(\x8d\
\x8e\x15G9o\xe6\xd4\xee}\xe9\xc9\xa3o\xbe\xd2\x0b\n_u\x10\xff\x9au\xf8\xd76\
\xe0\xab\x0e23}z\xe6\xddw\xde\xba\xf3\xb1\xe7Ro:\x1c\x8eo&\x12\x89\xbf_\x08\
\x87?\x8cr"`\x01\x8e=\xaf\x8f}7\x99x\xe4\x17\xc1\xf5Wv{|5\xbaee\xe2\xe3\xb1\
\xb7\x9e\x7f\xe7\xd8\xf4\x93O\xf7\xceN^\x7f\xfd\xf5\x9dJ\xa9\x03\x87\x0f\x1f\
^vK\xbc\x12\x94C@\x01\xe9]C\x99\xf1]C\xdc\x0b\xfb\x85\xf3\xa9/W\xfct\x9a\xa6\
\xf9\xedT*u\xff<\xcf_\x90\xf7\xb0\xe5\xce\x03\xa5\xe9l.J{[\x074\x111\x06\x07\
\x07\'\xe7}8\x9f\xaf\xf8\xeb\xfc\x8f2\xd0,t\x18\x85\x02\tYD\xc6RJ]\xb0:\xb0R\
\x08\x8b7\x87\xf9\xfd\xfb\xf7\xbf-"Wwuu\x95\xf5\n}1T\x92\x80\x16\x08\x04\\\
\x14\x9b\xa0y`\x03\xf9\x99\x99\x99G\xf3\xf9\xfco+f\xb4R\x8a\x00\x02\x81@-pb\
\x81\xdb\n\xc8\x0e\r\r\r\x03\xa7#\x91Hw%lVt\x0b\x99\xa6Y\x03\x9c^D&\x0fX\xd1\
h\xf4\x8fJ\xa9\x1fQ\xc6H\xbb\x10*\x1a\x01\x87\xc3Q\xad\x94:\xb3\x84\x985>>>\
\x9b\xcb\xe5\x9e\x88D"\xb7\xae\xd4f%\t\xd8\xc9dr\x10X\xaa\xd7Q@\xb6\xbf\xbf\
\xff5\xa5\xd4\xe5\xac0\n\x95$\x90\x1f\x1e\x1e\x9e\xa28\xeb.%\x0bX\xa7N\x9d\
\xfaGWW\xd7\xba\x95\x18\xaddaQ\x80\x16\x0c\x06\xd5\xfa\xf5\xeb\xab\xe2\xf1\
\xf8B\x87\xb9\x04{rr25::\xba\xd0\x80sI\xa0\x01\xbe\xad[\xb7V$\xc3\\*\x94*\
\xf2\xc7\xf8\x18\xff\x0f\xf8/8U6=9\xde\x04\xab\x00\x00\x00\x00IEND\xaeB`\x82\
\xffd2D'
