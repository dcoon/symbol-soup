
# Pin=Connector=Connection Point

alt = Part("Alternator", Symbol.ALTERNATOR, Footprint.BALMAR_SERIES_60_150)
alt.connectors.positive = Connector()
with alt.connections.positive:
    type = "M10Stud"
    position = NSEW/Coordinates, Rotation
    pin[1] = Pin(type, gender, position, orientation)

    

startBusbar = Part("Busbar")
houseBusbar = Part("Busbar")
negativeBusbar = Part("Busbar")

alt.positive = startBusbar[1]
alt.negative = negativeBusbar[1]
alt.lamp = regulator.lamp
alt.tach = 
engine.on = relay.enable
engine.negative = negativeBusbar[2]



