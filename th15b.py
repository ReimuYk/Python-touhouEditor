from win32gui import *
from win32process import *
from win32api import *
from win32con import *
import ctypes

##def foo(hwnd,mouse):
##    if IsWindow(hwnd) and IsWindowEnabled(hwnd) and IsWindowVisible(hwnd):
##        print(GetWindowText(hwnd))
##
##EnumWindows(foo,0)
life_addr = 0x4E7450
bomb_addr = 0x4E745C
life_init_addr = 0x43C2B3
bomb_init_addr = 0x43E6F1

def read(addr):
    base = ctypes.c_int()
    DLL.ReadProcessMemory(int(PROCESS),addr,ctypes.byref(base),4,None)
    print("0x%X"%addr,end='\t')
    print(base)
    return base
def write(addr,content):
    base = ctypes.c_int(content)
    DLL.WriteProcessMemory(int(PROCESS),addr,ctypes.byref(base),4,None)

HANDLE = FindWindow(None,r"東方紺珠伝　～ Legacy of Lunatic Kingdom. ver 1.00b")
hid,pid = GetWindowThreadProcessId(HANDLE)
PROCESS = OpenProcess(PROCESS_VM_READ|PROCESS_VM_WRITE|PROCESS_VM_OPERATION,True,pid)
DLL = ctypes.windll.LoadLibrary(".\\kernel32.dll")

write(life_init_addr,8)
write(bomb_init_addr,2)
