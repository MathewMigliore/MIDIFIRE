def handle_deinit():
    clear_all_pads()
    ClearDisplay()
    send_cc(IDKnobModeLEDArray, 16)
    for ctrlID in getNonPadLightCtrls():
        SendCC(ctrlID, 0)