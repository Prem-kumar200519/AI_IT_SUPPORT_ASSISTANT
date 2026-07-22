import platform
import psutil

print("===== SYSTEM INFORMATION =====")

# Operating System
print("Operating System :", platform.system(), platform.release())

# CPU Usage
print("CPU Usage        :", psutil.cpu_percent(interval=1), "%")

# RAM Usage
memory = psutil.virtual_memory()
print("RAM Usage        :", memory.percent, "%")

# Disk Usage
disk = psutil.disk_usage('/')
print("Disk Usage       :", disk.percent, "%")