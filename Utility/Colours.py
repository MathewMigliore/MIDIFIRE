from Utility.Device import SendMessageToDevice
from Constants.Colour import *
from Constants.System import *

class ColourMap:
    def __init__(self, padIndex, color, dimFactor):
        self.PadIndex = padIndex
        self.PadColor = color
        self.DimFactor = dimFactor
        self.R = 0
        self.G = 0
        self.B = 0
        self.Anim = ''
        self.AnimStep = -1  

_ColourMap = list()
for p in range(64):
    ColourMapTemp = ColourMap(p, 0, 0)
    _ColourMap.append(ColourMapTemp)

def getPadColour(padIdx):
    return _ColourMap[padIdx].PadColour

def TestColourMap():
    global _ColourMap

    for r in range(0, 127, 16):
        for g in range(0, 127, 16):
            for b in range(0, 127, 16):
                for cMap in _ColourMap:
                    cMap.R = r
                    cMap.G = g
                    cMap.B = b 
                FlushColourMap()  
                
def SetPadColourBuffer(idx, col, dimFactor, flushBuffer = False):
    global _ColourMap
    
    if(col == -1):
        col = _ColourMap[idx].PadColour

    #print('SetLEDCol', idx, col)
    r = (col & 0x7F0000) >> 16
    g = (col & 0x007F00) >> 8
    b = (col & 0x7F)

    # reduce brightness by half time dimFactor
    if(dimFactor > 0):
        for i in range(dimFactor):
            r = r >> 1
            g = g >> 1
            b = b >> 1

    _ColourMap[idx].PadColour = col 
    _ColourMap[idx].DimFactor = dimFactor
    _ColourMap[idx].R = r
    _ColourMap[idx].G = g
    _ColourMap[idx].B = b
    
    if(flushBuffer):
        FlushColourMap()

def FlushColourMap():
    dataOut = bytearray(4 * 64)
    bufOffs = 0
    for cMap in _ColourMap:
        dataOut[bufOffs] = cMap.PadIndex
        dataOut[bufOffs + 1] = cMap.R
        dataOut[bufOffs + 2] = cMap.G
        dataOut[bufOffs + 3] = cMap.B
        bufOffs += 4
    SendMessageToDevice(MsgIDSetRGBPadLedState, len(dataOut), dataOut)

def getColourMap():
    return _ColourMap

def SetPadColour(idx, col, dimFactor, bSaveColour = True):
    global _ColourMap
    SetPadColourDirect(idx, col, dimFactor, bSaveColour)

def SetPadColourDirect(idx, col, dimFactor, bSaveColour = True):
    global _ColourMap
    global _PadMap 

    if(col == -1):
        col = _ColourMap[idx].PadColour
        dimFactor = _ColourMap[idx].DimFactor

    r = (col & 0x7F0000) >> 16
    g = (col & 0x007F00) >> 8
    b = (col & 0x7F)

    if(dimFactor > 0):
        for i in range(dimFactor):
            r = r >> 1
            g = g >> 1
            b = b >> 1

    SetPadRGB(idx, r, g, b)

    if(bSaveColour):
        _ColourMap[idx].PadColour = col 
        _ColourMap[idx].DimFactor = dimFactor

def ColourToRGB(Colour):
    return (Colour >> 16) & 0xFF, (Colour >> 8) & 0xFF, Colour & 0xFF

def RGBToColour(R,G,B):
    return (R << 16) | (G << 8) | B

def SetPadRGB(idx, r, g, b):  
    dataOut = bytearray(4)
    i = 0
    dataOut[i] = idx
    dataOut[i + 1] = r
    dataOut[i + 2] = g
    dataOut[i + 3] = b

    SendMessageToDevice(MsgIDSetRGBPadLedState, len(dataOut), dataOut)

