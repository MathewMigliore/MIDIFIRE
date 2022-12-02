# name = FireNFX Definitions
#
# most of this is copied from the Image-Line device_Fire code
# from harmonicScales import *

# PAD Modes
MODE_PATTERNS = 0 # was MODE_STEP
MODE_NOTE = 1
MODE_DRUM = 2
MODE_PERFORM = 3

#PAD_MODE = MODE_PATTERNS

# Knob Modes
KM_CHANNEL = 0
KM_MIXER = 1
KM_USER1 = 2
KM_USER2 = 3

#Fire specific
ManufacturerIDConst = 0x47
DeviceIDBroadCastConst = 0x7F
ProductIDConst = 0x43

# Message IDs (from PC to device)
MsgIDGetAllButtonStates = 0x40
MsgIDGetPowerOnButtonStates = 0x41
MsgIDSetRGBPadLedState = 0x65
MsgIDSetManufacturingData = 0x79
MsgIDDrawScreenText = 0x08
MsgIDDrawBarControl = 0x09
MsgIDFillOLEDDiplay = 0x0D
MsgIDSendPackedOLEDData = 0x0E
MsgIDSendUnpackedOLEDData = 0x0F

# OnRefresh flags
MixerSelectSingle = 263
MixerSelectRange = 7

# Note/CC values for controls
IDKnob1 = 16 #0x10
IDKnob2 = 17 #0x11
IDKnob3 = 18 #0x12
IDKnob4 = 19 #0x13

IDJogWheel = 118 #0x76
IDSelect = IDJogWheel 

IDJogWheelDown = 25 #0x19
IDSelectDown = IDJogWheelDown

IDKnobMode = 26 # 0x1B # shouldn't it be 0x1A ? (doc says 0x1B for outbound & 0x1A for inbound...)
IDKnobModeLEDArray = 27

IDPatternUp = 31 #0x1F
IDUp = IDPatternUp
IDPatternDown = 32 # 0x20
IDDown = IDPatternDown

IDBrowser = 33 #0x21

IDBankL = 34 #0x22
IDBankR = 35 #0x23

IDLeft = IDBankL
IDRight = IDBankR 

IDMute1 = 36 #0x24
IDMute2 = 37 #0x25
IDMute3 = 38 #0x26
IDMute4 = 39 #0x27

# ADDED
IDPlaylist = 36 #0x24
IDChannelRack = 37 #0x25
IDPianoRoll = 38 #0x26
IDMixer = 39 #0x27

IDTrackSel1 = 40 #0x28
IDTrackSel2 = 41  #0x29
IDTrackSel3 =  42 #0x2A
IDTrackSel4 = 43  #0x2B

# ADDED
IDPlaylistFullScreen = 40 #0x28
IDChannelRackFullScreen = 41  #0x29
IDPianoRollFullScreen =  42 #0x2A
IDMixerFullScreen = 43  #0x2B

IDStepSeq = 44 #0x2C
IDAccent = 44
IDNote = 45 #0x2D
IDSnap = 45
IDDrum = 46 #0x2E
IDTap = 46
IDPerform = 47 #0x2F
IDOverview = 47

IDShift = 48 # 0x30
IDAlt = 49 #0x31

IDPatternSong = 50 #0x32
IDMetronome = 50 #
IDPlay = 51 #0x33
IDWait = 51 
IDStop = 52 #0x34
IDCount = 52
IDRec = 53 #0x35
IDLoop = 53 

# Pads
IDPadFirst = 54
IDPadLast = 117

TransportCtrls = [IDPatternSong, IDPlay, IDStop, IDRec]
ShiftAltCtrls = [IDShift, IDAlt]
PadModeCtrls = [IDStepSeq, IDNote, IDDrum, IDPerform]
PadModeNames = ['Pattern', 'Note', 'Drum', 'Perform']
PadModeShortNames = ['PTN', 'NOTE', 'DRM', 'PERF']
KnobCtrls = [IDKnob1, IDKnob2, IDKnob3, IDKnob4]
SelectWheelCtrls = [IDSelect, IDSelectDown]
PadCtrls = list()
for ctrlID in range(IDPadFirst, IDPadLast+1):
    PadCtrls.append(ctrlID)
