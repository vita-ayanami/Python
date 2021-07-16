# Импортировал библиотеку для работы с железом. https://psutil.readthedocs.io/en/latest/
import psutil

# Участок кода, позволяющий узнать кол-во ядер:
print(f"Физические ядра: {psutil.cpu_count(logical=False)}")
print(f"Всего ядер: {psutil.cpu_count(logical=True)}")

# Участок кода, позволяющий узнать частоту процессора:
cpufreq = psutil.cpu_freq()
print("")
print(f"Максимальная частота: {cpufreq.max: .2f}MHZ")
print(f"Минимальная частота: {cpufreq.min: .2f}MHZ")
print(f"Частота сейчас: {cpufreq.current: .2f}MHZ")

# Участок кода, позволяющий узнать использование ядер процессора:
print("")
print("Использование ядер процессора: ")
for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    print(f"Загрузка на ядро: {i}: {percentage} процентов.")
print(f"Средняя загрузка процессора: {psutil.cpu_percent()} процентов. ")

# Участок кода, позволяющий узнать использование диска:
print("")
print(f"Использование диска: {psutil.disk_usage('/')}")
print(f"Разделов на диске: {psutil.disk_partitions()}")

# Участок кода, позволяющий узнать кол-во пользователей в системе, а также некоторые их данные:
print("")
usr = psutil.users()
print(f"Пользователей в системе: {usr}")
