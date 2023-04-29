pVoice := ComObjCreate("SAPI.SpVoice")
FormatTime, Today, %A%, d MMMM
pVoice.Speak(Today)
sleep 3000