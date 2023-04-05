from Constants.System import *
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

