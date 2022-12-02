from device_MIDIFIRE import FireState
from Handlers.Mixer.HandleMixer import HandelMixer, MixerPadsInit
from Handlers.Channelrack.HandleChannelrack import HandelChannelrack, ChannelrackPadsInit
from Handlers.Painoroll.HandlePainoroll import HandelPianoroll, PianorollPadsInit
from Handlers.Playlist.HandlePlaylist import HandelPlaylist, PlaylistPadsInit
from Utility.Utils import SendCC
from Constants.Pad import *
from Constants.System import *
import ui 


def HandleMidiIn(event):
    event.handled = False
    ctrlID = event.data1
    # Choosing windows
    if (ctrlID in TabControls):
        if (not FireState.preventDoubleClick):
            FireState.preventDoubleClick = True
            if (ui.getFocused(TabControls.index(ctrlID)) == 0):
                ui.showWindow(TabControls.index(ctrlID))
                SendCC(ctrlID, SingleColourFull)
                FireState.currentTab = ctrlID
            elif(ctrlID != IDChannelRack):
                ui.enter()
            if (ctrlID != FireState.previousSelected):
                SendCC(FireState.previousSelected, SingleColourHalfBright)
                FireState.previousSelected = ctrlID
        else:
            FireState.preventDoubleClick = False
        event.handled = True
    
    if (FireState.currentTab == IDMixer):
        MixerPadsInit()
        HandelMixer(event)
    elif (FireState.currentTab == IDChannelRack):
        ChannelrackPadsInit()
        HandelChannelrack(event)
    elif (FireState.currentTab == IDPlaylist):
        PlaylistPadsInit()
        HandelPlaylist(event)
    elif (FireState.currentTab == IDPianoRoll):
        PianorollPadsInit()
        HandelPianoroll(event)

