from win32gui import *
from win32process import *
from win32api import *
from win32con import *
import ctypes

life_addr = 0x4A57F4
bomb_addr = 0x4A5800
bombpiece_addr = 0x4A5804
season_addr = 0x4A5808
life_init_addr = 0x42CDF4
bomb_init_addr = 0x42E5B1
bombpiece_init_addr = 0x42E5CF
season_init_addr = 0x42CECC


def read(addr):
    base = ctypes.c_int()
    DLL.ReadProcessMemory(int(PROCESS),addr,ctypes.byref(base),4,None)
    print("0x%X"%addr,end='\t')
    print(base)
    return base
def write(addr,content):
    base = ctypes.c_int(content)
    DLL.WriteProcessMemory(int(PROCESS),addr,ctypes.byref(base),4,None)

HANDLE = FindWindow(None,r"東方天空璋丂乣 Hidden Star in Four Seasons. ver 1.00a")
hid,pid = GetWindowThreadProcessId(HANDLE)
PROCESS = OpenProcess(PROCESS_VM_READ|PROCESS_VM_WRITE|PROCESS_VM_OPERATION,True,pid)
DLL = ctypes.windll.LoadLibrary(".\\kernel32.dll")

write(life_init_addr,8)
write(bomb_init_addr,2)
