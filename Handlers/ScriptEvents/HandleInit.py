from Utility.Utils import *
from Utility.Display import init_display
from Handlers.Mixer.HandleMixer import mixer_pads_init
from Constants.System import *
from Constants.Colour import *
def handle_init():
    print("INIT")
    send_cc(IDPatternUp, SingleColourOff)
    send_cc(IDPatternDown, SingleColourOff)
    send_cc(IDBankL, SingleColourOff)
    send_cc(IDBankR, SingleColourOff)
    send_cc(IDBrowser, SingleColourOff)
    clear_all_pads()
    clear_select_buttons()
    mixer_pads_init()
    init_display()