_author_ = 'mariag'

import unittest
import re

class InvalidImageExt(Exception):
    def __init__(self, msg):
        super(InvalidImageExt, self).__init__(msg)

class ImageFile(object):
    _supported = ["jpeg","gif","bmp","png"]
    
    def __init__(self, file):
        res = re.search("(^[\w]+)\.([\w]+)$",file)
        formatIm = res.group(2)
        if formatIm not in ImageFile._supported:
            raise InvalidImageExt("Image format {} is not supported".format(formatIm))

class TestImageFile(unittest.TestCase):
    def test_good_ext(self):
        try:
            img = ImageFile("file.png")
        except InvalidImageExt:
            self.fail("png should be a valid file extension")

    def test_bad_ext(self):
        with self.assertRaises(InvalidImageExt):
            img = ImageFile("file.mp3")

unittest.main()