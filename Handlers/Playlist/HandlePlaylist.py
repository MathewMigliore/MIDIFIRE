class PlaylistState(object):
    mixerTrackLastUsed = 0
    mixerBeginSelection = 0
    mixerBeginSelectionStored = 0
    mixerEndSelection = 0

    def __init__(self, mixerBeginSelectionStored, mixerTrackLastUsed, mixerBeginSelection , mixerEndSelection):
        self.mixerTrackLastUsed = mixerTrackLastUsed
        self.mixerBeginSelection = mixerBeginSelection
        self.mixerEndSelection = mixerEndSelection
        self.mixerBeginSelectionStored = mixerBeginSelectionStored

def HandelPlaylist(event):
    ctrlID = event.data1
    evnt = event.data2

def PlaylistPadsInit():
    print()