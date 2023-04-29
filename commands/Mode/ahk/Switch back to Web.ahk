#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

; Step 1. Close Steam
Process, Close, steam.exe

; Step 2. Run VSC
Run C:\Users\den03\AppData\Local\Programs\Microsoft VS Code\Code.exe

; Step 3. Run Music
Run C:\Program Files\jarvis-app\commands\vk music\ahk\Run music.ahk

; Step 4. Run OSPanel
Run C:\OSPanel\Open Server Panel.exe

; Step 5. Run Docker
Run C:\Program Files\Docker\Docker\Docker Desktop.exe