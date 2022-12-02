from Utility.Utils import *
from Utility.Display import InitDisplay
from Handlers.Mixer.HandleMixer import MixerPadsInit
from Constants.System import *
from Constants.Colour import *
def HandleInit():
    print("INIT")
    SendCC(IDPatternUp, SingleColourOff)
    SendCC(IDPatternDown, SingleColourOff)
    SendCC(IDBankL, SingleColourOff)
    SendCC(IDBankR, SingleColourOff)
    SendCC(IDBrowser, SingleColourOff)
    ClearAllPads()
    ClearSelectButtons()
    MixerPadsInit()
    InitDisplay()