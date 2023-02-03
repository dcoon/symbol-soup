from enum import Enum
from typing import (
        TypeAlias,
        List
        )

class ConnectionPointType(Enum):
    INPUT = 1
    OUTPUT = 2

class ConnectionPointStyle(Enum):
    TODO = 1

class Orientation(Enum):
    """
    Rotation of a drawable in degrees. Default rotation is N(orth) or 0 degrees.
    """
    N = 0
    E = 90
    S = 180
    W = 270

Coordinates: TypeAlias = tuple[int, int]

Coordinates.XO, Coordinates.YO = 0
Coordinates.ORIGIN = (Coordinates.XO, Coordinates.YO)
"""
Origin of a 2D space (x=0, y=0)
"""

Ratio: TypeAlias = float
"""
Ratio representing a scaling factor. Must be 0 < ratio < very large
"""
Ratio.HALF = 0.5
Ratio.ONE = 1
Ratio.DOUBLE = 2

class Position:
    """
    Position in 2D space. Positions are relative to a local origin. The actual position
    drawn may be transformed (coordinates, orientation, scale) by a drawing tool.
    """
    xy: Coordinates = Coordinates.ORIGIN

class Drawable():
    """
    Something that can be drawn on a diagram. Holds metadata for a drawing tool to 
    use to position and scale the element.
    """
    position: Position
    orientation: Orientation = Orientation.N
    scale: Ratio = Ratio.ONE

class ConnectionPoint(Drawable):
    """
    Describes a logical place|slot where a connection can be made to a symbol. 
    """
    name: str
    aliases: List[str]
    type: ConnectionPointType # electrical type of the pin
    style: ConnectionPointStyle
    length: int


URL: TypeAlias = str

class Icon(Drawable):
    def __init__(self, url: URL) -> None:
        self.url = url
        super().__init__()
    """
    Graphic icon for a symbol. Most likely loaded from an SVG file.
    """
    url: URL
    

class Symbol(Drawable):
    """
    Graphic representation of a part designed to used in 2D diagrams. Has an icon
    representating the part and connection points that indicate where connections should be 
    made.

    Symbols do not know how to draw themselves. They only hold metadata that an external tool
    uses to draw the symbol. 
    """
    name: str
    ref: str = "R?"
    value: str
    points: List[ConnectionPoint]
    icon: Icon
    courtyard: Icon
    # library metadata: documentation, category, tags, author, generatedBy

class CompoundSymbol(Symbol):
    """
    Symbol consisting of 2 or more sub symbols. 
    """
    units: List[Symbol]
    

class SymbolLibrary():
    """
    Group of symbols organized by metadata (category, tags, author, manufacturer, etc)
    """
    pass

# Exaple usage
# alt = Symbol()
# alt.pins += ConnectionPoint("positive", ConnectionPointType.OUTPUT)
# alt.pins += ConnectionPoint("lamp")
# # alt.category = "Electrical"
# # alt.tags
# alt.icon = Icon("url")
# tool.export(alt)


