#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

; Step 1. Start Music
Run C:/Program Files/Google/Chrome/Application/chrome.exe "https://vk.com/audios328786839?section=all"
Sleep 8000
Send {Alt down}
Send {Down}
sleep 1000
Send {Alt Up}



