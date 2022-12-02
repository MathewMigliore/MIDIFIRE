def HandleDeInit():
    ClearAllPads()
    ClearDisplay()
    SendCC(IDKnobModeLEDArray, 16)
    for ctrlID in getNonPadLightCtrls():
        SendCC(ctrlID, 0)