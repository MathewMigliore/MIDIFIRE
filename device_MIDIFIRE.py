#name=MIDIFIRE

from Handlers.ScriptEvents.HandleMidiIn import handle_midi_in
from Handlers.ScriptEvents.HandleDeInit import handle_deinit
from Handlers.ScriptEvents.HandleInit import handle_init
from Handlers.ScriptEvents.HandleProjectLoad import HandleProjectLoad
from Handlers.ScriptEvents.HandleRefresh import handle_refresh


def OnMidiIn(event):
    handle_midi_in(event)

def OnRefresh(flags):
    handle_refresh(flags)

def OnInit():
    handle_init()

def OnDeInit():
    handle_deinit()