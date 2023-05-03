import psutil
import pyttsx3

engine = pyttsx3.init()

# Получаем информацию о памяти
memory_percent = psutil.virtual_memory().percent

# Озвучиваем текст про загрузку памяти
engine.say("Использование РАМ: {} percent".format(memory_percent))
engine.runAndWait()

    
