#
# Defines how the pads are mapped in various modes.
#
from Utility.Colours import *
from Utility.Utils import *

# defines the pads when used as a set from 0..63
pdAllPads = [i for i in range(64)] 

#Banks are in reverse order - ie bottom row to top
pdBankA = [48, 49, 50, 51,
          32, 33, 34, 35, 
          16, 17, 18, 19,
           0,  1,  2,  3]

pdBankB = [52, 53, 54, 55,
          36, 37, 38, 39,
          20, 21, 22, 23,
           4,  5,  6,  7]

pdBankC = [56, 57, 58, 59,
          40, 41, 42, 43,
          24, 25, 26, 27,
          8,  9, 10, 11]

pdBankD = [60, 61, 62, 63, 
           44, 45, 46, 47,
           28, 29, 30, 31,
           12, 13, 14, 15 ]


padBankA = [0,  1,  2,  3, 4,  5,  6,  7,
            16, 17, 18, 19, 20, 21, 22, 23,
            32, 33, 34, 35, 36, 37, 38, 39,
            48, 49, 50, 51, 52, 53, 54, 55]

padBankB = [56, 57, 58, 59,
          40, 41, 42, 43,
          24, 25, 26, 27,
          8,  9, 10, 11]

padBankC = [60, 61, 62, 63, 
           44, 45, 46, 47,
           28, 29, 30, 31,
           12, 13, 14, 15 ]

#work area width
pdWorkAreaRowA = [  0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11]      # top row, first 12
pdWorkAreaRowB = [ 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]      # second row, first 12
pdWorkAreaRowC = [ 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43]     # third row, first 12
pdWorkAreaRowD = [ 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]     # fourth row, first 12

#full width
pdRowA = [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15]     
pdRowB = [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
pdRowC = [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]
pdRowD = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63] 

pdPatternStripA = pdWorkAreaRowA 
pdPatternStripB = pdWorkAreaRowB 
pdChanStripA    = pdWorkAreaRowC 
pdChanStripB    = pdWorkAreaRowD 
pdPatternStripANoNav = pdRowA 
pdPatternStripBNoNav = pdRowB 
pdChanStripANoNav    = pdRowC
pdChanStripBNoNav    = pdRowD 

#full size for alt mode
pdPlaylistSelStripA = pdRowA 
pdPlaylistSelMutesA = pdRowB 
pdMarkers  = pdRowC
pdProgress = [] 
pdProgress.extend(pdRowC)
pdProgress.extend(pdRowD) 

pdPlaylistStripA = pdWorkAreaRowA
pdPlaylistMutesA = pdWorkAreaRowB
pdPlaylistStripB = pdWorkAreaRowC
pdPlaylistMutesB = pdWorkAreaRowD
pdPlaylistStripANoNav = pdRowA
pdPlaylistMutesANoNav = pdRowB
pdPlaylistStripBNoNav = pdRowC
pdPlaylistMutesBNoNav = pdRowD

# these are defined in "FPC" order. Bottom Left FPC Pad is first value in index
# so I define them bottom to top order for each set.
pdFPCA = pdBankA
pdFPCB = pdBankB 

# quick slect FPC channels in drum mode - note unlike banks EXCEPT these are in top to bottom order
pdFPCChannels = [ 8,  9, 10, 11,
                 24, 25, 26, 27,
                 40, 41, 42, 43,
                 56, 57, 58, 59 ]

#helper to get the pads needed to map to notes.
def getDrumPads(isAlt, noNav, layoutIdx):
    pads = []
    if(not isAlt): # FPC Pads
        pads.extend(pdFPCA)
        pads.extend(pdFPCB)
    else: #ALT Drum mode 
        if(layoutIdx == 0): # bank style
            pads.extend(pdBankA)
            pads.extend(pdBankB)
            pads.extend(pdBankC)
            if(noNav):
                pads.extend(pdBankD)
        else: # strip style
            if(noNav):
                pads.extend(pdRowD)
                pads.extend(pdRowC)
                pads.extend(pdRowB)
                pads.extend(pdRowA)
            else:
                pads.extend(pdWorkAreaRowD)
                pads.extend(pdWorkAreaRowC)
                pads.extend(pdWorkAreaRowB)
                pads.extend(pdWorkAreaRowA)
    return pads 

pdChordBar =   [ 0, 1, 2,  3,  4,  5,  6 ]

pdChordFuncs     = [ 7,  8, 9, 10, 11 ] 
pd7th       = 7
pdNormal    = 8
pdInv1      = 9
pdInv2      = 10

pdWorkArea = [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11,
              16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
              32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43,
              48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59 ]

pdMacros = [ 12, 13, 14, 15, 28, 29, 30, 31]

# thx to "a candle" for the tab idea
pdShiftTab = 44
pdEsc = 45
pdUp = 46
pdEnter = 47
pdTab = 60
pdLeft = 61
pdDown = 62
pdRight = 63
pdUDLR = [pdShiftTab, pdEsc, pdUp, pdEnter, pdTab, pdLeft, pdDown, pdRight]

# for modes that need channel specific window control - ie Note mode, FPC, etc
pdShowChanEditor = 44
pdShowChanPianoRoll = 60
pdShowChanPads = [pdShowChanEditor, pdShowChanPianoRoll]
colShowChanPads = [cWhite, cWhite]

#navigation
pdNav = [ 44, 45, 46, 47,
          60, 61, 62, 63]

pdVelocityUp = 44
pdVelocityDown = 60
pdVelocityNav = [pdVelocityUp, pdVelocityDown]
colPresetNav  = [cWhite, cDimWhite]

#nav for PATTERNS and DRUMS
pdPresetPrev = 47
pdPresetNext = 63
pdPresetNav = [pdPresetPrev, pdPresetNext]
colPresetNav = [cWhite, cDimWhite]

pdNoteRepeat = 46
#colNoteRepeat = getShade(cOrange, shNorm)
#colNoteRepeatOn = getShade(cOrange, shLight)
#pdNoteRepeatLength = 62
#colNoteRepeatLength = getShade(cOrange, shNorm)

pdSnapUp = 45
pdSnapDown = 61
pdSnapNav = [pdSnapUp, pdSnapDown]
#colSnapUp = getShade(cYellow, shNorm)
#colSnapDown = getShade(cYellow, shNorm)

pdLayoutPrev = 45
pdLayoutNext = 61
pdLayoutNav = [pdLayoutPrev, pdLayoutNext]
#colLayoutPrev = getShade(cMagenta, shNorm)
#colLayoutNext = getShade(cMagenta, shDark)

#nav for NOTES
pdRootNotePrev = 45
pdRootNoteNext = 61
pdOctavePrev = 46
pdOctaveNext = 62
pdScalePrev = 47
pdScaleNext = 63

#colOctavePrev = getShade(cBlue, shLight)
colOctaveNext = cBlue

pdNoteFuncs = [pdScalePrev, pdScaleNext, pdRootNotePrev, pdRootNoteNext, pdOctavePrev, pdOctaveNext]
#colNoteFuncs = [getShade(cGreen, shLight), cGreen, getShade(cPurple, shLight), cPurple, colOctavePrev, colOctaveNext]
