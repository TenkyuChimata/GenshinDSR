# -*- coding: utf-8 -*-
import sys
import time
import psutil
import ctypes
import win32api
import win32con
import pyautogui
import subprocess
import pywintypes

game_width = 3840 # DSR resolution width
game_height = 2160 # DSR resolution height
origin_width = 2560 # Monitor resolution width
origin_height = 1440 # Monitor resolution height
launcher_name = "launcher.exe"
game_name = "GenshinImpact.exe"
process_path = r"C:\Program Files\Genshin Impact\launcher.exe"

if not ctypes.windll.shell32.IsUserAnAdmin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    sys.exit(0)

def check_process(process_name):
    for proc in psutil.process_iter(["name"]):
        if proc.info["name"] == process_name:
            return True
    return False

def change_resolution(width, height):
    while True:
        screen_width, screen_height = pyautogui.size()
        if screen_width != width and screen_height != height:
            devmode = pywintypes.DEVMODEType()
            devmode.PelsWidth = width
            devmode.PelsHeight = height
            devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT
            win32api.ChangeDisplaySettings(devmode, 0)
        else:
            break

subprocess.Popen(process_path)

while True:
    if not check_process(launcher_name):
        sys.exit(0)
    if check_process(game_name):
        change_resolution(game_width, game_height)
        sys.exit(0)
    time.sleep(0.1)
