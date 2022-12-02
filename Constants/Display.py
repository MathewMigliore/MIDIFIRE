DisplayWidth = 128
DisplayHeight = 64
# Text settings
Font6x8 = 0
Font6x16 = 1
Font10x16 = 2
Font12x32 = 3
JustifyLeft = 0
JustifyCenter = 1
JustifyRight = 2
ScreenDisplayDelay = 2 # delay (in ms) required to access the screen (seems slow)

TextScrollPause = 5
TextScrollSpeed = 2
TextDisplayTime = 4000

TimedTextRow = 1
FPSRow = 3
FireFontSize = 15 # was 16
TextOffset = -4
TextRowHeight = 18 #was 20

Idle_Interval = 100
Idle_Interval_Max = 8

ScreenActiveTimeout = 10 # seconds to keep screen active (screen has its own timeout which will kick in after this)
ScreenAutoTimeout = 5

tlNone = 1
tlText = 1 << 1
tlBar = 1 << 2
tlMeter = 1 << 3

ROWTOP = 0
ROWMID = 1
ROWBOT = 2