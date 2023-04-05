from Constants.System import *
from Classes.FireState import Knob
import mixer




def handle_mixer_knobs(event):
    
    ctrlID = event.data1
    evnt = event.data2
    mixerTrackNumber = mixer.trackNumber()

    if (ctrlID == IDKnob1):
        volume = mixer.getTrackVolume(mixerTrackNumber)
        print("IDKnob1", evnt)
        v = volume
        if (evnt == 127):
            if (not Knob.onTouch):
                Knob.onTouch = True
            else:
                volume-=.0005
        elif(evnt == 1):
            volume+=.0005
        elif (evnt > 1 and evnt < 10):
            volume+=.01
        elif (evnt < 127 and evnt > 11):
            volume-=.01

        if (evnt == 0):
            Knob.onTouch = False
        

        mixer.setTrackVolume(mixerTrackNumber, volume)
        event.handled = True
    elif (ctrlID == IDKnob2):
        pan = mixer.getTrackPan(mixerTrackNumber)
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
        #print("IDKnob3", evnt)
        event.handled = True
    elif (ctrlID == IDKnob4):
        #print("IDKnob4", evnt)
        event.handled = True
