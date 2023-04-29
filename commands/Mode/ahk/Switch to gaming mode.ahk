#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

; Step 1. Close all process
Process, Close, idea64.exe
Process, Close, pycharm64.exe
Process, Close, Code.exe
Process, Close, phpstorm64.exe
Process, Close, Open Server Panel.exe
Process, Close, chrome.exe
Process, Close, Docker Desktop.exe

; Step 2. Open Steam
Run C:\Program Files (x86)\Steam\Steam.exe

; Step 3. Open Wallpaper
Run C:\Program Files (x86)\Steam\steamapps\common\wallpaper_engine\wallpaper64.exe

; Step 4. WinMinimize
sleep 15000
Run C:\Program Files\jarvis-app\commands\browser\ahkahk\WinMinimizeAll.ahk
