import psutil
import pyttsx3

engine = pyttsx3.init()


# Получаем информацию об использовании памяти
memory = psutil.virtual_memory()
used_memory = memory.used / 1024 / 1024 / 1024
total_memory = memory.total / 1024 / 1024 / 1024

# Формируем текст для озвучивания
text = f"Использование памяти {int(used_memory)} гигабайт из {int(total_memory)} гигабайт"

# Озвучивание текста
engine.say(text)
engine.runAndWait()
