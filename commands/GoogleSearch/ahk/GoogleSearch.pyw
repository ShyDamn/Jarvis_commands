import speech_recognition as sr
import webbrowser

# Создаем объект Recognizer, который будет распознавать речь
r = sr.Recognizer()

# Определяем источник звука - микрофон
with sr.Microphone() as source:
    
    # Слушаем и записываем аудио в формате PCM с частотой дискретизации 16000 Гц
    audio_data = r.record(source, duration=5, offset=0)
    
    # Используем метод recognize_google для распознавания речи и преобразования ее в текст
    text = r.recognize_google(audio_data, language="ru-RU")
    
    # Формируем URL-адрес для поиска в Google
    url = f"https://www.google.com/search?q={text}"
    
    # Открываем браузер и переходим по URL-адресу
    webbrowser.open(url)
