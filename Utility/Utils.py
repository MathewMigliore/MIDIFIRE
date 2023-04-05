from Constants.Midi import *
from Constants.System import *
from Utility.Colours import SetPadColour

import device

def send_cc(ID, Val):
    if (not device.isAssigned()):
        return
    device.midiOutNewMsg(MIDI_CONTROLCHANGE + (ID << 8) + (Val << 16), ID)

def clear_all_pads():
    for pad in range(0,64):
        SetPadColour(pad, 0x000000, 0)

def clear_select_buttons():
    for tab in TabControls:
        send_cc(tab, SingleColourHalfBright)
    for led in FullScreenLED:
        send_cc(led, SingleColourOff)




















    
