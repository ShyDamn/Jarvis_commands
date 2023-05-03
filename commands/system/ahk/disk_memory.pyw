import psutil
import pyttsx3

# Создаем объект для генерации речи
engine = pyttsx3.init()

# Получаем информацию о дисках
for partition in psutil.disk_partitions():
    disk_usage = psutil.disk_usage(partition.mountpoint)
    used_gb = round(disk_usage.used / (1024**3))
    free_gb = round(disk_usage.free / (1024**3))
    percent_used = round(disk_usage.percent)
    drive_name = partition.device.split(':')[0]

    # Формируем текст для озвучивания и вывода на экран
    message = 'Использовано на диске {} {:.2f} Гб. Доступно {:.2f} Гб. Процент использования диска {}: {:.2f}%'.format(
        drive_name, used_gb, free_gb, drive_name, percent_used)
    print(message)

    # Озвучиваем текст системным голосом Windows
    engine.say(message)
    engine.runAndWait()
