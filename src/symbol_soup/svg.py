from multimethod import (
        multimethod
        )

import os

from ..symbol import (
        Drawable,
        Icon,
        Symbol
        )
from svgutils.compose import (
        SVG,
        Figure
        )

class SvgTool():
    """
    Convert one or more Drawables to SVG
    """
    @multimethod
    def svg(self, obj: Drawable):
        pass


    @classmethod
    def readFile(path: str) -> str:
        with open(path, 'r') as f:
            return f.read()

    @multimethod
    def svg(self, obj: Icon):
        # pic = SVG.readFile(obj.url)
        s = SVG(obj.url)
        print(s.tostr())

# load URL
#     import requests
#
# URL = "https://td-cdn.pw/api.php?download=tikdown.org-42500282235.mp4"
# FILE_TO_SAVE_AS = "myvideo.mp4" # the name you want to save file as
#
#
# resp = requests.get(URL) # making requests to server
#
# with open(FILE_TO_SAVE_AS, "wb") as f: # opening a file handler to create new file 
#     f.write(resp.content) # writing content to file

    @multimethod
    def svg(self, obj: Symbol):
        """
        Calculate bounding box of connectionPoints
        Draw scaled Icon
        Draw pins
        """
        self.svg(obj.icon)
        

# print(SVG().svg(alt))

# symbol library import yaml|json|toml|kicad|visio|drawio
# part library...the same

icon = Icon("standards/noun-chip-5475232.svg")
tool = SvgTool()
tool.svg(icon)
