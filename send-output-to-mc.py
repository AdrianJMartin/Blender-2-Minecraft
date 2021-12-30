import time
import win32gui

WM_ACTIVATE = 0x06
WM_ACTIVATEAPP = 0x06
WM_KEYDOWN = 0x0100
WM_KEYUP = 0x0101
WM_CHAR = 0x0102

VK_SHIFT = 0x10
VK_ESCAPE = 0x1B
VK_OEM_7 = 0xDE

SW_SHOW = 0x05
SW_ACTIVATE = 0x09

windows = []

mc_hwnd = 0

mc_child_windows = []

ime_child_windows = []


def enum_windows_callback(hwnd, data):
    win_text = win32gui.GetWindowText(hwnd)
    pwHwnd = win32gui.GetParent(hwnd)

    windows.append({'pWnd': pwHwnd, 'hWnd': hwnd, 'text': win_text})


hr = win32gui.EnumWindows(enum_windows_callback, "Minecraft")


if hr is None:

    for w in windows:
        if w["text"].find("Minecraft") > -1:
            mc_hwnd = w['hWnd']
            break

    for w in windows:
        if w["pWnd"] == mc_hwnd:
            mc_child_windows.append(w)

    for w in windows:
        if w['pWnd'] == mc_child_windows[0]['hWnd']:
            ime_child_windows.append(w)


print("mc hwnd:", mc_hwnd)
for w in mc_child_windows:
    print("mc child:", w['hWnd'], " WinText:", w['text'])


# Activate Minecraft window
# not sure why it wont come to the front...

hr = win32gui.SendMessage(mc_hwnd, WM_ACTIVATEAPP, 1, 0)
print(hr)
time.sleep(.1)

hr = win32gui.SendMessage(mc_hwnd, WM_ACTIVATE, 2, 0)
print(hr)
time.sleep(.1)

# send esc to dismiss the pause screen
hr = win32gui.PostMessage(mc_hwnd, WM_KEYDOWN, VK_ESCAPE, 0x00010001)
time.sleep(.1)



# send / to bring up console
hr = win32gui.PostMessage(mc_hwnd, WM_KEYDOWN, 0xBF, 0x0035_0001)

time.sleep(.1)

#for c in "FILL ~0 ~0 ~1 ~0 ~0 ~11 DIRT":
for c in "~~~~~~~~~~~~~~":

    if c == '~':
        win32gui.PostMessage(mc_hwnd, WM_KEYDOWN, VK_SHIFT, 0x002A_0001)
        time.sleep(.1)
        win32gui.PostMessage(mc_hwnd, WM_KEYDOWN, VK_OEM_7, 0x002B_0001)
        time.sleep(.1)
        win32gui.PostMessage(mc_hwnd, WM_KEYUP  , VK_SHIFT, 0xC02A_0001)
        time.sleep(.1)
    else:

        win32gui.PostMessage(mc_hwnd, WM_KEYDOWN, ord(c), 0)

    time.sleep(.1)


win32gui.PostMessage(mc_hwnd, WM_KEYDOWN, ord("\n"), 0)
time.sleep(.1)

hr = win32gui.PostMessage(mc_hwnd, WM_KEYDOWN, ' ', 0x0021_0001)


# send esc to leave console
hr = win32gui.PostMessage(mc_hwnd, WM_KEYDOWN, VK_ESCAPE, 0x0001_0001)
# send esc to pause game
hr = win32gui.PostMessage(mc_hwnd, WM_KEYDOWN, VK_ESCAPE, 0x0001_0001)
# sending again seem to make the pause screen come up...?
hr = win32gui.PostMessage(mc_hwnd, WM_KEYDOWN, VK_ESCAPE, 0x0001_0001)
