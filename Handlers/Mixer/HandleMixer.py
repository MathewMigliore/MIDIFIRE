import mixer
import ui
from Constants.System import *
from Constants.Pad import *
from Constants.Colour import *
from Classes.FireState import FireState
from Utility.Colours import *
from Utility.Display import *
from Handlers.Mixer.HandleMixerKnobs import handle_mixer_knobs

class MixerState(object):
    mixerTrackLastUsed = 0
    mixerBeginSelection = 0
    mixerBeginSelectionStored = 0
    mixerEndSelection = 0

    def __init__(self, mixerBeginSelectionStored, mixerTrackLastUsed, mixerBeginSelection , mixerEndSelection):
        self.mixerTrackLastUsed = mixerTrackLastUsed
        self.mixerBeginSelection = mixerBeginSelection
        self.mixerEndSelection = mixerEndSelection
        self.mixerBeginSelectionStored = mixerBeginSelectionStored



Dimming = 0
def handle_mixer(event):
    ctrlID = event.data1
    evnt = event.data2
    
    mixerTrackNumber = mixer.trackNumber()

    if (ctrlID == IDBrowser):
        ui.getFocused(4)
        event.handled = True
    if (ctrlID == IDJogWheelDown):
        handle_jog_wheel_down(event, mixerTrackNumber)
        
    if ctrlID in KnobCtrls:
        handle_mixer_knobs(event)
    if (FireState.selectWheelPressed):
        handle_jog_wheel_scroll_pressed(event, ctrlID, evnt)
    else:
        handle_jog_wheel_scroll_not_pressed(event, ctrlID, evnt, mixerTrackNumber)    


def handle_jog_wheel_scroll_pressed(event, ctrlID, evnt):
    if (ctrlID == IDJogWheel):
        if evnt == 1:
            ui.jog(1)
        elif evnt == 127:
            ui.jog(-1)

        padNum = mixer.trackNumber()
        mixer.selectTrack(padNum)
        if (padNum > 0 and padNum <= 32):
            #calculate_position_on_pads(padNum)
            event.handled = True

def calculate_position_on_pads(padNum):
    if (padNum > 8):
        tempNum = padNum - padNum%8
        tempNum = tempNum/8
        padNum = int(padNum%8 + 8*(tempNum))
        
        #MixerState.mixerTrackLastUsed = padBankA[padNum]
    SetPadColour(padBankA[padNum], cGreen, Dimming)
    return padNum

def handle_jog_wheel_scroll_not_pressed(event, ctrlID, evnt, mixerTrackNumber):
    if (ctrlID == IDJogWheel):
        if evnt == 1:
            ui.jog(1)
        elif evnt == 127:
            ui.jog(-1)
        padNum = mixer.trackNumber()
        if (padNum > 0 and padNum <= 32):
            #calculate_position_on_pads(padNum)
            event.handled = True

        
    if(IDPadFirst <= ctrlID <= IDPadLast):
        padNum = ctrlID - IDPadFirst

        if (padNum in padBankA):
            padNum = handle_bank_a(event, padNum)


        elif(padNum in padBankB):
            handle_bank_b(event, mixerTrackNumber, padNum)
        elif(padNum in padBankC):
            event.handled = True

def handle_bank_a(event, padNum):
    padNum+=1
    if (padNum > 8):
        padNum = padNum - 16%padNum
        padNum = padNum - ((padNum - padNum%16)/2)
        padNum = int(padNum + 8)
        mixer.setTrackNumber(padNum)
        event.handled = True
    else:
        mixer.setTrackNumber(padNum)
        event.handled = True
    return padNum

def handle_bank_b(event, mixerTrackNumber, padNum):
    if (padNum == 8): # Button 1 - Solo track
        if event.data2 == 127:
            mixer.soloTrack(mixerTrackNumber)
                    
    elif (padNum == 9): # Button 2 - Hold to solo
        mixer.soloTrack(mixerTrackNumber)
        print(padNum)
    elif (padNum == 10): # Button 3 - Mute track
        if (event.data2 == 0):
            mixer.muteTrack(mixerTrackNumber)
        print(padNum)
    elif (padNum == 11): # Button 4 - Hold to mute
        mixer.muteTrack(mixerTrackNumber)
        print(padNum)
    elif (padNum == 24): # Button 5
        print(padNum)
    elif (padNum == 25): # Button 6
        print(padNum)
    elif (padNum == 26): # Button 7
        print(padNum)
    elif (padNum == 27): # Button 8
        print(padNum)
    elif (padNum == 40): # Button 9
        print(padNum)
    elif (padNum == 41): # Button 10
        print(padNum)
    elif (padNum == 42): # Button 11
        print(padNum)
    elif (padNum == 43): # Button 12
        print(padNum)
    elif (padNum == 56): # Button 13
        print(padNum)
    elif (padNum == 57): # Button 14
        print(padNum)
    elif (padNum == 58): # Button 15
        print(padNum)
    elif (padNum == 59): # Button 16
        print(padNum)
                
    event.handled = True

def handle_jog_wheel_down(event, mixerTrackNumber):
    print("IDJogWheelDown")

    if(event.data2 == 127):
        MixerState.mixerBeginSelection = mixerTrackNumber
    elif(event.data2 == 0):
        MixerState.mixerBeginSelectionStored = MixerState.mixerBeginSelection
        MixerState.mixerEndSelection = mixerTrackNumber
        select_mixer()


    event.handled = True


def mixer_pads_init():
    for pad in padBankA:
        SetPadColour(pad, cBlack, Dimming)
    for pad in padBankB:
        SetPadColour(pad, cWhite, 2)
    for pad in padBankC:
        SetPadColour(pad, cWhite, Dimming)

def select_mixer():
    i = MixerState.mixerBeginSelectionStored
    while (i < MixerState.mixerEndSelection):
        mixer.selectTrack(i)
        SetPadColour(padBankA[calculate_position_on_pads(i-1)], cGreen, Dimming)
        i+=1
        

def handle_mixer_refresh(flags):
    print(flags)
    pad_num = mixer.trackNumber() - 1
    if (flags != 4):
        if (pad_num >= 0 and pad_num < 32):
            if (flags == MixerSelectSingle):
                
                SetPadColour(MixerState.mixerTrackLastUsed, cBlack, 0)  
                pad_num = calculate_position_on_pads(pad_num)
                MixerState.mixerTrackLastUsed = padBankA[pad_num]
                
                display_info()

            elif (flags == MixerSelectRange):
                
                calculate_position_on_pads(pad_num)
                display_info()
                
                
        else:
            if(pad_num < 0):
                SetPadColour(padBankA[pad_num+1], cBlack, Dimming)
            elif(pad_num >= 32):      
                SetPadColour(padBankA[31], cBlack, Dimming)
            display_info()
        

    else:
        #SetPadColour(padBankA[mixerTrackNumber - 1], cGreen, Dimming)
        display_info()

def display_info():
    mixerTrackNumber = mixer.trackNumber()
    volume = mixer.getTrackVolume(mixerTrackNumber)
    trackName = str(mixerTrackNumber) + ". " + str(mixer.getTrackName(mixerTrackNumber))
    trackVol = "Vol: " + str('%.1f'%(volume*100)) + "%"
    trackChange = ""
    DisplayTextAll(trackName, trackVol, trackChange)