import psutil
import pyttsx3

cpu_percent = psutil.cpu_percent(interval=1)
cpu_count = psutil.cpu_count(logical=False)
cpu_usage_percent = cpu_percent / cpu_count

msg = f"Использование процессора: {cpu_usage_percent:.2f} percent"
engine = pyttsx3.init()
engine.say(msg)
engine.runAndWait()
