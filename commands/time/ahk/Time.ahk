
VObj := ComObjCreate("SAPI.SpVoice")
FormatTime, TimeStr,, H:mm tt
VObj.Speak(TimeStr)