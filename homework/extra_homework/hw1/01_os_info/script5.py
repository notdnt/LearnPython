import platform
import sys

os_name = platform.system()
version = sys.version

result = f"OS info is {os_name} Python version is {version}"

print(result)

with open("os_info.txt", "w") as file:
    file.write(result)
