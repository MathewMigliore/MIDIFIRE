from Constants.Midi import *
from Constants.System import *
from Utility.Colours import SetPadColour

import device

def SendCC(ID, Val):
    if (not device.isAssigned()):
        return
    device.midiOutNewMsg(MIDI_CONTROLCHANGE + (ID << 8) + (Val << 16), ID)

def ClearAllPads():
    for pad in range(0,64):
        SetPadColour(pad, 0x000000, 0)

def ClearSelectButtons():
    for tab in TabControls:
        SendCC(tab, SingleColourHalfBright)
    for led in FullScreenLED:
        SendCC(led, SingleColourOff)




















    
