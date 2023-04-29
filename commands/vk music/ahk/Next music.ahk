#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

; Step 1. Next Music
If ErrorLevel = 0
{
Run C:/Program Files/Google/Chrome/Application/chrome.exe "https://google.com/"
sleep 5000
Send {Alt down}
Send {Right}
sleep 1000
Send {Alt Up}
}
Return