import speech_recognition as sr
import webbrowser
from googlesearch import search
import pyautogui
import time
import tkinter as tk


def speech_to_text():
    # Создаем объект Recognizer.
    r = sr.Recognizer()
    # Устанавливаем микрофон как источник звука.
    with sr.Microphone() as source:
        # Регулируем уровень громкости.
        r.adjust_for_ambient_noise(source)
        
        # Создаем и настраиваем всплывающее окно
        root = tk.Tk()
        root.title("Говорите")
        root.withdraw()
        root.update_idletasks()
        width = root.winfo_reqwidth()
        height = root.winfo_reqheight()
        x = (root.winfo_screenwidth() // 2) - (width // 2)
        y = (root.winfo_screenheight() // 2) - (height // 2)
        root.geometry("+{}+{}".format(x, y))
        root.deiconify()
        root.attributes("-alpha", 0.5)

        # Выводим приглашение на всплывающем окне
        label = tk.Label(root, text="Скажите что-нибудь:", font=("Calibri", 14))
        label.pack(padx=20, pady=20)

        # Записываем аудио и преобразуем его в текст с помощью Google Web Speech API.
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language="ru-RU")
        except Exception as e:
            text = ""
            print("Google Speech Recognition не смог распознать этот звук")
        root.destroy()
        print("Вы сказали: " + text)
        return text

def open_url_in_browser(url):
    # Открываем ссылку в браузере по умолчанию
    webbrowser.open(url)

def switch_to_previous_tab():
    # Имитируем нажатие сочетания клавиш Ctrl+Shift+Tab для переключения на предыдущую вкладку.
    pyautogui.hotkey('ctrl', 'shift', 'tab')

def close_current_tab():
    # Имитируем нажатие сочетания клавиш Ctrl+W для закрытия текущей вкладки.
    pyautogui.hotkey('ctrl', 'w')

def main():
    search_query = speech_to_text()
    # Ищем результаты поиска в Google.
    results = search(search_query, num_results=1)
    # Преобразуем генератор результатов поиска в список.
    results_list = list(results)
    # Открываем первую ссылку из результатов поиска в браузере по умолчанию.
    if len(results_list) > 0:
        url = results_list[0]
        print("Открываю ссылку: " + url)
        open_url_in_browser(url)
    else:
        print("По запросу " + search_query + " не найдено ни одной ссылки.")

if __name__ == "__main__":
    time.sleep(2)
    main()
