from Classes.FireState import FireState
from Handlers.Mixer.HandleMixer import handle_mixer, mixer_pads_init
from Handlers.Channelrack.HandleChannelrack import handle_channel_rack, channel_rack_pads_init
from Handlers.Painoroll.HandlePainoroll import handle_piano_roll, piano_roll_pads_init
from Handlers.Playlist.HandlePlaylist import handle_playlist, playlist_pads_init
from Utility.Utils import send_cc
from Constants.Pad import *
from Constants.System import *
import ui 


def handle_midi_in(event):
    event.handled = False
    ctrl_id = event.data1
    print(ctrl_id)
    handle_tab_controls(event, ctrl_id)
    if FireState.current_tab == IDMixer:
        handle_mixer(event)
    elif FireState.current_tab == IDChannelRack:
        handle_channel_rack(event)
    elif FireState.current_tab == IDPlaylist:
        handle_playlist(event)
    elif FireState.current_tab == IDPianoRoll:
        handle_piano_roll(event)


def handle_tab_controls(event, ctrl_id):
    if ctrl_id in TabControls:
        if event.data2 == 127:
            handle_tab_switch(event, ctrl_id)
        elif value == 0:
            print()
        event.handled = True


def handle_tab_switch(event, ctrl_id):
    if ui.getFocused(TabControls.index(ctrl_id)) == 0:
        ui.showWindow(TabControls.index(ctrl_id))
        send_cc(ctrl_id, SingleColourFull)
        FireState.current_tab = ctrl_id
    elif ctrl_id != IDChannelRack:
        ui.enter()

    if ctrl_id != FireState.previous_selected:
        send_cc(FireState.previous_selected, SingleColourHalfBright)
        FireState.previous_selected = ctrl_id
