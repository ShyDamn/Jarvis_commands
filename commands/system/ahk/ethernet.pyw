import psutil
import pyttsx3

engine = pyttsx3.init()

net_io_counters = psutil.net_io_counters()
bytes_sent = net_io_counters.bytes_sent
bytes_recv = net_io_counters.bytes_recv
total_bytes = bytes_sent + bytes_recv
total_mb = total_bytes / 1024 / 1024  # переводим в мегабайты
total_percent = total_mb / 10  # показываем в процентах от 10 мбит/с
message = "Сеть использована на " + str(round(total_percent)) + " процентов"
engine.say(message)
engine.runAndWait()
