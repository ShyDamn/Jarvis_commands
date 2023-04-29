#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

; Step 1. Close Steam
Process, Close, steam.exe

; Step 2. Run Idea
Run C:\Program Files\JetBrains\IntelliJ IDEA 2022.1.2\bin\idea64.exe

; Step 3. Run Music
Run C:\Program Files\jarvis-app\commands\vk music\ahk\Run music.ahk

; Step 4. Open ChatGPT
Run C:/Program Files/Google/Chrome/Application/chrome.exe "https://chat.chatbot.sex/chat/"