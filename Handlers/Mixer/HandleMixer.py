import mixer
import ui
from Constants.System import *
from Constants.Pad import *
from Constants.Colour import *
import device_MIDIFIRE
from Utility.Colours import *
from Utility.Display import *

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
def HandelMixer(event):
    ctrlID = event.data1
    evnt = event.data2
    
    mixerTrackNumber = mixer.trackNumber()
    volume = mixer.getTrackVolume(mixerTrackNumber)
    pan = mixer.getTrackPan(mixerTrackNumber)
    if (ctrlID == IDBrowser):
        print("test ", mixerTrackNumber)
        ui.getFocused(4)
        #Actions.open_mixer_plugin(mixerTrackNumber)
        event.handled = True
        
    # If select button is pressed down
    if (ctrlID == 25):
        if(not device_MIDIFIRE.FireState.selectWheelPressed):
            MixerState.mixerBeginSelection = mixerTrackNumber
            device_MIDIFIRE.FireState.selectWheelPressed = True
        else:
            MixerState.mixerBeginSelectionStored = MixerState.mixerBeginSelection
            MixerState.mixerEndSelection = mixerTrackNumber
            SelectMixer()
            device_MIDIFIRE.FireState.selectWheelPressed = False
        event.handled = True

    if (ctrlID == IDKnob1):
        print("IDKnob1", evnt)
        
        if (evnt == 127):
            volume-=.0005
        elif(evnt == 1):
            volume+=.0005
        elif (evnt > 1 and evnt < 5):
            volume+=.01
        elif (evnt < 127 and evnt > 6):
            volume-=.01
        mixer.setTrackVolume(mixerTrackNumber, volume)
        event.handled = True
    elif (ctrlID == IDKnob2):
        print("IDKnob2", evnt)
        if (evnt == 127):
            pan-=.005
        elif(evnt == 1):
            pan+=.005
        elif (evnt > 1 and evnt < 5):
            pan+=.05
        elif (evnt < 127 and evnt > 6):
            pan-=.05
        mixer.setTrackPan(mixerTrackNumber, pan)
        event.handled = True
    elif (ctrlID == IDKnob3): 
        print("IDKnob3", evnt)
        event.handled = True
    elif (ctrlID == IDKnob4):
        print("IDKnob4", evnt)
        event.handled = True
    
    # Scroll function held down
    if (device_MIDIFIRE.FireState.selectWheelPressed):

        if (ctrlID == IDJogWheel):
            
            if evnt == 1:
                ui.jog(1)
            elif evnt == 127:
                ui.jog(-1)

            padNum = mixer.trackNumber()
            mixer.selectTrack(padNum)
            if (padNum > 0 and padNum <= 32):
                if (padNum > 8):
                    tempNum = padNum - padNum%8
                    tempNum = tempNum/8
                    padNum = int(padNum%8 + 8*(tempNum))
            event.handled = True

    # Scroll function not held down
    else:
        # if (MixerState.mixerBeginSelection == 0):
        if (ctrlID == IDJogWheel):
            if evnt == 1:
                ui.jog(1)
            elif evnt == 127:
                ui.jog(-1)
            padNum = mixer.trackNumber()
            if (padNum > 0 and padNum <= 32):
                if (padNum > 8):
                    tempNum = padNum - padNum%8
                    tempNum = tempNum/8
                    padNum = int(padNum%8 + 8*(tempNum))
                    event.handled = True
                else:
                    event.handled = True
        
        if(IDPadFirst <= ctrlID <= IDPadLast):

            padNum = ctrlID - IDPadFirst

            if (padNum in padBankA):
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


            elif(padNum in padBankB):



                if (padNum == 8): # Button 1 - Solo track
                    if (not device_MIDIFIRE.FireState.preventDoubleClick):
                        mixer.soloTrack(mixerTrackNumber)
                        device_MIDIFIRE.FireState.preventDoubleClick = True
                        
                    else:
                        
                        device_MIDIFIRE.FireState.preventDoubleClick = False
                    
                    print(padNum)
                    
                elif (padNum == 9): # Button 2 - Hold to solo
                    mixer.soloTrack(mixerTrackNumber)
                    print(padNum)
                elif (padNum == 10): # Button 3 - Mute track
                    
                    if (not device_MIDIFIRE.FireState.preventDoubleClick):
                        mixer.muteTrack(mixerTrackNumber)
                        device_MIDIFIRE.FireState.preventDoubleClick = True
                    else:
                        device_MIDIFIRE.FireState.preventDoubleClick = False
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
            elif(padNum in padBankC):
                event.handled = True    
        # else:

        #     if (ctrlID == IDJogWheel):
        #         if evnt == 1:
        #             ui.jog(1)
        #         elif evnt == 127:
        #             ui.jog(-1)
        #         padNum = mixer.trackNumber()
        #         if (padNum > 0 and padNum <= 32):
                    
        #             if (padNum in padBankA):
        #                 #SetPadColour(MixerState.mixerTrackLastUsed, cGreen, 0)
        #                 if (padNum > 8):
        #                     tempNum = padNum - padNum%8
        #                     tempNum = tempNum/8
        #                     padNum = int(padNum%8 + 8*(tempNum))
        #                     #MixerState.mixerTrackLastUsed = padBankA[padNum-1]
        #                     #SetPadColour(padBankA[padNum-1], cGreen, 1)
        #                     event.handled = True
        #                 else:
        #                     #MixerState.mixerTrackLastUsed = padBankA[padNum-1]
        #                     #SetPadColour(padBankA[padNum-1], cGreen, 1)
        #                     event.handled = True
                        
        #             else:
        #                 #SetPadColour(MixerState.mixerTrackLastUsed, cBlack, 0)
        #                 if (padNum > 8):
        #                     tempNum = padNum - padNum%8
        #                     tempNum = tempNum/8
        #                     padNum = int(padNum%8 + 8*(tempNum))
        #                     #MixerState.mixerTrackLastUsed = padBankA[padNum-1]
        #                     #SetPadColour(padBankA[padNum-1], cGreen, Dimming)
        #                     event.handled = True
        #                 else:
        #                     #MixerState.mixerTrackLastUsed = padBankA[padNum-1]
        #                     #SetPadColour(padBankA[padNum-1], cGreen, Dimming)
        #                     event.handled = True
                    
        #         #else:
        #             #SetPadColour(MixerState.mixerTrackLastUsed, cGreen, 0)
        #         SelectMixer()
                
            # # Selecting tracks by pressing buttons  
            # if(IDPadFirst <= ctrlID <= IDPadLast):
                
            #     padNum = ctrlID - IDPadFirst
            #     SetPadColour(MixerState.mixerTrackLastUsed, cBlack, 0)
            #     if (padNum in padBankA):
            #         #print(padNum)
            #         padNum+=1
            #         if (padNum > 8):
            #         #     if (8%(padNum%16) != 8):
                        
            #             MixerState.mixerTrackLastUsed = padNum - 1
            #             SetPadColour(padNum - 1, cGreen, Dimming)
            #             padNum = padNum - 16%padNum
            #             padNum = padNum - ((padNum - padNum%16)/2)
            #             padNum = int(padNum + 8)
            #             mixer.setTrackNumber(padNum)
            #             event.handled = True
            #         else:
                        
            #             MixerState.mixerTrackLastUsed = padNum - 1
            #             mixer.setTrackNumber(padNum)
            #             SetPadColour(padNum - 1, cGreen, Dimming)
            #             event.handled = True           

                
    mixerTrackNumber = mixer.trackNumber()
    volume = mixer.getTrackVolume(mixerTrackNumber)
    

    trackName = str(mixerTrackNumber) + ". " + str(mixer.getTrackName(mixerTrackNumber))
    trackVol = "Vol: " + str('%.1f'%(volume*100)) + "%"

    #trackChange = "Pan: " + str('%.1f'%(mixer.getTrackPan(mixerTrackNumber)))
    #trackSW = " SW: " + str('%.1f'%(mixer.getTrackStereoSep(mixerTrackNumber)))
    print(mixer.getTrackInfo(mixerTrackNumber))
    #DisplayTextAll(trackName, trackVol, trackChange)


