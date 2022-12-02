import screen
from Constants.Midi import *
from Constants.Display import *
from Constants.System import *
def ClearDisplay():
    screen.fillRect(0, 0, DisplayWidth, DisplayHeight, 0x000000)
    screen.update()

def DisplayText(Font, Justification, PageTop, Text, CheckIfSame, DisplayTime = 0):
    try:
        screen.displayText(Font, Justification, PageTop, Text, CheckIfSame, DisplayTime)
        screen.update()
    except:
        return 
    
def DisplayBar3(p1, p2, Text, Value, Bipolar):    
    screen.displayBar(p1, p2, Text, Value, Bipolar)

def DisplayBar(Text, Value, Bipolar):
    screen.displayBar(0, TextRowHeight * TimedTextRow, Text, Value, Bipolar)

def barTest(p1, p2):
    DisplayBar3(p1, p2, "TEST", .75, False)

def DisplayBar2(Text, Value, ValueStr, Bipolar):
    screen.displayBar(0, TextRowHeight * ROWTOP, Text, Value, Bipolar)
    DisplayText(Font6x16 , JustifyCenter, ROWBOT, ValueStr, True)
    screen.update()

def DisplayTimedText(Text):
    screen.displayTimedText(Text, 2)
    screen.update()

def InitDisplay():
    screen.init(DisplayWidth, DisplayHeight, TextRowHeight, FireFontSize, 0xFFFFFF, 0)
    sysexHeader = int.from_bytes(bytes([MIDI_BEGINSYSEX, ManufacturerIDConst, DeviceIDBroadCastConst ,ProductIDConst, MsgIDSendPackedOLEDData]), byteorder='little')
    screen.setup(sysexHeader, ScreenActiveTimeout, ScreenAutoTimeout, TextScrollPause, TextScrollSpeed, TextDisplayTime)
    screen.fillRect(0, 0, DisplayWidth, DisplayHeight, 0)

def DeInitDisplay():
    DisplayTextTop(' ')
    DisplayTextMiddle(' ')
    DisplayTextBottom(' ')

# Helpers
def DisplayTextAll(textTop, textMid, textBot):
    DisplayTextTop(textTop)
    DisplayTextMiddle(textMid)
    DisplayTextBottom(textBot)
    screen.update

def DisplayTimedText2(Text1, Text2, Text3):
    DisplayTextCenter(Text1, ROWTOP)
    screen.displayTimedText(Text2, ROWMID)
    DisplayTextCenter(Text3, ROWBOT)
    screen.update()

def AddText(text):
    screen.addTextLine(text, 1)

def DisplayTextCenter(text, row):
    DisplayText(Font6x16 , JustifyCenter, row, text, True)

def DisplayTextTop(text):
    DisplayText(Font6x16 , JustifyLeft, ROWTOP, text, True)

def DisplayTextMiddle(text):
    DisplayText(Font6x16 , JustifyLeft, ROWMID, text, True)

def DisplayTextBottom(text):
    DisplayText(Font6x16 , JustifyLeft, ROWBOT, text, True)
