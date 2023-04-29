from PIL import ImageGrab
import datetime
import os

# Получаем путь к директории скрипта
script_dir = os.path.dirname(os.path.abspath(__file__))

# Получаем размеры экрана
screen_size = (1920, 1080) # Укажите нужный размер экрана

# Создаем скриншот
screenshot = ImageGrab.grab()

# Создаем папку "Screenshot", если ее не существует
screenshot_dir = os.path.join(script_dir, 'Screenshot')
if not os.path.exists(screenshot_dir):
    os.makedirs(screenshot_dir)

# Генерируем уникальное имя файла с текущей датой и временем
filename = "screenshot_{}.png".format(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))

# Сохраняем скриншот в папку "Screenshot" в директории скрипта с уникальным именем
filepath = os.path.join(screenshot_dir, filename)
screenshot.save(filepath)