def MixerPadsInit():
    for pad in padBankA:
        SetPadColour(pad, cBlack, Dimming)
    for pad in padBankB:
        SetPadColour(pad, cWhite, 2)
    for pad in padBankC:
        SetPadColour(pad, cWhite, Dimming)

def SelectMixer():
    i = MixerState.mixerBeginSelectionStored
    while (i <= MixerState.mixerEndSelection):
        mixer.selectTrack(i)
        i+=1

def HandleMixerRefresh(flags):
    
    padNum = mixer.trackNumber() - 1
    if (padNum >= 0 and padNum < 32 and flags != 4):
        MixerPadsInit()
        if (flags == MixerSelectSingle):
            
            SetPadColour(MixerState.mixerTrackLastUsed, cBlack, 0)  
            if (padNum > 8):
                tempNum = padNum - padNum%8
                tempNum = tempNum/8
                padNum = int(padNum%8 + 8*(tempNum))
                MixerState.mixerTrackLastUsed = padBankA[padNum]
                SetPadColour(padBankA[padNum], cGreen, Dimming)
            else:
                MixerState.mixerTrackLastUsed = padBankA[padNum]
                SetPadColour(padBankA[padNum], cGreen, Dimming)
            mixerTrackNumber = mixer.trackNumber()
            volume = mixer.getTrackVolume(mixerTrackNumber)
            trackName = str(mixerTrackNumber) + ". " + str(mixer.getTrackName(mixerTrackNumber))
            trackVol = "Vol: " + str('%.1f'%(volume*100)) + "%"
            trackChange = ""
            DisplayTextAll(trackName, trackVol, trackChange)
            MixerState.mixerBeginSelection = mixerTrackNumber

        elif (flags == MixerSelectRange):
            mixerSel = MixerState.mixerBeginSelection
            while mixer.isTrackSelected(mixerSel):
                mixerSel+=1
                padNum = mixerSel - 2
                if (padNum > 8):
                    tempNum = padNum - padNum%8
                    tempNum = tempNum/8
                    padNum = int(padNum%8 + 8*(tempNum))
                    #MixerState.mixerTrackLastUsed = padBankA[padNum]
                    SetPadColour(padBankA[padNum], cGreen, Dimming)
                else:
                    #MixerState.mixerTrackLastUsed = padBankA[padNum]
                    SetPadColour(padBankA[padNum], cGreen, Dimming)
            volume = mixer.getTrackVolume(mixerSel)
            trackName = str(mixerSel) + ". " + str(mixer.getTrackName(mixerSel))
            trackVol = "Vol: " + str('%.1f'%(volume*100)) + "%"
            trackChange = "Select " + str(MixerState.mixerBeginSelection) + " - " + str(mixerSel - 1)
            DisplayTextAll(trackName, trackVol, trackChange)
            
            
    else:
        if(padNum < 0):
            SetPadColour(padBankA[padNum+1], cBlack, Dimming)
            mixerTrackNumber = mixer.trackNumber()
            volume = mixer.getTrackVolume(mixerTrackNumber)
            trackName = str(mixerTrackNumber) + ". " + str(mixer.getTrackName(mixerTrackNumber))
            trackVol = "Vol: " + str('%.1f'%(volume*100)) + "%"
            trackChange = ""
            DisplayTextAll(trackName, trackVol, trackChange)
        elif(padNum >= 32):      
            SetPadColour(padBankA[31], cBlack, Dimming)
            mixerTrackNumber = mixer.trackNumber()
            volume = mixer.getTrackVolume(mixerTrackNumber)
            trackName = str(mixerTrackNumber) + ". " + str(mixer.getTrackName(mixerTrackNumber))
            trackVol = "Vol: " + str('%.1f'%(volume*100)) + "%"
            trackChange = ""
            DisplayTextAll(trackName, trackVol, trackChange)
    

    if (flags == 4):
        mixerTrackNumber = mixer.trackNumber()
        #SetPadColour(padBankA[mixerTrackNumber - 1], cGreen, Dimming)
        volume = mixer.getTrackVolume(mixerTrackNumber)
        trackName = str(mixerTrackNumber) + ". " + str(mixer.getTrackName(mixerTrackNumber))
        trackVol = "Vol: " + str('%.1f'%(volume*100)) + "%"
        trackChange = ""
        DisplayTextAll(trackName, trackVol, trackChange)