#name=MIDIFIRE

from Handlers.ScriptEvents.HandleMidiIn import *
from Handlers.ScriptEvents.HandleDeInit import *
from Handlers.ScriptEvents.HandleInit import *
from Handlers.ScriptEvents.HandleProjectLoad import *
from Handlers.ScriptEvents.HandleRefresh import *

# import midi
# import channels
# import patterns
# import utils
# import time
# import ui 
# import transport 
# import mixer 
# import general
# import playlist
# import arrangement
# import device


Dimming = 0
trackChange = ""
trackName = ""
trackVol = ""

class FireState(object):
    isSelectedTab = list()

    isMixerSelected = False
    isPlaylistSelected = False
    isChannelRackSelected = False
    isPianorollSelected = False

    currentTab = IDMixer

    isMaximized = False
    preventDoubleClick = False
    previousSelected = 100
    selectWheelPressed = False
    def __init__(self, previousSelected, isMaximized, preventDoubleClick, selectWheelPressed, isSelectedTab):
        self.selectWheelPressed = selectWheelPressed
        self.preventDoubleClick = preventDoubleClick
        self.isMaximized = isMaximized
        self.previousSelected = previousSelected
        self.isSelectedTab = isSelectedTab


def OnMidiIn(event):
    HandleMidiIn(event)

def OnRefresh(flags):
    HandleRefresh(flags)

def OnInit():
    HandleInit()

def OnDeInit():
    HandleDeInit()