MuteControls = [IDMute1, IDMute2, IDMute3, IDMute4]
TabControls = [IDMixer, IDChannelRack, IDPlaylist,  IDPianoRoll]
FullScreenLED = [IDPlaylistFullScreen, IDChannelRackFullScreen, IDPianoRollFullScreen, IDMixerFullScreen]
# the operating knobs mode NOT Pad mode
KnobModeNames = ["Channel", "Mixer", "User1", "User2"]
KnobModeShortNames = ["Ch", "Mx", "U1", "U2"]
KnobModeCtrlID = IDKnobMode
IDKnobModeLEDVals = [1,2,4,8]

PattUpDnCtrls = [IDPatternUp, IDPatternDown]
GridLRCtrls = [IDBankL, IDBankR]

IDPage0 = IDMute1
IDPage1 = IDMute2
IDPage2 = IDMute3
IDPage3 = IDMute4

PageCtrls = [IDPage0, IDPage1, IDPage2, IDPage3] # using these since I dont use the step mode

BeatIndicators = [IDTrackSel1, IDTrackSel2, IDTrackSel3, IDTrackSel4]

def getNonPadLightCtrls():
    NonPadLightCtrls = []
    NonPadLightCtrls.extend(PattUpDnCtrls)
    NonPadLightCtrls.append(IDBrowser)
    NonPadLightCtrls.extend(GridLRCtrls)
    NonPadLightCtrls.extend(PageCtrls)
    NonPadLightCtrls.extend(BeatIndicators)
    NonPadLightCtrls.extend(PadModeCtrls)
    NonPadLightCtrls.extend(ShiftAltCtrls)
    NonPadLightCtrls.extend(TransportCtrls)
    return NonPadLightCtrls



IdxStepSeq = 14
IdxNote = 15
IdxDrum = 16
IdxPerform = 17
IdxShift = 18
IdxAlt = 19
IdxPatternSong = 20
IdxPlay = 21
IdxStop = 22
IdxRec = 23
IdxButtonLast = 23

# Colours
DualColourOff = 0x00
DualColourHalfBright1 = 0x01
DualColourHalfBright2 = 0x02
DualColourFull1 = 0x03
DualColourFull2 = 0x04

SingleColourOff = 0x00
SingleColourHalfBright = 0x01
SingleColourFull = 0x02

IDColPattMode = DualColourHalfBright2
IDColSongMode = DualColourHalfBright1 

IDColPlayOff = DualColourOff
IDColPlayOn = DualColourHalfBright1
IDColPlayOnBar = DualColourFull2
IDColPlayOnBeat = DualColourFull1

IDColStopOff = DualColourOff
IDColStopOn = DualColourHalfBright2

IDColRecOff =  DualColourOff
IDColRecOn = DualColourFull1

IDColMetronome = DualColourFull2
IDColWait = DualColourFull2
IDColCount = DualColourFull2
IDColLoop = DualColourFull2

#

#for the scale notes
NotesListFlats = ['C','Db','D','Eb','E','F','Gb','G','Ab','A','Bb','B']
NotesListSharps = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
NotesList = NotesListSharps
#list of notes values
NoteValueList = [0,1,2,3,4,5,6,7,8,9,10,11]

OctavesList = [1,2,3,4,5]



lvlN = -2 # Never
lvlA = -1 # Always
lvl0 = 0  # general use
lvlE = 1
lvlH = 2
lvlR = 3
lvlU = 4
lvlD = 5
level0 = [lvl0, '....']
levelE = [lvlE, 'SysEvent']
levelH = [lvlH, 'Handler']
levelR = [lvlR, 'Refresh']
levelU = [lvlU, 'Update']
levelD = [lvlD, 'Display']
prnLevels = [level0, levelE, levelH, levelR, levelU, levelD]

FLEFFECTS = 'CHAN FX'
NOSUPPTEXT = "UNSUPPORTED"
